import os
import discord
from discord.ext import commands
from flask import Flask
from threading import Thread

# Веб-сервер для поддержания активности на Render
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# Настройка бота Discord
intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Вставь сюда данные (ID сервера, ID канала "Основа-1" и Токен бота)
GUILD_ID = 1560639563502985326    # <-- ID сервера Va1lka 26.3
CHANNEL_ID = 1560639565889409208  # <-- ID канала Основа-1
TOKEN = MTU2MTI2OTkzNzQ1OTQzNzU2OA.GwuLLe.LJOk9yoPDcwqKl3XhpCHzBbI2CFzY3PkHozSTo         # <-- Токен бота

@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен!")
    guild = bot.get_guild(GUILD_ID)
    if guild:
        channel = guild.get_channel(CHANNEL_ID)
        if channel and isinstance(channel, discord.VoiceChannel):
            try:
                await channel.connect()
                print(f"Бот зашел в {channel.name}!")
            except Exception as e:
                print(f"Ошибка подключения: {e}")

keep_alive()
bot.run(TOKEN)
