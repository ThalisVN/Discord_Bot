import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import config
from cogs.basic import ComandosBasicos
from cogs.moderation import Moderation
from cogs.roles import RoleCommands

load_dotenv()  # Carrega o .env

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=config.PREFIX,
            intents=intents,
            case_insensitive=True
        )

    async def setup_hook(self):
        await self.add_cog(ComandosBasicos(self))
        await self.add_cog(Moderation(self))
        await self.add_cog(RoleCommands(self))

bot = MyBot()

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user.name}')

bot.run(os.getenv("DISCORD_TOKEN"))