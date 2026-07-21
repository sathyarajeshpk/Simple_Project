import asyncio

async def api_call(url:str):
    print("Fetching data from: ", url)
    await asyncio.sleep(3)
    return f"{url} data"

async def execute():
    result = await api_call("orders")
    print("Data Fetched", result)

asyncio.run(execute())