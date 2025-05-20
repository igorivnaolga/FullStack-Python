import asyncio
from aiofile import async_open


async def main():
    async with async_open("hello.txt", "r") as afp:
        async for line in afp:
            print(line)


if __name__ == "__main__":
    asyncio.run(main())
