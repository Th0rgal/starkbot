from config import TomlConfig
from discord.bot import bot, setup
import logging
import asyncio


async def main():
    asyncio.create_task(parallel())
    conf = TomlConfig("config.toml", "config.template.toml")
    await setup()
    await bot.start(conf.token)


async def parallel():
    pass


logging.basicConfig(level=logging.INFO)
asyncio.run(main())
