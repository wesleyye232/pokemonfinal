def func(x,y,z):
    return x+y+z

l = lambda x=10,y=20,z=30:x+y+z

print ("call with no arguments - default used")
print (l())
print ("give three arguments")
print (l(5,6,7,))
print ("give part of arugment")
print (l(1,2))

def myfunc(n):
    return lambda a:a*n

times2 = myfunc(2)
times3 = myfunc(3)
times4 = myfunc(4)
#created 3 new functions using myfunc as template

print (times2(50))
print (times3(50))

def knights():
    title = 'sir'
    action = (lambda x: title + ' ' + x)
    return action
act = knights()
print (act("David"))

# x ^ y

powers = [lambda x: x **2, lambda x: x **3, lambda x: x**4]

for func in powers:
    print (func(3))

print (powers [1](3))
