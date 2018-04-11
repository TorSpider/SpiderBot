#!/usr/bin/env python3

''' SpiderBot.py
    A Discord Interface for TorSpider
'''

import os
import sys
import discord
import configparser
from app.bot import SpiderBot
from app.logging import logger


#---[ INITIALIZATION ]---#


bot = SpiderBot()


#---[ FUNCTIONS ]---#


def main():
    if not os.path.exists('bot.cfg'):
        default_config = configparser.RawConfigParser()
        default_config.optionxform = lambda option: option
        default_config['SpiderBot'] = {
            'Token': 'BOT_TOKEN_GOES_HERE',
        }
        default_config['LOGGING'] = {
            'LogToConsole': 'True',
            'loglevel': 'INFO'
        }
        with open('bot.cfg', 'w') as config_file:
            default_config.write(config_file)
        print('Default configuration stored in bot.cfg.')
        print('Please edit bot.cfg before running SpiderBot again.')
        sys.exit(0)

    logger.log('Initializing...', 'INFO')

    # Load the configuration file.
    try:
        config = configparser.ConfigParser()
        config.read('bot.cfg')
        bot_token = config['SpiderBot'].get('Token')
    except Exception as e:
        print('Could not parse bot.cfg. Please verify its syntax.')
        sys.exit(0)

    # Config loaded. Start the bot.
    logger.log('SpiderBot Initialized. Connecting to Discord...', 'INFO')
    try:
        bot.run(bot_token)
    except discord.LoginFailure:
        logger.log('Exception: Login Failure. Check bot token in bot.cfg.',
                   'CRITICAL')
        sys.exit(0)
    except Exception as e:
        logger.log('Exception: {}'.format(e), 'CRITICAL')
        raise
        sys.exit(0)

    # When we reach this point, the bot has shut down.
    logger.log('SpiderBot disconnected.', 'INFO')


#---[ MAIN ]---#


if __name__ == '__main__':
    main()
