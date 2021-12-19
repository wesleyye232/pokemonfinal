#x>y
#x<y
#x==y
#x<=y
#x>=y
#and
#or

x = -1

if x > 1:
    print ("x is positive")
else:
    print ("x is negative")


age = 18
height = 60
#purchase tickets, above 16yrs at least 30in tall

if age >= 16 and height >= 30:
    print ("you can purchase a ticket")
else:
    print ("you cannot purchase a ticket")

homework = int(input("Enter hw score:" ))
midterm = int(input("Cumulative midterm score:" ))
project = int(input("Enter Project score:" ))

finalscore = 0.3*homework + 0.4*midterm + 0.3*project

print ("final score: ", finalscore)

#if FS >= 90, A
#if FS >= 80 and <90, B

if finalscore >= 90:
    print ("A")
elif finalscore >= 80 and finalscore < 90:
    print ("B")
elif finalscore >= 70 and finalscore <80:
    print ("C")
else:
    print ("D :C")


    
               
