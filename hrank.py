#list comprehensions
#Input:4 integers x,y,x and n each n four separate lines,respectively
#print the list in lexographic increasing order
#sample input:
"""
1
1
1
2
output:
[[0,0,0],[0,0,1],[0,1,0],[1,0,0],[1,1,1]]
"""
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
l = []
for i in range(a):
	for i in range
"""

"""
students = [['Harry',37.21],['Berry',37.21],['Tina',37.2],['Akriti',41],['Harsh',39]]
#sort the student list
students.sort()
for key,value in students:
	print(min(value))
"""

"""
#MongoDB ESSENTIALS
db.students.insert(
[
	{
	    "Studentno":"1",
	    "firstname":"sid",
	    "lastname":"m",
	    "age":"21"
	},
	{
	    "Studentno":"2",
	    "firstname":"dis",
	    "lastname":"n",
	    "age":"20"
	},
	{
	    "Studentno":"3",
	    "firstname":"ids",
	    "lastname":"o",
	    "age":"23"
	},
	{
	    "Studentno":"4",
	    "firstname":"john",
	    "lastname":"cena",
	    "age":"25"
	},
	{
	    "Studentno":"5",
	    "firstname":"dave",
	    "lastname":"bautista",
	    "age":"26"
	},
	{
	    "Studentno":"6",
	    "firstname":"dwyane",
	    "lastname":"rock",
	    "age":"25"
	},
	{
	    "Studentno":"7",
	    "firstname":"ric",
	    "lastname":"flair",
	    "age":"29"
	}
]
)




use school
db.students.find()
db.students.find(
{
"firstname":"sid","age":"21"
}
)

db.students.find(
{
$or : [{"firstname":"sid"},{"age":"25"}]
}
)


db.students.find(
{
"firstname":"sid" , $or : [{"age":"21"},{"age":"25"}]
}
)

db.students.update(
{"_id": ObjectId("5d2d7fdd4e49fb14661dd9cc")},
{$set : {"lastname":"mason"}}

)
db.students.find()

db.students.update(
{"age" : "25"},
{$set : {"lastname":"kohligfgfjhgfhgj"}},
{multi:true}
)


db.students.save(
{"_id" : ObjectId("5d2d7fdd4e49fb14661dd9cb"), 
    "Studentno" : "1", 
    "firstname" : "siddy", 
    "lastname" : "mythos", 
    "age" : "17"
}
)
db.students.find()

db.students.remove(
{"age" : "25"
} , 1
)

db.students.update(
{"_id" : ObjectId("5d2d7fdd4e49fb14661dd9ce")},
{$set : {"lastname":"cena"}}
)
db.students.find()

db.COLLECTION_NAME.find({},{KEY:1})
db.students.find({},{"firstname": 1,"_id":0})


db.students.find({},{"Studentno":1,"firstname":1,"_id":0}).limit(3)
db.students.find({},{"Studentno":1,"firstname":1,"_id":0}).skip(2)

db.students.find({},{"Studentno":1,"firstname":1,"_id":0}).skip(3).limit(3)

db.students.find({},{"Studentno":1,"firstname":1,"_id":0}).sort({"Studentno":1})

db.students.find({},{"Studentno":1,"firstname":1,"_id":0}).sort({"firstname":-1})

db.students.save(
{"_id" : ObjectId("5d2d7fdd4e49fb14661dd9cc"), 
    "Studentno" : "2", 
    "firstname" : "dis", 
    "lastname" : "mason", 
    "age" : "20",
    "gender":"female"}
)

db.students.find()

db.students.aggregate([{$group:{_id:"$gender",MaxAge:{$max : "$age"}}}]);
"""


"""
#Reverse Array problem
#input: [1,4,3,2]
#expected output: [2,3,4,1]
n = int(input("Enter a number:"))
m = input().strip().split()
res = m[::-1]
r = ""
for i in range(n):
	r = r + str(res[i]) + " "

print(r)
"""

"""
n = int(input("Enter a number:"))
m = input("Enter the numbers:").strip().split(' ')
sum = 0
for i in range(n):
	sum = sum  + int(m[i])
print(str(sum))
"""


"""
#5 4
#1 2 3 4 5
#o/p: 5 1 2 3 4
n = input("Enter a number:").strip().split(' ')
m = input("Enter numbers:").strip().split(' ')
p = n[0]
q = n[1]
i=0
res = []
while i < int(q):
	val = m[i]
	res.append(val)
	i = i + 1
l1 = m[int(q):]
l2 = res[:]
l1.extend(l2)
r = ""
for i in range(int(p)):
	r = r + str(l1[i]) + " "
print(str(r))
"""


"""
Our initial numbers are , , , , and . We can calculate the following sums using four of the five integers:

