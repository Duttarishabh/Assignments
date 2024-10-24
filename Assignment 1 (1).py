#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1. Explain with an example each when to use a for loop and a while loop.
for i in range(1,10):
    print(i)
#we use for loop when we know the number of times we have to iterate the loop.


# In[2]:


i=0
while i<=10:
    print(i)
    i=i+1
#while  loop is use best when we don't know the iteration, as it depends more on the condition.


# In[ ]:


""""Write a python program to print the sum and product of the first 10 natural numbers using for
and while loop.""""


# In[1]:


sum=0
prod=1
for i in range(1,11):
        sum=sum+i
        prod=prod*i
        print(sum, prod)
    


# In[10]:


sum=0
prod=1
i=1
while i<11:
    sum+=i
    prod=prod*i
    print(sum,prod)
    i=i+1
    


# In[11]:


"""Create a python program to compute the electricity bill for a household.
Q4. Create a list of numbers from 1 to 100. Use for loop and while loop to calculate the cube of each
number and if the cube of that number is divisible by 4 or 5 then append that number in a list and print
that list.
The per-unit charges in rupees are as follows: For the first 100 units, the user will be charged Rs. 4.5 per
unit, for the next 100 units, the user will be charged Rs. 6 per unit, and for the next 100 units, the user will
be charged Rs. 10 per unit, After 300 units and above the user will be charged Rs. 20 per unit.


You are required to take the units of electricity consumed in a month from the user as input.


Your program must pass this test case: when the unit of electricity consumed by the user in a month is
310, the total electricity bill should be 2250."""


# In[33]:


# Input the number of electricity units consumed
units_consumed = int(input("Enter the number of electricity units consumed in a month: "))

# Calculating the electricity bill
if units_consumed <= 100:
    bill = units_consumed * 4.5
elif units_consumed <= 200:
    bill = (100 * 4.5) + (units_consumed - 100) * 6
elif units_consumed <= 300:
    bill = (100 * 4.5) + (100 * 6) + (units_consumed - 200) * 10
else:
    bill = (100 * 4.5) + (100 * 6) + (100 * 10) + (units_consumed - 300) * 20

# Printing the total bill
print(f"Total electricity bill for {units_consumed} units is: Rs. {bill}")

# Part 2: Calculating cubes of numbers from 1 to 100 divisible by 4 or 5
numbers = []
for i in range(1, 101):
    cube = i ** 3
    if cube % 4 == 0 or cube % 5 == 0:
        numbers.append(i)

# Printing the list of numbers whose cubes are divisible by 4 or 5
print(f"Numbers from 1 to 100 whose cubes are divisible by 4 or 5: {numbers}")


# In[42]:


vowel = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")  # Tuple of vowels
s = "I want to become a data scientist"  # String to check vowels in
count = 0  # Initialize count

for i in s:  # Iterate through each character in the string
    if i in vowel:  # Check if the character is a vowel (in the tuple)
        print(i)  # Print the vowel
        count += 1  # Increment the count

print(f"Total number of vowels: {count}")


# In[ ]:





# In[ ]:




