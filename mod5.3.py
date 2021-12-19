x = 99

def f1():
    x=88
    def f2():
        print (x)
    f2()

f1()

def displayitemclick():
    print ("display item, photo, price")
    def sponsored():
        print ("ads")
    def alsoview():
        print ("correlate to other item")
    return sponsored

bottomblock = displayitemclick()
bottomblock()
