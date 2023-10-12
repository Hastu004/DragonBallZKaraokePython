#!/usr/bin/env python3

import asyncio
import string


async def print_num():
    for x in range(0, 10):
        print('Number: {}'.format(x))
        await asyncio.sleep(1)

    print('print_num is finished!')

async def print_alp():
    my_list = string.ascii_uppercase

    for x in my_list:
        print('Letter: {}'.format(x))
        await asyncio.sleep(1)

    print('print_alp is finished!')


async def msg(my_msg):
    print(my_msg)
    await asyncio.sleep(1)


async def main():
    await msg('Hello World!')
    await print_alp()
    await msg('Hello Again!')
    await print_num()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
