import asyncio
from aioredlock import Aioredlock


async def basic_lock():
    lock_manager = Aioredlock('localhost', 6379)

    lock = await lock_manager.lock("resource")
    assert lock.valid is True

    await lock_manager.unlock(lock)
    assert lock.valid is False

    await lock_manager.destroy()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(basic_lock())