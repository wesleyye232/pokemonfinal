
while True:
    reply = input("Enter some text: ")
    if reply == 'stop':
        break
    try:
        num = int(reply)
    except:
            print ("Oops, smth bad happened")
    else:
            print ("Best case scenario")

print ("Bye")


L = [123, 'spam', 1.23]
#L
#L[0]
#L[2]

L + [4,5,6]

a = [66.25,333,333,1,1234.5]
a.count(333)
a.insert(2,-1)
a.append(333)
a.index(333)
a.remove(333)
a.reverse()
a.sort()
a.pop() #takes out last value

tel = {'jack':4098, 'sape':4139}
tel['guido']=4127
tel
tel['jack']
