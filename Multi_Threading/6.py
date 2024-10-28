import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(second):
    print(f"Sleeping for {second} seconds")
    time.sleep(second)
    return f"{second}sec"

def main():
    time1 = time.perf_counter()

    t1 = threading.Thread(target=func, args=[4])
    t2 = threading.Thread(target=func, args=[2])
    t3 = threading.Thread(target=func, args=[1])
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()
    time2 = time.perf_counter()
    print(time1 - time2)

