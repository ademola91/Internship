#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11. Write a python program to find the factorial of a number.


# In[2]:


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

number = int(input("Enter a number to find its factorial: "))

if number < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")


# In[3]:


#12. Write a python program to find whether a number is prime or composite.


# In[4]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(num, "is a prime number")
else:
    print(num, "is a composite number")


# In[5]:


#13. Write a python program to check whether a given string is palindrome or not.


# In[6]:


def is_palindrome(s):
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")


# In[7]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.


# In[8]:


from math import sqrt

def calculate_third_side(a, b):
    return sqrt(a**2 + b**2)

side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
third_side = calculate_third_side(side1, side2)
print("The length of the third side is", third_side)


# In[9]:


#15. Write a python program to print the frequency of each of the characters present in a given string.


# In[ ]:


def count_chars(string):
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

string = "Hello World"
print(count_chars(string))


# In[ ]:




