import threading

print("Start Code")

def fun():
    print("in fun")

print(threading.current_thread().name)      # MainThread

fun()