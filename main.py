"""
tgvc-userbot, Telegram Voice Chat Userbot
Copyright (C) 2021  Dash Eclipse

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from os import environ

# import logging
from pyrogram import Client, idle

API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
SESSION_NAME = environ["SESSION_NAME"]
BOT_TOKEN = environ["BOT_TOKEN"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc." + environ["PLUGIN"],
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)

class xbot(Client):

    def __init__(self):
        super().__init__(
            "Dump",
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN
        )

    async def start(self):
        await super().start()
        print(f"xbot with for Pyrogram started.")

    async def stop(self, *args):
        await super().stop()
        print("Bot stopped. Bye.")


XBOT = xbot()
XBOT.run()
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
