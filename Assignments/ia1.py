#2. 

"""
#4. Convert degree celsius to fahrenheit
#take input in degree celsius
input1 = int(input("Enter temperatue in ˚C:"))
print("temperature in fahrenheit is: "+str(input1*(9/5)+32))
"""

"""
#5. to check the palindrome
def isPalindrome(string):
	str = string[::-1]

	#check whether str and string are the same
	if str == string:
		print(True)
	else:
		print(False)

isPalindrome("malayalam")
"""

"""
#6. to count the number of vowels in a string
a = ['a','e','i','o','u','A','E','I','O','U']
b = input("Enter a string:")
count = 0
not_a_vowel = 0
for i in b:
	if i in a:
		count = count+1
	else:
		not_a_vowel = not_a_vowel+1
print("number of vowels is:"+str(count))
"""

"""
#7. to check the presence of substring in a string
b = input("Enter something:")
c = input("Enter substring:")
if c in b:
	print(True)
else:
	print(False)
"""


"""
#8. slice and convert to float
str = "X-DSPAM-Confidence:0.8475"
i = str.find(":")
res = str[i+1:]
print(float(res))
"""