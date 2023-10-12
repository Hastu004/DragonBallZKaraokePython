import asyncio
import time

async def some_coro(delay,text):
    await asyncio.sleep(delay)
    print(f"{text} at {time.strftime('%X')}")
async def another_coro(delay,text):
    await asyncio.sleep(delay)
    print(f"{text} at {time.strftime('%X')}")
async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(some_coro(1,"some"))
        task2 = tg.create_task(another_coro(1,"another"))
    print(f"Both tasks have completed now: {task1.result()}, {task2.result()}")

asyncio.run(main())