If we sum everything except1 , our sum is .14
If we sum everything except 2, our sum is .13
If we sum everything except 3, our sum is .12
If we sum everything except 4, our sum is .11
If we sum everything except 5, our sum is .10
"""

"""
res = []
n = input("Enter numbers:").strip().split(' ')
sum = sum1 = sum2 = sum3 = sum4 = 0
#while len(n) == 5:
if len(n) == 5:
	s1 = n[1:]
	#print(s1)
	#s2 = n[0]+n[2:]
	s2 = list(n[0]) + n[2:]
	#print(s2)
	s3 = n[0:2]
	s4 = n[3:]
	s3.extend(s4)
	#print(s3)
	s5 = n[0:3]
	s6 = n[4:]
	s5.extend(s6)
	#print(s5)
	s7 = n[:4]
	#print(s7)
	for num in s1:
		sum = sum + int(num)
	res.append(sum)
	#print(str(sum))

	for num in s2:
		sum1 = sum1 + int(num)
	res.append(sum1)
	#print(str(sum1))

	for num in s3:
		sum2 = sum2 + int(num)
	res.append(sum2)
	#print(str(sum2))


	for num in s5:
		sum3 = sum3 + int(num)
	res.append(sum3)
	#print(str(sum3))


	for num in s7:
		sum4 = sum4 + int(num)
	res.append(sum4)
	#print(str(sum4))

	#print(res)
	min = min(res)
	max = max(res)
	#print(sum)
	#print(str(sum))
	#print(str(sum1))
	#print(str(sum2))
	#print(str(sum3))
	#print(str(sum4))
	result = ""
	result = result + str(min) + " "  + str(max)
	print(result)
	#print(len(n))
	#print(min(res))
	#print(max(res))
else:
	m = n[1:]
	s1 = m[1:]
	#print(s1)
	#s2 = n[0]+n[2:]
	s2 = list(m[0]) + m[2:]
	#print(s2)
	s3 = m[0:2]
	s4 = m[3:]
	s3.extend(s4)
	#print(s3)
	s5 = m[0:3]
	s6 = m[4:]
	s5.extend(s6)
	#print(s5)
	s7 = m[:4]
	#print(s7)
	for num in s1:
		sum = sum + int(num)
	res.append(sum)
	#print(str(sum))

	for num in s2:
		sum1 = sum1 + int(num)
	res.append(sum1)
	#print(str(sum1))

	for num in s3:
		sum2 = sum2 + int(num)
	res.append(sum2)
	#print(str(sum2))


	for num in s5:
		sum3 = sum3 + int(num)
	res.append(sum3)
	#print(str(sum3))


	for num in s7:
		sum4 = sum4 + int(num)
	res.append(sum4)
	#print(str(sum4))

	#print(res)
	min = min(res)
	max = max(res)
	#print(sum)
	#print(str(sum))
	#print(str(sum1))
	#print(str(sum2))
	#print(str(sum3))
	#print(str(sum4))
	result = ""
	result = result + str(min) + " "  + str(max)
	print(result)
	#print(len(n))
	#print(min(res))
	#print(max(res))
"""


"""
#print the prime numbers between 2 and 50
start = 2
end = 50

for val in range(start,end+1):
	if val > 1:
		for n in range(2,val):
			if val%n == 0:
				break
		else:
			print(val)
"""

"""
def common_letters(string_one,string_two):
  res = []
  for i in string_one:
    if i in string_two and not (i in res):
      res.append(i)
  print(res)

common_letters("manhattan","san francisco")
"""

"""
def password_generator(username):
  password = ""
  for i in range(0,len(username)):
  	password+=username[i-1]
  return password

print(password_generator("AbeSimp"))
"""

"""
authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(',')
author_last_names = []
for name in author_names:
	author_last_names.append(name.split()[-1])
print(author_last_names)
"""

"""
highlighted_poems = "Afterimages:Audre Lorde:1997,  The Shadow:William Carlos Williams:1915, Ecstasy:Gabriela Mistral:1925,   Georgia Dusk:Jean Toomer:1923,   Parting Before Daybreak:An Qi:2014, The Untold Want:Walt Whitman:1871, Mr. Grumpledump's Song:Shel Silverstein:2004, Angel Sound Mexico City:Carmen Boullosa:2013, In Love:Kamala Suraiyya:1965, Dream Variations:Langston Hughes:1994, Dreamwood:Adrienne Rich:1987"

# print(highlighted_poems)

highlighted_poems_list = highlighted_poems.split(',')

# print(highlighted_poems_list)

highlighted_poems_stripped = []

for poem in highlighted_poems_list:
  highlighted_poems_stripped.append(poem.strip())
  
# print(highlighted_poems_stripped)

highlighted_poems_details = []

