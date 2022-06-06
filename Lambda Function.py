#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Let's write a function that returns twice its value.


# In[6]:


def double(x):
    return x *2
print(double(10))


# In[7]:


## Let's write a lambda function that returns twice its value.


# In[8]:


double = lambda x: x*2
print(double(10))


# In[9]:


# It takes default value


# In[10]:


double = lambda x = 2: x*2
print(double(23))


# In[11]:


double = lambda x = 2: x*2
print(double())


# In[12]:


# Using if, else decision structures with functions.


# In[13]:


def max(x,y):
    if x > y:
        return x
    else:
        return y
max(45,60)


# In[15]:


max = lambda x, y: x if x > y else y
max(45,60)


# In[16]:


# Multiply each value in the list by 10.
my_list = [1,2,3,4]
new_list = lambda x: (i*10 for i in x)
print(list(new_list(my_list)))


# In[17]:


# Sorted
my_list = [[2,6,4,1],[7,5,3,9]]
sort_list = lambda x: (sorted(i) for i in x)
print(list(sort_list(my_list)))


# In[20]:


# Using with map()
my_list = [1,2,3,4,5,6,7,8,9,0]
new_list = list(map(lambda x: x*2, my_list))
print(new_list)


# In[22]:


# Print the code block that returns 3 times each first element in the list with map.
A = [[1,2], [3,4], [5,6]]
print(list(map(lambda x: x[0] * 3, A)))


# In[24]:


# First, find the list whose list [10,20,30,40,50] is greater than 20 with filter.
# With map, make integer division on the elements in this list and divide by 10.

my_list = [10,20,30,40,50]
new_list = list(map(lambda x: x //10, filter(lambda x: x > 20, my_list)))
                    
print(new_list)                   


# In[25]:


# Let's define a mixed type list. 
# Find elements of type int in the list.
my_list = ["python", 20, 10, True, 30, "b"]
list(filter(lambda a: type(a) == int, my_list))


# In[26]:


# Let's capitalize the first letters of our list.
my_list= ["anna", "rebecca", "jack"]
list(map(lambda x: x.capitalize(), my_list))


# In[27]:


# define a string type list 
# then print them in capital letters.
my_list= ["anna", "rebecca", "jack"]
list(map(lambda x: x.upper(), my_list))


# In[31]:


# Let's write a function that checks if a number is even.
def function(number):
    return number % 2 == 0
print(function(40))


# In[32]:


def function(number):
    return number % 2 == 0
print(function(41))


# In[34]:


# Let's write a lambda function that checks if a number is even.
function = lambda x: x % 2 == 0
print(function(40))


# In[35]:


function = lambda x: x % 2 == 0
print(function(41))


# In[36]:


# Calculate the square of all numbers in a list.
x = [2,5,10,23,3,6]
for i in x:
    print(i **2)
    


# In[37]:


print(*map(lambda number: number ** 2 , x))


# In[ ]:




