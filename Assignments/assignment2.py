"""
#1. Write a program to replace the line which starts with "From" to "To" and vice versa
n = input("Enter filename:")
count = 0
try:
	fhand = open(n)
	#inp = fhand.read()
	for line in fhand:
		line = line.strip()
		if line.startswith("From:"):
			line = line.replace("From:","To:")
		elif line.startswith("To:"):
			line = line.replace("To:","From:")
		print(line)
except:
	print("Enter a valid filename.")
"""


"""
#2. Write a program to read through a file and print contents of the file, all in
#upper case letters
n = input("Enter filename:")
count = 0
try:
	fhand = open(n)
	for line in fhand:
		line = line.strip()
		line = line.upper()
		print(line)
except:
	print("Enter a valid filename.")
"""


"""
#3. Write a program too extract all the numbers in a file.
num = ['1','2','3','4','5','6','7','8','9','0']
n = input("Enter filename:")
try:
	fhand = open(n)
	for line in fhand:
		for i in line:
			if i in num:
				print(int(i))

except:
	print("Enter a valid filename")
"""


"""
#4. Write a program to read a file line by line and write each line in reverse order in 
#another file.
n = input("Enter filename:")
f2 = open('file2.txt','a')

try:
	fhand = open(n)
	for line in fhand:
		line = line[::-1]
		f2.write(line)
except:
	print("Enter a valid filename.")
"""




