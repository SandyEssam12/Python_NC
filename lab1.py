# Question 1
# a = [10, 20, 30, 20, 40, 50]
# Remove the first occurance of 20
a = [10, 20, 30, 20, 40, 50]
a.remove(20)
print(a)

# _________________________________________________________________________________
# Question 2
# Remove element at index 1 and return its value in val
val=a.pop(1)
print(f"{val=}") 

# _________________________________________________________________________________
# Question 3
# a = [10, 20, 30, 40, 50, 60, 70]
# Removes elements from index 1 to index 3 (which are 20, 30, 40)
a = [10, 20, 30, 40, 50, 60, 70]
del a[1:4]
print(a)

# _________________________________________________________________________________
# Question 4
# a = [10, 20, 30, 40, 50, 60, 70]
# Remove all elements
a = [10, 20, 30, 40, 50, 60, 70]
a.clear()
print(a)

# _________________________________________________________________________________
# Question 5
# Write a program that prints the number of times the substring 'iti' occurs in a string
str='iti'
print(str.count('i'))

# _________________________________________________________________________________
# Question 6
# application to take a number in binary form from the user, and print it as a decimal
num=input('Enter binary number: ')
decimal_num=int(num,2)
print(f"{decimal_num= }")

# _________________________________________________________________________________
# Question 7
# write a code take a number as an argument 
# and if the number divisible by 3 return "Fizz" 
# and if it is divisible by 5 return "buzz" 
# and if is is divisible by both return "FizzBuzz"
num= input('please enter number : ')
num = int(num)
if(num%3==0 and num%5==0):
    print('FizzBuzz')
elif(num%3==0):
    print('Fizz')    
elif(num%5==0):
    print('buzz')
else :
    print ('not vaild number')

# _________________________________________________________________________________
# Question 8
# Ask the user to enter the radius of a circle print its calculated area 
# and circumference
radius= input('please enter the radius of a circle : ')
radius=int(radius)
pi=3.14
area=pi*(radius**2)
circumference=2*pi*radius
print(f"the Area of circle={area}" )
print(f"the circumference of circle={circumference}" )

# _________________________________________________________________________________
# Question 9
# Ask the user for his name then confirm that he has entered his name (not an empty string/integers).
# then proceed to ask him for his email 
# and print all this data
name= input('please enter your name : ')
if (name == ''):
    print (' name requird')
elif any(char.isdigit() for char in name): 
    print('name contain number(only string)')
else:
    print(' sucess name ')
    email= input('please enter your email : ')
    if ('@' not in email or '.' not in email):
        print('invaild email ')
    else:
        print('++++++ your data ++++++ ')
        print (f"name : {name}")
        print (f"email :{email}")



    


