def powerof(N):
    def coreact(x):
        return x**N
    return coreact
print ("raise to power 2")
f = powerof(2) #f is label, point to binary, raise to power of 2
print (f(3))
print (f(4))

print ("raise to power 3")
g = powerof(3)
print (g(2))
print (g(3))
