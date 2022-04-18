#!/usr/bin/env python
# coding: utf-8

# # Q. 11 Program to find the factorial of a number

# In[ ]:


number = int(input("Please enter the number to find Factorial : "))

factorial = 1

if number <=0:
    print("Invalid Input, Input must be greater than 0")
    
else:
    
    for n in range(1, number + 1):
        
        factorial = factorial * n
        
    print("The factorial of", number, "is", factorial)


# # Q. 12 Program to find whether a number is prime or composite.

# In[ ]:


num = int(input("Enter any number : "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is COMPOSITE number")
            break
    else:
        print(num, "is a PRIME number")

else:
    print(num, "is a neither prime NOR composite number")


# # Q. 14 Program to get the third side of right-angled triangle from two given sides.

# In[ ]:


def rightangle(opp_side, adj_side, hyp):
    
    if hyp== str('n'):
        
        return ('Hypotenuse = '+ str(((opp_side**2)+(adj_side**2))**0.5))
    
    elif opp_side == str('n'):
        
        return ('Opposite = '+ str(((hyp**2)-(adj_side**2))**0.5))
    
    elif adj_side == str('n'):
        
        return ('Adjacent = '+ str(((hyp**2)-(opp_side**2))**0.5))
    else:
        
        print("You have all the values")             


# # Q. 13 Program to check whether a given string is palindrome or not.

# In[ ]:



my_str = input("Enter your string ")

# make it suitable for caseless comparison
my_str = my_str.casefold()

rev_str = reversed(my_str)

print('Your entered string is : ', my_str)

if list(my_str) == list(rev_str):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")


# In[ ]:




