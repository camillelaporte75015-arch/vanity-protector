from discord.ext import commands

class CommandHandler:
    def __init__(self, config, vanity_manager, logger):
        self.config = config
        self.vanity_manager = vanity_manager
        self.logger = logger

    @commands.command(name="lockvanity")
    async def lock_vanity(self, ctx):
        """Active la protection du vanity."""
        if ctx.author.id != self.config["admin_id"]:
            await ctx.send("❌ **Accès refusé.**")
            return

        self.vanity_manager.protected = True
        await self.vanity_manager.load_current_vanity()
        await ctx.send(f"✅ **Le vanity {self.vanity_manager.current_vanity} est maintenant protégé.**")

    @commands.command(name="unlockvanity")
    async def unlock_vanity(self, ctx):
        """Désactive la protection du vanity."""
        if ctx.author.id != self.config["admin_id"]:
            await ctx.send("❌ **Accès refusé.**")
            return

        self.vanity_manager.protected = False
        await ctx.send(f"✅ **Le vanity n'est plus protégé.**")
