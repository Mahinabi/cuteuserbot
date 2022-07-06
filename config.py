import os
import logging
import aiohttp
from dotenv import load_dotenv
from pyrogram import Client
from pyrogram.types import *
from pytgcalls import PyTgCalls


logging.basicConfig(level=logging.INFO)
                    
if os.path.exists("Internal"):
    load_dotenv("Internal")

API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

SESSION = os.getenv("SESSION", "")
SESSION2 = os.getenv("SESSION2", "")
SESSION3 = os.getenv("SESSION3", "")
SESSION4 = os.getenv("SESSION4", "")
SESSION5 = os.getenv("SESSION5", "")
SESSION6 = os.getenv("SESSION6", "")
SESSION7 = os.getenv("SESSION7", "")
SESSION8 = os.getenv("SESSION8", "")
SESSION9 = os.getenv("SESSION9", "")
SESSION10 = os.getenv("SESSION10", "")

SUDO_USERS = list(map(int, os.getenv("SUDO_USERS", "1323020756").split()))
aiohttpsession = aiohttp.ClientSession()

#-------------------------BOT-----------------------------

bot = Client(
    'AltronUserbot',
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins={'root': 'AltronUserbot.bot'},
)

#-------------------------CLIENTS-----------------------------

if SESSION:
    client = Client(SESSION, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py = PyTgCalls(client)
else:
    client = None
    call_py = None

if SESSION2:
    client2 = Client(SESSION2, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py2 = PyTgCalls(client2)
else:
    client2 = None
    call_py2 = None

if SESSION3:
    client3 = Client(SESSION3, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py3 = PyTgCalls(client3)
else:
    client3 = None
    call_py3 = None

if SESSION4:
    client4 = Client(SESSION4, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py4 = PyTgCalls(client4)
else:
    client4 = None
    call_py4 = None

if SESSION5:
    client5 = Client(SESSION5, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py5 = PyTgCalls(client5)
else:
    client5 = None
    call_py5 = None

if SESSION6:
    client6 = Client(SESSION6, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py6 = PyTgCalls(client6)
else:
    client6 = None
    call_py6 = None
        
if SESSION7:
    client7 = Client(SESSION7, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py7 = PyTgCalls(client7)
else:
    client7 = None
    call_py7 = None

if SESSION8:
    client8 = Client(SESSION8, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py8 = PyTgCalls(client8)
else:
    client8 = None
    call_py8 = None

if SESSION9:
    client9 = Client(SESSION9, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py9 = PyTgCalls(client9)
else:
    client9 = None
    call_py9 = None

if SESSION10:
    client10 = Client(SESSION10, API_ID, API_HASH, plugins=dict(root="AltronUserbot.userbot"))
    call_py10 = PyTgCalls(client10)
else:
    client10 = None
    call_py10 = None
