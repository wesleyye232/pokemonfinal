x = input("Choose number for x: ")
y = input("Choose number for y: ")

if x>y:
    print ("x greater y")
    print ("print this too")
    print ("still inside the if block")

print ("this is not part of if")

print ("Make this part of it, wont work tho")


while True:
        reply = input("Enter text: ")
        if reply == 'stop':
            break
        print (reply.upper())

#S = input("enter 123: ")
#T = input("enter xxx: ")
#print ("Type: S.isdigit(), T.isdigit() ")
#(True,False)

while True:
    reply =input("Enter some text: ")
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 8)
    else:
        print(int(reply) ** 2)
print('Bye')
