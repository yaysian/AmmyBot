import discord
from discord.ext import commands
import random

class Commands():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def avatar(self, ctx, user = ''):
        """Returns the avatar of the user specified. If no user is specified, the sender's avatar is returned."""
        isYou = False
        if user and user.strip('<@>') != ctx.message.author.id:
            targetUser = discord.utils.find(lambda m: m.id == user.strip('<@>'), ctx.message.server.members)
        else:
            targetUser = ctx.message.author
            isYou = True
        if isYou:
            if targetUser.avatar_url:
                await self.bot.say('Your avatar:\n' + targetUser.avatar_url)
            else:
                await self.bot.say('Y-You are naked. >///<\nhttp://i.imgur.com/CXXJV2s.png')
        else:
            if targetUser.avatar_url:
                await self.bot.say(targetUser.mention + '\'s avatar:\n' + targetUser.avatar_url)
            else:
                await self.bot.say(targetUser.mention + ' is n-naked. >///<\nhttp://i.imgur.com/CXXJV2s.png')

    @commands.command()
    async def joined(self, member : discord.Member):
        """"""
        await self.bot.say('{0.mention} has joined the server! **#MAHVELLIVES**'.format(member))



    @commands.command(pass_context=True)
    async def roll(self, ctx, sides : str, rolls : str):
        """Rolls a user-specified sided dice for a user-specified amount of rolls and returns the sum of all the rolls and each individual roll."""
        try:
            rolls = int(rolls)
            sides = int(sides)
        except Exception:
                await self.bot.say('````\nInput must be valid integers.\n```'.format(command_prefix=self.bot.command_prefix))
                return
        if (sides > 1000000) or (rolls > 1000):
            await self.bot.say('```\nThat number is too big for me. >///<\n```')
        else:
            diceRolls = [random.randint(1, sides) for r in range(rolls)]
            dicemsg = ctx.message.author.mention + ' a rolled {}-sided dice {} times for a total of {}. \nRollss: {}'.format(sides, rolls, sum(diceRolls), str(diceRolls).strip('[]'))
            if (len(dicemsg) >= 1999):
                await self.bot.say('```\nThat number is too big for me. >///<\n```')
            else:
                await self.bot.say(dicemsg)

    @commands.command(pass_context=True, hidden=True)
    async def reboot(self,ctx):
        """Reload the Commands module."""
        if ctx.message.author.id == self.bot.config.owner_id:
                print('loading commands')
                self.bot.unload_extension('ammybot.command')
                print('successfully unloaded commands')
                print('loading commands')
                self.bot.load_extension('ammybot.command')
                print('successfully loaded commands\n')
                return

def setup(bot):
    bot.add_cog(Commands(bot))



