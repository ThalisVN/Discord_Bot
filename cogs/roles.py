import discord
from discord.ext import commands
import config

class RoleCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def visitante(self, ctx):
        """Adiciona o cargo de Visitante"""
        await self._assign_role(ctx, "visitante")

    @commands.command()
    async def cc(self, ctx):
        """Adiciona o cargo de CC"""
        await self._assign_role(ctx, "cc")

    @commands.command()
    async def ads(self, ctx):
        """Adiciona o cargo de ADS"""
        await self._assign_role(ctx, "ads")

    @commands.command()
    async def si(self, ctx):
        """Adiciona o cargo de SI"""
        await self._assign_role(ctx, "si")

    async def _assign_role(self, ctx, role_key):
        role_name = config.SELF_ROLES.get(role_key)
        if not role_name:
            await ctx.send("❌ Este cargo não está disponível para auto-atribuição!")
            return

        role = discord.utils.get(ctx.guild.roles, name=role_name)
        if not role:
            await ctx.send(f"❌ O cargo {role_name} não foi encontrado no servidor!")
            return

        try:
            if role in ctx.author.roles:
                await ctx.author.remove_roles(role)
                await ctx.send(f"✅ Cargo {role_name} removido com sucesso!")
            else:
                await ctx.author.add_roles(role)
                await ctx.send(f"✅ Cargo {role_name} adicionado com sucesso!")
        except discord.Forbidden:
            await ctx.send("❌ Não tenho permissão para gerenciar cargos!")
        except Exception as e:
            await ctx.send(f"❌ Ocorreu um erro: {str(e)}")

async def setup(bot):
    await bot.add_cog(RoleCommands(bot))