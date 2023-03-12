import data
import internal
import asyncio

# Note: Should convert all instances of \n to \\n internally.

async def main():
    data.init()
    await asyncio.gather(internal.think(), internal.subthink())

asyncio.run(main())
