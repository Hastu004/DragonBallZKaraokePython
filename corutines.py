import asyncio

async def child():
    i = 5
    while i > 0:
        print("Hi, I'm the child coroutine, la la la la la")
        await asyncio.sleep(1)
        i -= 1

async def parent():
    print("Hi, I'm the parent coroutine awaiting the child coroutine")
    await child() # this blocks inside the parent coroutine, but not the neighbour
    print("Hi, I'm the parent, the child coroutine is now done and I can stop waiting")

async def neighbour():
    i = 5
    while i > 0:
        await asyncio.sleep(1)
        print("Hi, I'm your neighbour!")
        i -= 1

async def my_app():
    # start the neighbour and parent coroutines and let them coexist in Task wrappers
    await asyncio.wait([neighbour(), parent()])

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(my_app())
