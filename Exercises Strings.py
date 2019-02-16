'''1. Write a Python program to calculate the length of a string.'''

string='Abracadabra'

print(len(string))

#2. Write a Python program to count the number of characters (character frequency) in a string.

string='abracadabra'
print(string.count('a'))

def counting(a):
	b= [letter for letter in a.split()]


#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. If the string length is less than 2, return instead of the empty string.

user=input('Give me a string')

for letter in user:
	if len(user)<2:
		print(user.clear())
	if len(user)>2:
		print(user[:2] + user[-2:])
		break

#4. Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.

def change_str(a):
	char=a[0]
	replace1=a.replace(char, '$')
	print(replace1)
	modificare=char+replace1[1:]

	print(modificare)

#5. Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string. Go to the editor
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'

def string(a,b):
	z = a[0]+b[1:]+" "+b[0]+a[1:]
	return z

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.

def string(a):
	'''THIS FUNCTION IS FOR KIDS'''
	if len(a)<3:
		print(a)
	elif len(a)>3:
		if a[-3:]=='ing':
			print(a+'ly')
		else:
			print(a+ 'ing')

# . Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'
# Return the resulting string.
#Sample String : 'The lyrics is not that poor!'
#'The lyrics is poor!'
#Expected Result : 'The lyrics is good!'
#'The lyrics is poor!'

def appeareance(a):
	c=a.replace('not poor', 'good', 1)
	print(c)




a='Ana are mere acasa'

print(a.find('are mere'))


def not_poor(str1):
	snot = str1.find('not')
	spoor = str1.find('poor')

	if spoor > snot and snot > 0 and spoor > 0:
		str1 = str1.replace(str1[snot:(spoor + 4)], 'good')
		return str1
	else:
		return str1


print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))

#8. Write a Python function that takes a list of words and returns the length of the longest one.

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][1]

#9. Write a Python program to remove the nth index character from a nonempty string.

def index(a):
	b=input('Provide a string')
	for char in b[a]:
		print(b.replace(b[a], ''))

#10. Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

def program(a):
	b=a[1:-1]
	return a[-1] + b + a[0]

def change_sring(str1):
	return str1[-1:] + str1[1:-1] + str1[:1] #TO BE CHECKED

#11. Write a Python program to remove the characters which have odd index values of a given string.

def odd_values_string(str):
  result = ""
  for i in range(len(str)): #TO BE CHECKED AGAIN
    if i % 2 == 0:
      result = result + str[i]
  return result

#12. Write a Python program to count the occurrences of each word in a given sentence.

def counts(a):
	for words in a.split():
		print(a.count(words))


#w3school varianta:

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] =counts[word]+1
        else:
            counts[word] = 1

    return counts

#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

user_input =input('What is your favorite color?')
print('My favorite color is {0}'.format(user_input.upper()))
print('My favorite color is {0}'.format(user_input.lower()))

#14. Write a Python program that accepts a comma separated sequence of words as input and prints the unique words in sorted form (alphanumerically).

def seq(*args):
	a=set(args)
	for elem in a:
			a.add(elem)
	d=sorted(a)
	e= ','.join(d)
	return e

#15. Write a Python function to create the HTML string with tags around the word(s).
#add_tags('i', 'Python') -> '<i>Python</i>'

def add_tags(a,b):
	return '<' + a + '>' + b + '<' + a + '/>'

#16. Write a Python function to insert a string in the middle of a string.
#insert_sting_middle('[[]]<<>>', 'Python') -> [[Python]]

def insert_string(a,b):
	c= [num for num in a]
	c.insert(4, b)
	d=''.join(c)

		return d

#17. Write a Python function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2)
#insert_end('Python') -> onononon

def insert_end(a):
	if len(a)<2:
		print('Lenght must be at least 2')
	else:
		print (a[-2:] *4)
#18. Write a Python function to get a string made of its first three characters of a specified string. If the length of the string is less than 3 then return the original string.
#first_three('ipy') -> ipy
#first_three('python') -> pyt

def first_three(a):
	if len(a)<3:
		return a
	else:
		return a[:3]

#19. Write a Python program to get the last part of a string before a specified character.

def specif_separator(a):
	b=a.rsplit('/', 1)
	return b[1]

#20. Write a Python function to reverses a string if it's length is a multiple of 4

def lenght(a):
	if len(a)%4==0:
		return a[::-1]
	else:
		print('Not multiple of 4')

#21. Write a Python function to convert a given string to all uppercase if it contains at least 2 uppercase characters in the first 4 characters.

def convert(a):           #first version but only works if all letter from index 0 to 3 are upper
	if a[:4].isupper():
		print(a.upper())
	else:
		print('First characters are not upper!')

def convert(str1):
	count=0

	for letter in str1[:4]:
		if letter==letter.upper():
			count=count+1
	if count>=2:
		return str1.upper()
	return str1

#22.Write a Python program to sort a string lexicographically.

def str(a):
	for letter in a:
		b=sorted(a)
		return b

#23. Write a Python program to remove a newline in Python.

str='This is war \n'
print(str)
print(str.rstrip())

#24. Write a Python program to check whether a string starts with specified characters.

def mystr(a):
	print(a.startswith('al'))


def factorial(n):
	if n == 1:
		return 1
	else:
		res = n * factorial ( n - 1 )
		print ( "rez intermed pentru ", n, " * factorial(", n - 1, "): ", res )

		return res


