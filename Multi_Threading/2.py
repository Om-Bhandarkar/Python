import threading,os

print("One")
print("two")
print("three")

print(threading.current_thread().name)  
print(os.getpid())      # Get PVM Process ID 
