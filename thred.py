import threading


def car():
    for i in range(1, 100):
        print("hellooooo")
    
def bus():
    for i in range(1, 100):
        print("noooooo")
        
# car()

# bus()

th1 = threading.Thread(target = car)
th2 = threading.Thread(target = bus)

th1.start()
th2.start()

print("this is imp code")

print("runningg")

print("going")

th1.join()
th2.join()

print("doneee")


# a = 10
# b = 20

# c = a + b

# d = c + 100

# print(c)