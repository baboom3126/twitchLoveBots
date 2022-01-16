from twitchio.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

class BotLeader(commands.Bot):

    def __init__(self):
        super().__init__(token='oauth:gi98ygl663er2hotme0ztkzzo1jcjv', prefix='??', initial_channels=[os.getenv('CHANNEL')])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    async def event_message(self, message):
        if message.echo:
            return
        else:
            ctx = await self.get_context(message)
            msg = message.content
            identity = message._tags['badges']
            if('moderator' in identity or 'vip' in identity or 'broadcaster' in identity):
                'moderator,vip'
                if(msg[0:3]=='!色狗'):
                    speak = msg.split('狗 ')[1]
                    print(msg)
                    await ctx.send(speak)

    @commands.command()
    async def hello(self, ctx: commands.Context):
        # Send a hello back!
        await ctx.send(f'{ctx.author.name} hello!')




bot1 = BotLeader()
bot1.run()



