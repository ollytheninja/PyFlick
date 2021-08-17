import asyncio
import os

from aiohttp import ClientSession
from dotenv import load_dotenv

from pyflick import FlickAPI
from pyflick.authentication import SimpleFlickAuth

load_dotenv()  # take environment variables from .env.

USERNAME = os.getenv("FLICK_USERNAME")
PASSWORD = os.getenv("FLICK_PASSWORD")


async def get_flick_pricing():
    async with ClientSession() as session:
        auth = SimpleFlickAuth(USERNAME, PASSWORD, session)

        api = FlickAPI(auth)

        return await api.get_pricing()


def main():
    price = asyncio.run(get_flick_pricing())
    print(f"Current price ${price.price / 100}")

    # You can get all components of the price by inspecting the price object


if __name__ == "__main__":
    main()
