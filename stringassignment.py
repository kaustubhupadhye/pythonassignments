#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python program find a 
#list of integers with exactly two occurrences#
#of nineteen and at least three occurrences of five.
lst=[19, 19, 5, 5,5 ,1, 5]
if lst.count(19)==2 and lst.count(5)>=3:
    print("true")
else:
    print("false")
    


# In[ ]:


#2. Write a Python program that accept a list of integers and check the length and the fifth element.#
#Return true if the length of the list is 8 and fifth element occurs thrice in the said list. 

temp=input("Enter comma seperated input").split(",")
a=[]
for i in temp:
    a.append(i)
print(a) 
if len(a)!=8:
    print("enter 8 char")
b=a.count(a[5])
if len(a)==8 and b<=3:
    print("True")
else:
    print("False")


# In[ ]:


#3.  Write a Python program to split a string of words separated by commas and spaces into two lists, words and separators. 
#Input: The dance, held in the school gym, ended at midnight.
#Output:
#[['The', 'dance', 'held', 'in', 'the', 'school', 'gym', 'ended', 'at', 'midnight.'], [' ', ', ', ' ', ' ', ' ', ' ', ', ', ' ', ' ']]


a="The dance, held in the school gym, ended at midnight."
c=a.split(" ")

e=[]
for i in c:
    e.append(",")
c.extend(e)
print(c)


# In[ ]:


#4. Write a Python program to find missing numbers from a list. Input : [1,2,3,4,6,7,10]
#Output : [5, 8, 9]

s=[1,2,3,4,6,7,10]
c=[]
for i in range(s[0],s[6]):
    if i not in s:
        c.append(i)
print("missimg numbers are",c)    


# In[3]:


#5. Write a Python program to push all zeros to the end of a list. Input : [0,2,3,4,6,7,10]
#Output : [2, 3, 4, 6, 7, 10, 0]
n=[0,2,3,4,6,7,10]
for i in n:
    if i==0:
        n.remove(0)
        n.append(0)
print(n)


# In[3]:


a=[]

while True:
    i=str(input("enter"))
    if i=="q":
        break
    else:
        a.append(i)

type(a[1])


# In[ ]:


a= [2, 3, 5, 7, 9, 11,0]
a.remove(0)
a
type(a[3])


# In[ ]:





# In[ ]:




