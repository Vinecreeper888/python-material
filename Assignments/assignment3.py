"""
a = {}
n = "Writing programs or programming is a very creative"
for i in n:
	a[i] = a.get(i,0) + 1
print(a)
"""


"""
#1. Write a program to read through a main log. Build a histogram using dictionary
#to count how many messages have come from each email address. 
res = []
a = {}
n = input("Enter filename:")
fhand = open(n)
for line in fhand:
	#line = line.split()
	#line = line.lstrip()
	at = line.find('@')
	if line.startswith('From:'):
		res.append(line[5:at])
for i in res:
	if i in a:
		a[i] = a[i] + 1
	else:
		a[i] = 1
print(a)
"""


"""
#2. Write a program that categories each mail whose message is in the following format: 
#(From:abc@gmail.com Saturday Jan 5 9:14:06 2018) which mentions by which day of the week the 
#commit was done. TO do this,look for the lines which start with from, then look
#for the 3rd word and keep a running count of each of the days of the week. At the end
#of the program, print the contents of the dictionary.
res = []
a = {}
days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
n = input("Enter filename:")
try:
	fhand = open(n)
	for line in fhand:
		line = line.rstrip()
		if line.startswith('From'):
			res.append(line)
	for i in res:
		i = i.split()
		for j in i:
			if j in days:
				if j in a:
					a[j] = a[j] + 1
				else:
					a[j] = 1
	print(a)
except:
	print("Enter valid filename.")
"""


"""
#3. Modify the first program to figure out who has the most messages in the file
res = []
a = {}
n = input("Enter filename:")
fhand = open(n)
for line in fhand:
	#line = line.split()
	#line = line.lstrip()
	at = line.find('@')
	res.append(line[5:at])
for i in res:
	if i in a:
		a[i] = a[i] + 1
	else:
		a[i] = 1
print(max(a))
"""


"""
#4. dictionary to tell how many times a letter repeats consecutively in a string
n = input("Enter a string:")
a = {}
#m = int(input("Enter a number:"))
for i in range(0,len(n)):
	if n[i-1] == n[i]:
		if n[i] in a:
			#a[n[i]] = 1
			a[n[i]] = a[n[i]] + 1
		else:
			#n[i] = a[n[i]] + 1
			a[n[i]] = 1
	else:
		if n[i] in a:
			#a[n[i]] = 1
			a[n[i]] = a[n[i]] + 1
		else:
			#n[i] = a[n[i]] + 1
			a[n[i]] = 0
print(a)
"""


#5. 
