import threading
def method1():
    print("Hai this is method1 ")

def method2():
    print("Hello this is  method2")

def all_threads():

    first_thread=threading.Thread(target=method1)
    second_thread = threading.Thread(target=method2)

    first_thread.start()
    second_thread.start()

    first_thread.join()
    second_thread.join()


all_threads()