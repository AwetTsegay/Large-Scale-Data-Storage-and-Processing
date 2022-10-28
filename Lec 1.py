# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 16:53:51 2021

@author: tsega
"""

##### Week 1

f = open('/Users/uxac007/Work/CS5234/demo.txt', 'r')
print(type(f))
print(f.readline())
print(f.read())
f.close()


f = open("demo.txt")
print(type(f))
f.close()

f = open("demo.txt")
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()

f = open("demo.txt")
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line.strip())
f.close()


f = open("demo.txt", 'r')
for line in f:
    print(line.strip())
f.close()

with open("demo.txt") as f:
    for line in f:
        print(line.strip())

## Splitting the text into words
with open('demo.txt', 'r') as f:
    for line in f:
        for w in line.split():
            print(w.strip(',.'))
        

f = open('animals.txt', 'w')
f.read() # Error: file in not readable

f = open('animals.txt', 'w')
f.write('cat')
f.write('dog')
f.write('t-rex')
f.write('sloth')
f.close()

f = open('animals.txt', 'w')
f.write('cat\n')
f.write('dog\n')
f.write('t-rex\n')
f.write('sloth\n')
f.close()

with open('animals.txt', 'w') as f:
    f.write('cat\n')
    f.write('dog\n')
    f.write('t-rex\n')
    f.write('sloth\n')

with open('animals.txt') as f:
    for line in f:
        # suppress new lines when printing instead of line.strip()
        print(line, end = '')   
        
#=================================================================
pwd
cat demo.txt
more demo.txt

f = open('sonnet14-15.txt', 'r')
f.readline()
f.read()


f = open('sonnet14-15.txt', 'r')
for line in f:
    print(line.strip())
f.close()

with open('sonnet14-15.txt') as f:
    for line in f:
        print(line.strip())
        

# Split files into words
with open('sonnet14-15.txt', 'r') as f:
    for line in f:
        for w in line.split():
            print(w.strip(',.'))
            

count = 0
with open('sonnet14-15.txt', 'r') as f:
    for line in f:
        for w in line.split():
            if (w=="I"):
                count = count + 1
print(count)
          
# Writing files
$cat > foo.txt
hello world
goodye
$cat foo.txt

f = open('animals.txt', 'w')
f.write('shark')
f.write('cat')
f.close()
$cat animals.txt

f = open('animals.txt', 'w')
f.write('shark\n')
f.write('cat\n')
f.close()
$cat animals.txt

f = open('animals.txt', 'a')
f.write('dog\n')
f.write('mole\n')
f.close()
$cat animals.txt

with open('animals.txt', 'w') as f:
    f.write('cat\n')
    f.write('dog\n')
    f.write('t-rex\n')
    f.write('sloth\n')

with open('animals.txt') as f:
for line in f:
     print(line, end = '')   
