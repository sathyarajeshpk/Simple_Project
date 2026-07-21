import asyncio

async def api_call(url:str, delay:int=3):
    print("Fetching data from: ", url)
    await asyncio.sleep(delay)
    print("Data fetched from ", url)
    return f"{url} data"

async def execute():
    await asyncio.sleep(1)
    print("Data Executed")

async def transform():
    await asyncio.sleep(10)
    print("Data Transformed")

# asyncio.run(execute())

async def main():
    tasks = await asyncio.gather(
        api_call("URL1"),
        execute(),
        transform(),
    )

    print("Completed")

asyncio.run(main())