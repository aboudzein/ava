## AVABot

---

[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)][![GitHub issues](https://img.shields.io/github/issues/Naereen/StrapDown.js.svg)]

Imagine having a personal assistant that can help you with your daily tasks. Imagine having a bot that can answer your questions, schedule events, provide weather forecasts and much more. Imagine having a bot that can do all of this and more, all in one place. Well, now you can.

Introducing AVA , an open-source Discord bot that serves as a helpful assistant for your daily tasks. This bot is powered by the OpenAI API and is built using Python and the Discord API. It utilizes natural language processing techniques to understand the user's intent and perform specific actions. Some of its features include answering questions, scheduling events, providing weather forecasts and much more.

The bot is easy to set up and customize to fit your needs. It also has a simple and user-friendly interface that makes it easy for anyone to use. Whether you're a developer looking to improve your skills or a user looking for a helpful bot, AVA is the perfect choice.

This project is open for contributions, feel free to fork it, improve it and create pull requests.

## Getting Started

---

1. **Clone the repository**: First, you will need to clone the repository to your local machine using git. You can do this by running the following command in your terminal:

```
git clone https://github.com/username/your-project-name.git
```

2. **Create a virtual environment**: Next, you will need to create a virtual environment for your project. This is to ensure that the dependencies and packages installed for your project do not interfere with other projects on your machine. You can create a virtual environment using the following command:

```
python -m venv env
```

3. **Activate the virtual environment**: Once the virtual environment is created, you will need to activate it. You can do this by running the following command:

```
source env/bin/activate
```

4. **Install the dependencies**: Next, you will need to install the dependencies for your project. You can do this by running the following command:

```
pip install -r requirements.txt
```

5. **Add your Discord bot token** : You need to create a discord bot on discord developer portal and get the token then you need to add it to your project. You can do this by creating a new file called `.env` in the root of your project, and adding the following line:

```
DISCORD_TOKEN=your_token_here
```

6. **Run the bot**: Finally, you can run the bot by running the following command:

```
python src/main.py
```
