import asyncio

loop = asyncio.get_event_loop()

async def my_coroutine(text, time_to_wait):
    await asyncio.sleep(time_to_wait)
    print(f"My coroutine! -> {text}")

loop.run_until_complete(my_coroutine("Hola Mundo", 0.5))
