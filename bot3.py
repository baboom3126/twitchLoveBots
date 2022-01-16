from twitchio.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

class BotChild(commands.Bot):

    def __init__(self):
        super().__init__(token='oauth:7ja8zjgdusot5hdfdgpoa9ej9ejw10', prefix='??', initial_channels=[os.getenv('CHANNEL')])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.echo:
            return
        else:
            ctx = await self.get_context(message)
            msg = message.content
            if(message._author.name == 'johndoe__001'):
                await ctx.send(msg)


bot2 = BotChild()
bot2.run()