for poem in highlighted_poems_stripped:
  highlighted_poems_details.append(poem.split(':'))

#print(highlighted_poems_details)

titles = []
poets = []
dates = []

for info in highlighted_poems_details:
	titles.append(info[0])
	poets.append(info[1])
	dates.append(info[2])
print(titles)
print(poets)
print(dates)
"""

"""
#6. Porject on strings
daily_sales_replaced = daily_sales.replace(";,;",":")
print(daily_sales_replaced)
"""


"""
#importing the datetime module
from datetime import datetime

#creating a date(yyyy,mm,dd,h,mm,ss)
birthday = datetime(1997,12,29,13,30,8)


print(birthday.year)
print(birthday.month)
print(birthday.day)
print(birthday.hour)
print(birthday.minute)
print(birthday.second)

#to get the weekday 
#print(birthday.weekday())

#creating a date using datetime.now()
#print(datetime.now())

#getting the difference between dates
diff = datetime.now() - datetime(2017,1,1)
#print(diff) 

#using strptime
#converts string dates into datetime
parsed_date = datetime.strptime('Jan 15, 2018','%b %d, %Y')
#print(parsed_date.year)

#using strftime
date_string = datetime.strftime(datetime.now(),'%b %d, %Y')
print(date_string)
"""


"""
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

letter_to_points = {key:value for key,value in zip(letters,points)}
#print(letter_to_points)

letter_to_points[" "] = 0

def score_word(word):
  point_total = 0
  for letter in word:
    if letter in letters:
    	point_total+=letter_to_points[letter]
    else:
      point_total+=0
  return point_total

brownie_points = score_word("BROWNIE")
print(brownie_points)

#print(letter_to_points)


for element in how_many_s:
  if hasattr(element, "count"):
    print(element.count("s"))

"""

"""
x = int(input("enter x:"))
y = int(input("enter y:"))
z = int(input("enter z:"))
n = int(input("enter n:"))

#print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if ((i+j)!=n)])

for i in range(x+1):
	for j in range(y+1):
		for k in range(z+1):
			if (i+j+k)!=n:
				print([i,j,k])
"""
"""
#2D Array

#take input
number_matrix = []
number = int(input("Enter number:"))
for i in range(1,number+1):
	number_matrix.append(input("Enter elements:"))
print(number_matrix)
"""

"""
#30 Day coding challenge
#Day 2: Operators
#first line:total cost
#second line: tip percent
#third line: tax percent
#output:total cost after tip and tax
totalCost = float(input("Enter total cost:"))
tip_percent = float(input("Enter the tip percent:"))
tax_percent = float(input("Enter tax percent:"))

tip = float(totalCost*(tip_percent/100))
tax = float(totalCost*(tax_percent/100))

total_bill = totalCost+tip+tax
print(round(total_bill))
"""

"""
#Day 3: Given an integer,n, perform the following conditional actions:
#If n is odd, print Weird
#If n is even and in the inclusive range of 2 to 5, print Not Weird
#If n is even and in the inclusive range of 6 to 20, print Weird
#If n is even and greater than 20, print Not Weird

number = int(input("Enter a number:"))
if number%2 == 0 and number in range(2,6):
	print("Not Weird")
elif number%2 == 0 and number in range(6,21):
	print("Weird")
elif number%2 == 0 and number > 20:
	print("Not Weird")
else:
	print("Weird")
"""

"""
#Input is handled for you by the stub code in the editor.
#The first line contains an integer,  (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.
#Constraints
#Output Format
#Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print  or  lines (depending on whether or not a valid  was passed to the constructor).
#Sample Input
#4
#1,10,16,18
n = int(input("Enter a number:"))
for i in range(1,n+1):
	age = int(input("Input age:"))
	if age < 0:
		age = 0
		print("Age is not valid, setting the age to 0.")
		print("You are young.")
	elif age >= 0 and age <  13:
			print("You are young.")
	elif age >= 13 and age < 18:
		print("You are a teenager.")
	else:
		print("You are old.")

"""

"""
#First 10 multiples
num = int(input("Enter a number:"))
for i in range(1,11):
	print(str(num)+" X "+str(i)+" = "+str(num*i))
"""

#2
#Hacker
#Rank
"""
result = ''
result1 = ''
n = int(input("Enter a number:"))
for i in range(0,n):
	word = input("Enter a word:")
	for i in range(len(word)):
		if i % 2 == 0:
			#result.append(word[i])
			result = result+word[i]
		else:
			result1 = result1+word[i]
			#result1.append(word[i])
print(result+" "+result1)
"""

"""
n = int(input("Enter a number:"))
for i in range(0,n):
	word = input("Enter a word:")
	print("{} {}".format(word[::2],word[1::2]))
"""

"""
res = []
n = int(input("enter a number:").strip())
for i in range(0,n):
	#num = input("Enter number:")
	res.append(input("Enter a number:"))
