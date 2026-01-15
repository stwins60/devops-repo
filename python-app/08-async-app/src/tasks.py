import asyncio

async def task_a():
    """Simulated task A"""
    print("Task A starting...")
    await asyncio.sleep(2)
    print("Task A completed!")
    return "Result A"

async def task_b():
    """Simulated task B"""
    print("Task B starting...")
    await asyncio.sleep(1)
    print("Task B completed!")
    return "Result B"

async def task_c():
    """Simulated task C"""
    print("Task C starting...")
    await asyncio.sleep(3)
    print("Task C completed!")
    return "Result C"

async def run_concurrent_tasks():
    """Run multiple tasks concurrently"""
    print("\nRunning concurrent tasks...")
    results = await asyncio.gather(task_a(), task_b(), task_c())
    print(f"All tasks completed: {results}")
    return results
