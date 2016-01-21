# MahvelBot v0.1
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
            # if 'reboot' in message.content.lower() and message.author.id == self.config.owner_id:
            #     print('unloading commands')
            #     self.unload_extension('ammybot.command')
            #     print('successfully unloaded commands')
            #     print('loading commands')
            #     self.load_extension('ammybot.command')
            #     print('successfully loaded commands')
            # else:
                await self.process_commands(message)
                #await command.getCommand(message, self)



    async def on_member_join(self, member):
        await self.send_message(member.server, '<@{}> has joined the server! **#MAHVELLIVES**'.format(member.id))
        await self.send_message(member, 'Welcome {}! Type !help for a list of available commands.'.format(member.name))


# if __name__ == '__main__':
#     print('starting marvel bot')
#     bot = MahvelBot()
#     print('created marvel bot')
#     @bot.command()
#     async def add(left : int, right : int):
#         """Adds two numbers together."""
#         print('created add command')
#         await bot.say(left + right)
#     bot.run()