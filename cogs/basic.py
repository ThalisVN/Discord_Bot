import discord
from discord.ext import commands
import config

class ComandosBasicos(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def hello(self, ctx):
        print(f"Ola {ctx.author.name}")
        await ctx.send('Ola')
        
    @commands.command()
    async def ping(self, ctx):
        """Verifica a latência do bot"""
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')

    @commands.command()
    async def info(self, ctx):
        """Informações sobre o bot"""
        await ctx.send('Olá, eu sou a Sara, um bot criado para auxiliar os membros da guild')

    @commands.command()
    async def convite(self, ctx):
        """Envia o link de convite do servidor"""
        await ctx.send('https://discord.gg/sXnn59AM')

    @commands.command()
    async def ajuda(self, ctx):
        """Mostra todos os comandos disponíveis"""
        help_msg = """
        **Comandos disponíveis:**
        !ping - Verifica a latência do bot
        !info - Informações sobre o bot
        !convite - Envia o link de convite do servidor
        
        **Auto-atribuição de cargos:**
        !visitante - Adiciona/remove cargo de Visitante
        !cc - Adiciona/remove cargo de CC
        !ads - Adiciona/remove cargo de ADS
        !si - Adiciona/remove cargo de SI
        
        **Comandos de moderação:**
        !kick - Expulsa um membro (Admin)
        !ban - Bane um membro (Admin)
        !unban - Desbane um usuário (Admin)
        !clear - Limpa mensagens (Admin)
        """
        await ctx.send(help_msg)
    
async def setup(bot):
    await bot.add_cog(ComandosBasicos(bot))