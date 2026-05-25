import discord
import requests
import asyncio
from datetime import datetime

class VanityManager:
    def __init__(self, config):
        self.config = config
        self.current_vanity = None
        self.protected = False

    async def load_current_vanity(self):
        """Récupère le vanity actuel du serveur."""
        guild = bot.get_guild(self.config["protected_server_id"])
        if guild:
            for member in guild.members:
                if member.nick and member.nick.startswith(self.config["vanity_prefix"]):
                    self.current_vanity = member.nick
                    self.protected = True
                    break

    async def check_vanity_change(self, before, after):
        """Vérifie si un changement de vanity est détecté."""
        if not self.protected:
            return

        if before.nick != after.nick:
            await self.handle_vanity_steal(before, after)

    async def handle_vanity_steal(self, before, after):
        """Gère la tentative de vol de vanity."""
        logger.log_steal_attempt(after, self.current_vanity)

        # Tentative de récupération
        success = await self.recover_vanity()

        if success:
            logger.log_successful_recovery(after, self.current_vanity)
        else:
            logger.log_failed_recovery(after, self.current_vanity)

    async def recover_vanity(self):
        """Récupère le vanity en utilisant l'API Discord."""
        guild = bot.get_guild(self.config["protected_server_id"])
        if not guild:
            return False

        # Récupérer l'utilisateur admin
        admin = guild.get_member(self.config["admin_id"])
        if not admin:
            return False

        # Récupérer le membre actuel avec le vanity
        for member in guild.members:
            if member.nick == self.current_vanity:
                # Ban le voleur
                await member.ban(reason="Vol de vanity détecté")
                # Réattribuer le vanity à l'admin
                await admin.edit(nick=self.current_vanity)
                return True

        return False
