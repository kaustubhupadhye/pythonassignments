#!/usr/bin/env python
# coding: utf-8

# # Digit or Alphabet
# 
# Description Write a program to display whether the input is a digit or a letter of the alphabet.
# 
# Input:
# 
# A digit or a letter of the alphabet
# 
# Output:
# 
# Displays whether the given output is an integer or a letter of the alphabet
# 
# Sample input:
# 
# 1
# 
# Sample output:
# 
# Integer
# 
# Sample input:
# 
# b
# 
# Sample output:
# 
# Alphabet

# In[6]:


a= input("Enter a number or character")

if (a.isalpha()):
    print("this a charcter")
    
elif(a.isdigit()):
    print("this a  number")
else:
    print("this is special character")
    


# # Description Write a program to accept a character and display its next and previous character.
# 
# Hint: Make use of Ascii values here.
# 
# Input:
# 
# A character
# 
# Output:
# 
# Previous character and the next character of the given character
# 
# Sample input:
# 
# D
# 
# Sample output:
# 
# C
# 
# E
# 
# Sample input:
# 
# 8
# 
# Sample output:
# 
# 7
# 
# 9
# 
# Sample input:
# 
# @
# 
# Sample Output:
# 
# ?
# 
# A

# In[10]:


ch = input("enter a char  ")

x = chr(ord(ch)+1) # compare it to ascii value
#The ord() function returns the number representing the unicode code of a specified character.
print (x)

y = chr(ord(ch)-1)
print (y)


# # Write a program to accept a string from the user, delete all vowels from the string and display the result.
# Input:
# 
# A string
# 
# Output:
# 
# A string with vowels removed
# 
# Sample input:
# 
# Upgrad
# 
# Sample output:
# 
# pgrd
# 
# Sample input:
# 
# Python Programming
# 
# Sample output:
# 
# Pythn Prgrmmng

# In[23]:


a=str(input("enter a string"))
b=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
d=""

for c in a:
    if c not in b:
        
        d=d+c
        
print("\nWith Vowels =", a)
a = d

print("\nWithout Vowels =", a)


# # Write a program to display the multiplication table of a given number.
# Input:
# 
# A positive integer
# 
# Output:
# 
# Multiplication table
# 
# Sample input:
# 
# 5

# In[35]:


num=int(input("enter a number of table"))

for i in  range(1,11):
    
     print(num, 'x', i, '=', num*i)


# In[ ]:




