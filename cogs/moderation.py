import nextcord
from nextcord.ext import commands
from nextcord import Interaction, SlashOption
from nextcord.ext.commands import has_permissions

class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @nextcord.slash_command(name="ban", description="Ban a user from the server")
    @has_permissions(ban_members=True)
    async def ban(self, interaction: Interaction,
                  member: nextcord.Member = SlashOption(description="Member to ban"),
                  reason: str = SlashOption(description="Reason for banning")):
        await member.ban(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been banned for: {reason}")

    @nextcord.slash_command(name="kick", description="Kick a user from the server")
    @has_permissions(kick_members=True)
    async def kick(self, interaction: Interaction,
                   member: nextcord.Member = SlashOption(description="Member to kick"),
                   reason: str = SlashOption(description="Reason for kicking")):
        await member.kick(reason=reason)
        await interaction.response.send_message(f"{member.mention} has been kicked for: {reason}")

def setup(bot):
    bot.add_cog(Moderation(bot))
