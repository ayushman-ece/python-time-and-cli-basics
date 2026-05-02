import time
def usingWhile():
    i = 0
    while i < 50000:
        i = i+1
def usingFor():
    for  i in range (50000):
        print(i)


#For loop
init  = time.time()
usingFor()
t1 = time.time() - init


#While loop
init = time.time()
usingWhile()
print(time.time() - init)
print(t1)