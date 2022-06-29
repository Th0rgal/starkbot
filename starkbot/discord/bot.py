import discord
from discord import app_commands
from discord.ext import commands

description = "A discord bot to interact with StarkNet"
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="?", description=description, intents=intents)


async def setup() -> None:
    await bot.add_cog(MyCog(bot))


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")


@bot.command()
async def refresh(ctx):
    """Refresh commands tree"""
    await bot.tree.sync(guild=MY_GUILD_ID)
    await ctx.send("Commands tree refreshed!")


MY_GUILD_ID = discord.Object(991644956198457424)


class MyCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="connect")
    @app_commands.guilds(MY_GUILD_ID)
    async def my_command(self, interaction: discord.Interaction) -> None:
        """Connect your StarkNet account"""
        await interaction.response.send_message("Hello from command 1!", ephemeral=True)
