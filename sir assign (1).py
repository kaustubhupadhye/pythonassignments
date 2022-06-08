#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Exercise Question 1: Given a two list. Create a
#third list by picking an odd-index element from the first list and even index
#elements from the second

c = [3, 6, 9, 12, 15, 18, 21] #1
d = [4, 8, 12, 16, 20, 24, 28]
a=[]
b=[]   
for i in range(len(c)):
    if i %2==1:
        a.append(c[i])
for i in range(len(d)):
    if i %2==0:
        b.append(d[i])
print("list with odd index :",a)
print("list with even index :",b)
f=[]
for i in a:
    f.append(i)
for j in b:
    f.append(j)
print("final list:",f)    


# In[56]:


#Write a Python program to print the numbers of a
#specified list after removing even numbers from it.  


c = [3, 6, 9, 12, 15, 18, 21]  #1 method 2
d = [4, 8, 12, 16, 20, 24, 28]
odd=[]
odd=c[1:len(c):2]
print("odd number of index from 1st list: ",odd)
f=[]
even=d[0:len(d):2]
print("even number of index from 2nd list :",even)
j=[]
j.extend(odd)
print()
j.extend(even)
print("Final elemnet",j)







# In[60]:


#Given a number count the total number of digits in a number

var=input("enter a number")#2
a=var
print('total number of digits',len(a))


# In[122]:


#Write a Python program to print the numbers of a specified list after removing even numbers from it.  

ls = [3, 6, 9, 12, 15, 18, 21]#3
b=ls[1]
print(b)
for i in ls:
    if i%2==0:
        ls.remove(i)
print("after removing even number: ",ls)
c=ls[1]
print(c)    
   

    


# In[113]:


num = [7,8, 120, 25, 44, 20, 27]#3 b
num = [ x for x in num if x%2!=0]
print("after removing even number",num)


# In[76]:


# Write a Python program to generate and print a list offirst and last 5 elements
#where the values are square of numbers between 1 and30 (both included).  


c = [3, 2,4,5,6, 9, 12, 15, 18, 21,4, 8, 12, 16, 20, 24, 28,1]#6
b=c[:]
d=c[0:5]
a=[]
j=[]
z=[]
s=[]
for b in d:
    a.append(b)
print(a)
f=c[-1:-6:-1]
f
for b in f:
    j.append(b)
print(j) 
a.extend(j)
print("first 5 and last 5 elemnts:",a)
for i in a:
    z.append(i**2) 
print("square of number",z)  
for i in z:
    if i < 30:
        s.append(i)
print("less than 30 square numbers are",s)    

    
    
    
  

    
    


    


# In[14]:


#Write a Python program to generate all permutations of a list in Python.

a=permutations([1,2,3]) #6
for i in a:
     print(i) 


# In[1]:


#Write a python program to check whether two lists are circularly identical.   


ls = [3, 6, 9, 12, 15, 18, 21]#7
st= [3, 6, 9,18, 21,7,5,12,15,18]
for i in ls:
    print(i,end=" ")
print()
for j in st:
    print(j,end=" ")
print()    
if i==j:
    print("identical")
else:
    print("not identical")

        


# In[1]:


#Write a python program to check whether two lists are circularly identical.
ls = [3, 6, 9, 15, 10, 18, 21]#7
st= [3, 6, 9,18, 21,15,12]
for i in ls:
    if i in st:
        print(i,"identical")
    else:
        print(i,"not identical")
        break
        
        



# In[19]:


#Write a python program to check whether two lists are circularly identical.

l1 = [10, 0, 0, 10, 5]  #7

l2 = [10, 5, 10, 0, 0]

l3 = [5, 10, 10, 0, 0]

for i in range(len(l2)):
    l1.append(l1[i])

s1 = str(l1)
s2 = str(l2)
s3 = str(l3)

x = s2[1:len(s2) - 1]
y = s3[1:len(s3) - 1]

print("For l1 and l2 ", x in s1)

print("For l1 and l3 ", y in s1)


# In[9]:


# Write a Python program to change the position of every n-th value with the (n+1)th in a list. 

a=[0,1,2,3,4,5]#7
for i in range(0,len(a),2):
    a[i],a[i+1] = a[i+1],a[i]
print(a)


# In[10]:


#Write a Python program to iterate over two lists simultaneously
a = [1,2,3,4,5]#8
b = [6,7,8,9,10]
c = []
j=0
for i in a:
    c.append(i)
    c.append(b[j])
    j+=1
c


# In[9]:


#Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2
#distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]

from itertools import combinations#9
a=combinations([1,2,3,4,5],2)
for i in a:
    print(i,end=" ")


# In[14]:


a=[1,2,3,4,5,6]#9
c=[]
for i in a:
    for j in a:
        b=[]
        if (i == j):
            pass
        elif i != j:
            b.append(i)
            b.append(j)
            c.append(b)
print("Combination of distinct elements are: ",c)



# In[15]:


#Write a Python program to remove duplicates from a list of lists. 
list1=[[10,20],[40],[30,56,25],[10,20],[33]]#10
list2=[]
for i in list1:
    if i not in list2:
        list2.append(i)

print(list2)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




