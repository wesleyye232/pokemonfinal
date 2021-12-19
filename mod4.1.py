x = 0

while x < 10:
    print ("X is currently, ", x)
    x = x + 1
print ("Done w/ loop")

y = 7
z = y-1
#figure out of number is prime

while z>1:
    if y % z ==0:
        print (y, "has a factor", z)
        break #break will jump out of loop
    z = z-1
else:
    print (y, "is a prime number")

#continue :continue with loop
#pass :do nothing, pauses
