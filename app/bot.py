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

    async def on_message(self, message):
        # Called when we receive a message.
        if not self.user == message.author:
            logger.log('Received a message!', 'DEBUG')
            text = message.content

            if text.startswith('$info'):
                # They asked for information about the bot.
                information = discord.Embed(
                        title="Created by the TorSpider Team",
                        url='https://github.com/TorSpider/',
                        description="A Discord Interface for TorSpider",
                        colour=0x00AA00
                )
                information.set_author(
                        name='SpiderBot',
                        url='https://github.com/TorSpider/SpiderBot',
                        icon_url='https://i.imgur.com/lP3FmYH.png'
                )
                information.add_field(
                        name="Commands",
                        value=open('app/text/commands.md','r').read()
                )
                await message.channel.send(
                        content="Let me tell you a little about myself...",
                        embed=information
                )

            if text.startswith('$boturl'):
                # They asked for the URL of the bot, to add it to their server.
                await message.channel.send(
                        content=open('app/text/boturl.md','r').read()
                )

        else:
            logger.log('Received a message from myself.', 'DEBUG')

    # Continue to fill in as necessary.
