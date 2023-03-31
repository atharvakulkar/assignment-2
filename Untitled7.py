#!/usr/bin/env python
# coding: utf-8

# QUES 1

# In[9]:


marks = int(input("entyer your marks"))
if marks >90:
    print("your grade is A")
elif marks >80 and marks <=90:
    print("your grade is B")
elif marks >=60 and marks <=80:
    print("your grade is C")
else:
    print("your grade is D") 


# QUES 2

# In[10]:


price = int(input("enter the price of bike "))
if price >100000 :
    print ("Your road tax is 15%")
elif price >50000 and price <100000 :
    print("Your road tax is 10%")
else :
    print("Your road tax is 5%")

QUES 3
# In[11]:


city = input("enter your city")
if city == "Delhi" :
    print("Monument of your city is Red Fort")
if city == "Agra" :
    print("Monument of your city is Tajmahal")
if city == "Jaipur":
    print("Monument of your city is Jal Mahal")


# QUES 4

# In[13]:


num = int(input("Enter the numbers"))
count = 0
while num > 10:
    num = num / 3
    count += 1
print(count)


# QUES 5 

# In[14]:


'''Ans => Python while loop is used to run a block code until a certain
condition is met.
      The syntax of while loop is:
      while condition:
      # body of while loop
      Here,
      A while loop evaluates the condition
      If the condition evaluates to True, the code inside the while
      loop is executed.
      condition is evaluated again.
      This process continues until the condition is False.
      When condition evaluates to False, the loop stops'''


# QUES 6 

# In[15]:


# Pattern 1:
i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
    print("")
    i += 1
    
print("-----")
# Pattern 2:
i = 5
while i >= 1:
    j = i
    while j >= 1:
        print("*", end="")
        j -= 1
    print("")
    i -= 1

print("-----")
# Pattern 3:
i = 5
while i >= 1:
    j = 1
    while j <= 5:
        if j >= i:
            print("*", end="")
        else:
            print(" ", end="")
        j += 1
    print("")
    i -= 1


# QUES 7 

# In[16]:


i =10
while i>0:
    i  = i-1
    print(i)


# In[ ]:




