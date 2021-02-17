from threading import Semaphore, BoundedSemaphore

sema = Semaphore(value=3)

print("Init value: ", sema._value)
sema.release()
print("Modified 1: ", sema._value)
sema.acquire()
print("Modified 2: ", sema._value)
