#Write a Python program to check if a number is positive, negative or zero
"""
num=int(input("enter number:"))
if num>0:
    print("number is positive")
elif num==0:
    print("number is zero")
else:
    print("number is negative")

print (num)
"""

#Write a Python program to get the Factorial number of given number

"""num=int(input("enter number:"))
factorial=1
if num<0:
    print("factorial of negative number doesn't exist")
elif num==0:
    print("factorial of zero is 1")
else:
     for i in range(1,num+1):
        factorial=factorial*i
        print("factorial of",num,"is",factorial)"""
  
#Write a Python program to get the Fibonacci series of given range.
"""
from itertools import count


n1=0
n2=1
limit=int(input("enter a number:"))
print(n1)
print(n2)
count=2
while count<limit:
    n3=n1+n2
    n1=n2
    n2=n3
    print(n3)
    count+=1
    
    """

    #How memory is managed in Python?
"""
     The Python memory manager has different components which deal with 
    various dynamic storage management aspects, like sharing, segmentation, 
    preallocation or caching.

    At the lowest level, a raw memory allocator ensures that there is 
    enough room in the private heap for storing all Python-related data
     by interacting with the memory manager of the operating system.

     On top of the raw memory allocator, several object-specific allocators
     operate on the same heap and implement distinct memory management policies
     adapted to the peculiarities of every object type.


"""
    #What is the purpose continue statement in python?
"""The continue keyword is used to end the current iteration in a for
loop (or a while loop),and continues to the next iteration"""

#Write python program that swap two number with temp variable and without temp variable.

#with temp variable.
"""
x = 5
y = 10
    
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

#without temp variable.

x = 5
y = 10

x, y = y, x
print("x =", x)
print("y =", y)
"""

#Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user.
"""
num=int(input("enter a number :"))
if num%2==0:
    print("number is even")
else:
    print("number is odd")
print("successfully got the number")
"""

#Write a Python program to test whether a passed letter is a vowel or not.
"""
vowel=['a','e','i','o','u','A','E','I','O','U']
letter=(input("enter a letter:"))
if letter in vowel:
        print("its a vowel")
else:      
         print("SORRY!!its not a vowel")
"""

#Write a Python program to sum of three given integers.However, if two values are equal sum will be zero.
"""
x=int(input("enter first number:"))
y=int(input("enter second number"))
z=int(input("enter third  number"))

if x == y or y == z or x==z:
        sum = 0
else:
        sum = x + y + z

print(sum)
"""
#Write a Python program that will return true ifthe two given integervalues are equal or their sum or difference is 5.
"""
x=int(input("enter first number:"))
y=int(input("enter second number:"))

if x == y or abs(x-y) == 5 or (x+y) == 5:
     print("true")
else:
       print("False")
"""
#Write a python program to sum of the first n positive integers
"""
n= int(input("Input a number: "))
sum = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum)
"""
#Write a Python program to calculate the length of a string.
"""
str = input("Enter a string: ")
counter = 0
for s in str:
      counter = counter+1
print("Length of the input string is:", counter)
"""
#Write a Python program to count the number of characters (character frequency) in a string
"""
string = input("enter string:")

for i in string:
    frequency = string.count(i)
    print(str(i) + ": " + str(frequency), end=", ")
"""
#What are negative indexes and why are they used?
"""Python programming language supports negative indexing of arrays, 
something which is not available in arrays in most other programming languages.

This means that the index value of -1 gives the last element, and -2 gives the
 second last element of an array. The negative indexing starts from where the array ends."""

 #Write a Python program to count occurrences of a substring in a string.
"""
 str1 = 'tu ayy b tu ayy'
print()
print(str1.count("tu ayy"))
print()
"""
#Write a Python program to count the occurrences of each word in a given sentence
"""
str=input("Enter string:")
word=input("Enter word:")
count=0
for i in range(0,len(str)):
      if(word==str[i]):
            count=count+1
print("Count of the word is:")
print(count)
"""
#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
"""
str1 = input("Please Enter First String : ")
str2 =input("Please Enter Second String : ")
x=str1[0:2]
str1=str1.replace(str1[0:2],str2[0:2])
str2=str2.replace(str2[0:2],x)
print("Your first string has become :- ",str1)
print("Your second string has become :- ",str2)
"""
#Write a Python program to add 'ing' at the end of a given string (length should be at least 3). 
# If the given string already ends with 'ing' then add 'ly' instead if the string length of the given string is less than 3, leave it unchanged.
"""
str=input("enter string:")
length = len(str)
if length > 2:
    if str[-3:] == 'ing':
      str += 'ly'
    else:
      str += 'ing'
print(str)
"""
#Write a Python program to find the first appearance of the substring 'not' and 'poor' froma given string, if 'not' follows the 'poor', replace the whole'not'...'poor'substring with 'good'. 
# Return the resulting string.
"""
str1=input("enter string:")
s1 = str1.find('not')
s2 = str1.find('poor')
if s2 > s1 and s1>0 and s2>0:
    str1 = str1.replace(str1[s1:(s2+4)], 'good')
    print (str1)
else:
   print (str1)
   """
#Write a Python function that takes a list of words and returns the length of the longest one.
"""
def longest_word(list):
    word_len = []
    for n in list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = longest_word(["titanium", "mercury", "aluminium"])
print("Longest word: ",result[1])
print("Length of the longest word: ",result[0])
"""
#Write a Python function to reverses a string if its length is a multiple of 4.
"""
def reverse_string(str):
    if len(str) % 4 == 0:
       return ''.join(reversed(str))
    return str

print(reverse_string('help'))
print(reverse_string('python'))
"""
#Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. Ifthe string length is less than 2,return instead of the empty string.

"""
def string_fun(str):
  if len(str) < 2:
    return ''

  return str[0:2] + str[-2:]

print(string_fun('w3resource'))
print(string_fun('w3'))
print(string_fun('w'))
"""
#Write a Python function to insert a string in the middle of a string
"""
def insert_str(str, word):
	return str[:2] + word + str[2:]

print(insert_str('eeee', 'shweta'))
print(insert_str('oooo', 'shirin'))
print(insert_str('iiii', 'helly'))
"""



