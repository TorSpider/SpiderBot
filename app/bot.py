import discord
from app.logging import logger

class SpiderBot(discord.Client):
    # This is the main interface with Discord.

    def __init__(self):
        discord.Client.__init__(self, fetch_offline_members=True)

    async def on_ready(self):
        activity = discord.Activity(
                # Set the activity to "Watching my children roam..."
                name="my children roam...",
                type=discord.ActivityType.watching)
        await self.change_presence(
                status=discord.Status.online,
                activity=activity)
        logger.log('Connected to {} guilds, with {} known users.'.format(
                len(self.guilds), len(self.users)), 'INFO')

    async def on_connect(self):
        logger.log('Logged in as {} ({}).'.format(
                self.user.name, self.user.id), 'INFO')

    # Continue to fill in as necessary.
