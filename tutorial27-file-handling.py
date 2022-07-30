"""
File Handling
"""
f = open("testfile.txt", "r")
#print(f.read())
#print(f.read(15))
#print(f.readline())
#print(f.readline())
"""
data = f.readlines()
for l in data:
    print(l)

f.close()
"""
"""with open("testfile.txt", "r") as f:
    data = f.readlines()
    for l in data:
        print(l)
"""
"""
w = open("testfile2.txt", "a")
w.write("new data This is testfile2 data 10\n")
w.write("new data  This is testfile2 data 20\n")
w.close() 
"""
import os
os.remove('testfile2.txt') 