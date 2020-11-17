#!/usr/bin/python3
import discord
from discord.ext import commands

class CommandHandler(commands.Cog):
    def __init__(self, client):
        self.client = client