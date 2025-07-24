import asyncio


# custom routine function
def custom_routine():
    print('Routine task')


# define a coroutine function
async def custom_coroutine():
    await asyncio.sleep(1)
    message = "Custom Coroutine Result"
    print(message)
    return message


if __name__ == "__main__":
    custom_routine()
    # Run the custom routine
    # coro = custom_coroutine()
    # asyncio.run(coro)
    asyncio.run(custom_coroutine())