for i in range(len(res),0,-1):
	print("{}".format(res[i-1]),end=' ')
"""


"""
#DAY 8
#3
#sam 99912222
#tom 11122222
#harry 12299933
#sam
#edward
#harry

names = {}
n = int(input("Enter a number:"))
for i in range(0,n):
	names.update([input("Enter name and salary").split(' ')])
for i in range(0,n):
	retrieve_name = input("Enter the names to be retrieved:")
	#print(len(retrieve_name))
	if retrieve_name in names:
		if len(retrieve_name)>1:
			print(retrieve_name+'='+names[retrieve_name])
		else:
			print("Not found")
"""


"""
#check for anagrams
#example: build and diblu should return "yes"
#else "no"

def anagrams(input1, input2):
	res = []
	res1 = []
	for i in input1:
		res.append(i)
	for i in input2:
		res1.append(i)
	for i in res:
		if i in res1:
			return "yes"
		else:
			return "no"

test_case = anagrams("beast","yeast")
print(test_case)
"""


"""
#printing the factorial of a number
#n = int(input("Enter a number:"))
def fact(n):
	if n == 1:
		return 1
	else:
		return n*fact(n-1)

n = fact(int(input("Enter a number:")))
print(n)
"""

"""
#DAY 10
#converting Base10 decimal numbers to Base2
def decimalToBinary(n):
	binary = ''
	i = 0
	while n > 0 and i < 8:
		s1 = str(int(n%2))
		binary = binary+s1
		n/=2
		i+=1
		d=binary[::-1]
	return d

print(decimalToBinary(100))
"""
"""
n = int(input("Enter a number:"))
b = bin(n)
res = b[2:]
lst = []
for i in res:
	lst.append(i)
print(lst)
"""

"""
#parentheses as a string
#return YES if it contains continuous parentheses(the pair should be present) else
#return NO
#input 2 {}{}[] {[)]}
#output YES NO

def parenthesisBalanced(values):
	s = []
	for i in range(len(values)):
		if values[i] == '{' or values[i] == '[' or values[i] == '(':
			s.append(values[i])
			print(s)
			

		if(len(s) == 0):
			return "yes"

		#if current character is not an opening
		#bracket, then it must be a closed bracket
		if values[i] == ')':
			x = s.pop()

			#check if the popped value matches with the top of stack
			if x == "{" or x == "[":
				return False

		elif values[i] == '}':
			x = s.pop()

			if x == "(" or x == "[":
				return False

		elif values[i] == "]":
			x = s.pop()

			if x == "(" or x == "{":
				return False

	

test_case = parenthesisBalanced("[()]{}{[()()]()}")
print(test_case)
"""

"""
#print the prime numbers between 1 and 100
n = int(input("ENter start:"))
m = int(input("ENter end:"))
for i in range(n,m+1):
	if i > 1:
		for j in range(2,i):
			if i%j==0:
				break
		else:
				print(i)

"""

"""
count = 1
res = []
n = bin(int(input("Enter a number:")))
n = n.replace('0b','')
for i in n:
	res.append(i)
#if(any(res[i] == res[i+1] for i in range(len(res)-1))):
while len(res) > 1:
	if
"""

"""
#binary_nos = [0,1]
count = 1
lst = []
n = bin(int(input("Enter a number:")))
n = n.replace('0b','')
for i in n:
	lst.append(i)
#for i in :
for i in range(0,len(lst)-1):
	#print(i)
	#if i == 1:
	if lst[i] == lst[i+1]:
		count+=1
print(n)
print(count)
"""

"""
import math
n = int(input("Enter:").strip())
count = 0
maxi = 0
while n > 0:
    if n % 2 == 1:
        count += 1
    else:
        if count > maxi:
            maxi = count
        count = 0
    n=math.floor(n / 2)
if count > maxi:
    maxi = count
print(maxi)
"""

"""
#display fibonacci series using yield() keyword
n = int(input("enter:"))

def fibon(n):
	a = 0
	b = 1
	for i in range(n):
		yield a
		a,b = b,a+b

for num in fibon(n):
	print(num)

"""


"""
#printing a 6X6 matrix
matrix = []
#row = []
for i in range(6):    #row count is 6
	row = []
	for j in range(6):		#column count is 6
		row.append(0)
	matrix.append(row)
print(matrix)
"""

class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
	def __init__(self,firstName,lastName,id,scores):
		self.firstName = firstName
		self.lastName = lastName
		self.id = id
		self.scores = scores

	"""
	def calculate():
		for i in range(len(scores)-1):
			if i =
	"""


line = input("enter:").split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
#numScores = int(input("enter:")) # not needed for Python
scores = list( map(int, input("enter:").split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())







