x = 1
def test():
    x = 2
test()
print(x) #1


x = 1
def test1():
    global x
    x = 2
test1()
print(x) #2


x = [1]
def test2():
    x = [2]
test2()
print(x) #1


x = [1]
def test3():
    global x
    x = [2]
test3()
print(x) #2


x = [1]
def test4():
    x[0] = 2
test4()
print(x) #2