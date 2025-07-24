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

    # create a coroutine object
    coro = custom_coroutine()
    # coro.__await__() # awaitabe - means that it implements '__await__'
    print(coro)  # <coroutine object custom_coroutine at ...>
    # coro.send(None)  # Start the coroutine
    # coro.close()  # Close the coroutine
    # asyncio.run(coro)

    # Run the custom routine
    asyncio.run(custom_coroutine())
