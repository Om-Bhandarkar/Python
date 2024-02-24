import threading
class MyThread(Thread):
    def run(self):
        print("In run Method")
        print(threading.current_thread().getName())

print(threading.current_thread().getName())
t = MyThread(10,20)
t.start()