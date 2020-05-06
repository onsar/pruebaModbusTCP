import sched, time, threading

n=0
m=0
def hello():
    global n
    print ("hello, world: " + str(n))
    n=n+1
    threading.Timer(0.01, hello).start()
    list= threading.enumerate()
    print(list)
    number = threading.active_count()
    print(number)
def hello2():
    global n
    print ("hello, world: " + str(m))
    m=m+1
    threading.Timer(0.02, hello2).start()
    number= threading.enumerate()
    print(number)
    number = threading.active_count()
    print(number)

def hello3():
    global n
    print ("hello, world: " + str(n))
    n=n+1
    threading.Timer(0.01, hello3).start()
    list= threading.enumerate()
    print(list)
    number = threading.active_count()
    print(number)
def hello4():
    global n
    print ("hello, world: " + str(m))
    m=m+1
    threading.Timer(0.02, hello4).start()
    number= threading.enumerate()
    print(number)
    number = threading.active_count()
    print(number)

def hello5():
    global n
    print ("hello, world: " + str(n))
    n=n+1
    threading.Timer(0.01, hello5).start()
    list= threading.enumerate()
    print(list)
    number = threading.active_count()
    print(number)
def hello6():
    global n
    print ("hello, world: " + str(m))
    m=m+1
    threading.Timer(0.02, hello6).start()
    number= threading.enumerate()
    print(number)
    number = threading.active_count()
    print(number)
def hello7():
    global n
    print ("hello, world: " + str(n))
    n=n+1
    threading.Timer(0.01, hello7).start()
    list= threading.enumerate()
    print(list)
    number = threading.active_count()
    print(number)
def hello8():
    global n
    print ("hello, world: " + str(m))
    n=n+1
    threading.Timer(0.02, hello8).start()
    number= threading.enumerate()
    print(number)
    number = threading.active_count()
    print(number)
'''
t = Timer(30.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed
'''
print ("hello, world -1")
print(threading.active_count())
hello()
hello2()
hello3()
hello4()
hello5()
hello6()
hello7()
hello8()
print ("hello, world -2")
print(threading.active_count())
