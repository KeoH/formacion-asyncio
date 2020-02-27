import asyncio

loop = asyncio.get_event_loop()

async def my_coroutine(text, time_to_wait):
    await asyncio.sleep(time_to_wait)
    print(f"My coroutine! -> {text}")
    return text

gather = asyncio.gather(
    my_coroutine("Hola", 0.5),
    my_coroutine("Mundo", 0.9),
    my_coroutine("Q ase?", 0.5)
)

loop.run_until_complete(gather)
print(gather.result())