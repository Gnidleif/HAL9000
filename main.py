#!/usr/bin/python3
import os, discord, sys, json, command_handler
from discord.ext import commands
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

class HAL9000(commands.Bot):
    def __init__(self, config, prefix='!'):
        super().__init__(command_prefix=prefix)
        self.config = config
        self.add_cog(command_handler.CommandHandler(self))

        self.run(config["bot_token"])

def run(*args):
    with open(os.path.join(__location__, "config.json"), 'r', encoding="utf-8") as f:
        config = json.load(f)
    
    bot = HAL9000(config)
    return

if __name__ == "__main__":
    run(sys.argv[1:])