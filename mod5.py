age = 15
interest1 = "football"
interest2 = "python"
#150 data points

if age> 18 and interest1 == "football":
    def showvideos():
        print ("show mature content")
        print ("show football")
        print ("show sports")
elif age<18 and interest1 =="cooking":
    def showvideos():
        print ("no mature")
        print ("show recipes")
else:
    def showvideos():
        print ("show default videos")

showvideos()

def noreturn():
    print ("returns nothing")
    print ("void function")
                    
def times(x,y):
    return x*y

number = times(3,4)
print (number)

fraction = times(3.14,4)
print (fraction)

string = times("lol",3)
print (string)
