# AmmyBot v0.2
#

import asyncio
import imp
import discord
from ammybot.config import Config
from discord.ext import commands
from ammybot import command_old

class AmmyBot(commands.Bot):
    def __init__(self, config_file='config/options.txt'):
        self.config = Config(config_file)
        super().__init__(command_prefix=self.config.command_prefix)
        self.load_extension('ammybot.command')

    def run(self):
        return super().run(self.config.username, self.config.password)


    async def on_ready(self):
        print('Logged in as')
        print('Username: ' + self.user.name)
        print('ID: ' + self.user.id)
        print('[Server List]')
        for server in self.servers:
            print(server.name)

    async def on_message(self, message):

        #makes sure bot does not respond to itself
        if message.author == self.user:
            return
        if message.content.startswith(self.config.command_prefix):
                await self.process_commands(message)


if __name__ == '__main__':
    bot = AmmyBot()
    bot.run()