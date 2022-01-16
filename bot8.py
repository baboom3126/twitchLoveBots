from twitchio.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

class BotChild(commands.Bot):

    def __init__(self):
        super().__init__(token='oauth:7lgfebbr0w7d30iuc65l6k2tdtt8db', prefix='??', initial_channels=[os.getenv('CHANNEL')])

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