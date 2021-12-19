#files

#r - read, error if not exist
#a - append, add at end, create file if not exist
#w - write, create if not exist
#x - create specified file

#t - text
#b - binary

f = open ("demofile.txt")
#same as f = open ("demofile.txt", "rt")

f = open ("demofile.txt", "r")

#print (f.read(5)) #read 5 characters

#print (f.readline(3)) #read 3 lines

#for x in f:
    #print (x)

f = open ("demofile.txt", "a")
f.write ("Now file has one more line")

import os

if os.path.exists("demofile.txt"):
        os.remove("demofile.txt")
else:
    print ("The file does not exist")

