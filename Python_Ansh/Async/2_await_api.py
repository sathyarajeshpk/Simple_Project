# import time

# def api_call():
#     time.sleep(2)  # Simulate a delay in API call
#     return "API call completed"

# def execute():
#     print("Executing API call...")
#     result = api_call()
#     print(result)

# execute()

import asyncio
import time

async def api_call():
    await asyncio.sleep(5)  # Simulate a delay in API call
    return "API call completed"

async def execute():
    print("Executing API call...")
    result = await api_call()
    print(result)

asyncio.run(execute())