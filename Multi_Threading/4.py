import threading 

def fun(x, y):
    print("In fun Function ")
    print(threading.current_thread().name)
    for i in range(6):
        print("In fun")

def mun(x):
    print("In mun Function ")
    print(threading.current_thread().name)
    for i in range(6):
        print("In mun")

print(threading.current_thread().name)

thread1 = threading.Thread(target=fun, name="First Thread", args=(5, 7))
thread2 = threading.Thread(target=mun, name="Second Thread", args=(8,))  # Note the comma after 8 to make it a single-element tuple

thread1.start()
thread2.start()
