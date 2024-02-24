import threading 
def fun():
    print("In fun Function ")
    print(threading.current_thread().name)
    for i in range(6):
        print("In fun")
def mun():
    print("In mun Function ")
    print(threading.current_thread().name)
    for i in range(6):
        print("In mun")

print(threading.current_thread().name)
thread1 = threading.Thread(target=fun, name="First Thread")
thread2 = threading.Thread(target=mun, name="Second Thread")

thread1.start()
thread2.start()