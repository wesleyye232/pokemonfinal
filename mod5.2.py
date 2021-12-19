temp = 105
def func1():
    global temp
    if temp > 102:
        print ("ALARM")
        print ("START COOLER")
        temp = 99
func1()
print (temp)
