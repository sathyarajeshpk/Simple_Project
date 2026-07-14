import asyncio
import time

async def main():
    print("Starting async operations...")
    await asyncio.sleep(10)
    print("Async operation completed.")

asyncio.run(main())