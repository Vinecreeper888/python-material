"""
#1. write a program which can compute the fact of given number using function
#using recursion, separated val in console
#n = int(input("Enter a number:"))

n = int(input("Enter a number:"))

def computeFact(n):
	fact = 1
	for i in range(1,n+1):
		fact = fact * i
	print(fact)

computeFact(n)
"""


"""
#2. With a given int "n", write a program to generate the output in the following format:
#if val = 8, then output: 1:1,2:4,3:9....8:64
n = int(input("Enter a number:"))

for i in range(1,n+1):
	print(str(i)+":"+str((i*i)))
"""

"""
#3. Write a program that calculates and prints the value according to the given
#formula: q = sqrt(2*c*d)/h
import math
c = int(input("Enter value of c:"))
d = int(input("Enter value of d:"))
h = int(input("Enter height:"))
q = math.sqrt(2*c*d)/h
print(q)
"""

"""
#4. Write a program with a sequence of comma separated 4 digit binary number
#as input and check whether they are is divisible by 5

a = [x for x in input().split(',')]
"""
#meaning of the list generator statement
#a = input().split(',')
#for i in a:
	#a[i] = int(a[i])
"""

for i in a:
	x = int(i,2)
	if x%5 == 0:
		print(i+" is divisible by 5")
"""



#5. Write a program which will find all numbers between 1000 and 3000 such that each
#digit is even (list)
res = []
for i in range(1000,3001):
	for j in str(i):
		#print(j)
		if int(j)%2 == 0:
			res.append(i)
		else:
			break
print(res)

"""
#6. Accept a sentence eg: "Hello World!! 123",calculate number of letters and digits
#in that sentence

import collections
n = "Hello World!! 123"
print(collections.Counter(n))

"""


"""
#7. Write a program to read the sentence "Hello World" and count the number of upper case
#and lower case letters
n = "Hello World"
count = 0
lcount = 0
for i in n:
	if ord(i) >= 65 and ord(i) < 91:
		count = count + 1		
	else:
		lcount = lcount + 1

print("Number of Uppercase letters: "+str(count))
print("Number of Lowercase letters: "+str(lcount))
"""

#8. 

"""
#9. Net amount of a bank account based on a trans log from the console i/p
#the trans log D 100 W 200. Suppose the following inputis applied to the 
#program D 300, D 300, w 200, D 400,net=500
disp = input("Enter deposit amount:")

try:
		dep = disp.split()
		if dep[0] == "d" or dep[0] == "D":
			print("Net:"+dep[1])
		else:
			print("Please deposit first.")

		disp1 = input("D for deposit and W for withdrawl:")
	#while disp1 == "D" or disp1 == "W":
		t = disp1.split()
		if t[0] == "D":
			if dep[0] == "d" or dep[0] == "D":
				sum = int(t[1])+int(dep[1])
				print("Net: "+str(sum))
			else:
				print("Net:"+t[1])
		elif t[0] == "W":
			w = disp1.split()
			sum1 = int(dep[1]) - int(w[1])
			print("Net:"+str(sum1))
except:
		print("Enter the right details.")
"""

 	





