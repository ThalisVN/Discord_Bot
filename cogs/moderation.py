import discord
from discord.ext import commands
import config

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        """Verifica se o usuário tem algum dos cargos de admin"""
        if not any(role.name in config.ADMIN_ROLES for role in ctx.author.roles):
            await ctx.send("🚫 Você não tem permissão para usar este comando!")
            return False
        return True

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Expulsa um membro do servidor"""
        await member.kick(reason=reason)
        embed = discord.Embed(
            title="✅ Usuário expulso",
            description=f"{member.mention} foi expulso por {ctx.author.mention}",
            color=discord.Color.red()
        )
        if reason:
            embed.add_field(name="Motivo", value=reason, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bane um membro do servidor"""
        await member.ban(reason=reason)
        embed = discord.Embed(
            title="🔨 Usuário banido",
            description=f"{member.mention} foi banido por {ctx.author.mention}",
            color=discord.Color.dark_red()
        )
        if reason:
            embed.add_field(name="Motivo", value=reason, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def unban(self, ctx, *, member):
        """Desbane um usuário"""
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                embed = discord.Embed(
                    title="✅ Usuário desbanido",
                    description=f"{user.mention} foi desbanido por {ctx.author.mention}",
                    color=discord.Color.green()
                )
                await ctx.send(embed=embed)
                return
        await ctx.send(f"❌ Usuário {member} não encontrado na lista de banidos")

    @commands.command()
    async def clear(self, ctx, amount: int = 5):
        """Limpa mensagens (padrão: 5)"""
        if amount > 100:
            await ctx.send("❌ Você não pode limpar mais de 100 mensagens de uma vez!")
            return
            
        await ctx.channel.purge(limit=amount + 1)  # +1 para incluir o comando
        embed = discord.Embed(
            description=f"🗑️ {amount} mensagens foram deletadas por {ctx.author.mention}",
            color=discord.Color.blue()
        )
        msg = await ctx.send(embed=embed)
        await msg.delete(delay=5)  # Apaga a mensagem após 5 segundos

async def setup(bot):
    await bot.add_cog(Moderation(bot))