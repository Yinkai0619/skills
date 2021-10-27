import threading
import multiprocessing
import time
import asyncio

# @asyncio.coroutine
# def a():
async def a():
    for x in range(3):
        # time.sleep(0.1)
        print(x)
        # yield from asyncio.sleep(0.001)
        await asyncio.sleep(0.01)
    return 1000

@asyncio.coroutine
def b():
# async def b():
    for x in "abc":
        # time.sleep(0.1)
        print(x)
        yield from asyncio.sleep(0.001)
        # await asyncio.sleep(0.01)
    return 2000


def cb(future):
    print(3, type(future), "||||",future, "----------------------")
    print(4, future.result())

# threading.Thread(target=a, name="a").start()
# threading.Thread(target=b, name="b").start()

if __name__ == "__main__":
    # multiprocessing.Process(target=a, name="a").start()
    # multiprocessing.Process(target=b, name="b").start()

    # x = a()
    # y = b()
    # for i in range(3):
    #     next(x)
    #     next(y)

    loop = asyncio.get_event_loop()
    # loop.run_until_complete(a())
    task = loop.create_task(a())
    # print(type(task),"~~~~~~~~~~~~~~~~~~~~~~")
    # print(task)
    task.add_done_callback(cb)
    # print(1, task)
    tasks = [task, b()]
    ret = loop.run_until_complete(asyncio.wait(tasks))
    # print(2, task, task.result())
    loop.close()

    # print(10, type(ret),"|||||||||",ret)
    # print(11, ret)

    # for s in ret:
    #     for t in s:
    #         print(t, "!!!!!!!!!!", type(t))
    #         print(t.result(), "~~~~~~~~~")

    print(asyncio.iscoroutinefunction(a))
    print(asyncio.iscoroutinefunction(b))