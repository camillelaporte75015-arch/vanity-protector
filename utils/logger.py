import discord
from datetime import datetime

class Logger:
    def __init__(self, config):
        self.config = config

    async def log_steal_attempt(self, user, vanity):
        """Log une tentative de vol de vanity."""
        channel = bot.get_channel(self.config["logs_channel_id"])
        if channel:
            embed = discord.Embed(
                title="DÉTECTION DE VOL DE VANITY 🚨",
                description=f"**Utilisateur** : {user.mention} / `{user.id}` a tenté de changer le vanity de ce serveur.",
                color=discord.Color.red()
            )
            embed.add_field(name="Heure", value=datetime.now().strftime("%H:%M:%S"))
            embed.add_field(name="Date", value=datetime.now().strftime("%d/%m/%Y"))
            await channel.send(embed=embed)

    async def log_successful_recovery(self, user, vanity):
        """Log une récupération réussie."""
        channel = bot.get_channel(self.config["logs_channel_id"])
        if channel:
            embed = discord.Embed(
                title="RÉCUPÉRATION RÉUSSIE 🎉",
                description=f"**Utilisateur** : {user.mention} a été banni et le vanity `{vanity}` a été récupéré.",
                color=discord.Color.green()
            )
            embed.add_field(name="Heure", value=datetime.now().strftime("%H:%M:%S"))
            embed.add_field(name="Date", value=datetime.now().strftime("%d/%m/%Y"))
            await channel.send(embed=embed)

    async def log_failed_recovery(self, user, vanity):
        """Log une récupération échouée."""
        channel = bot.get_channel(self.config["logs_channel_id"])
        if channel:
            embed = discord.Embed(
                title="RÉCUPÉRATION ÉCHOUÉE ❌",
                description=f"**Utilisateur** : {user.mention} a été banni mais le vanity `{vanity}` n'a pas pu être récupéré.",
                color=discord.Color.red()
            )
            embed.add_field(name="Heure", value=datetime.now().strftime("%H:%M:%S"))
            embed.add_field(name="Date", value=datetime.now().strftime("%d/%m/%Y"))
            await channel.send(embed=embed)
