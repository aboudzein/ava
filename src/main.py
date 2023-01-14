import os
import openai
import discord
import nltk
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize
from dotenv import load_dotenv

from services.translate_text import async_translate_text


load_dotenv()


# OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = openai_api_key

# NLP Cloud API key
nlpcloud_api_key = os.getenv("NLPCLOUD_API_KEY")


client = discord.Client(intents=discord.Intents.all())


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    user_id = message.author.id
    if message.author == client.user:
        return

    nlu_response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{message.content}",
        max_tokens=2048,
        n=1,
        stop=None,
        temperature=0.9,
    )

    response = nlu_response["choices"][0]["text"]

    await message.channel.send(response)

    # result = await async_translate_text(f"{message.content}", nlpcloud_api_key, "ace_Arab", "eng_Latn", client, user_id)

    # print(result)


# Discord API token
TOKEN = os.getenv("DISCORD_TOKEN")

client.run(TOKEN)
