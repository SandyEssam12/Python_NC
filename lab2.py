# Question 1 
# Write a simple calculator program using match 
# to perform addition, subtraction, multiplication, and division.
# operation = "add"
# a, b = 10, 5
print('Calculator program \n \
      1-addition\n \
      2-subtraction\n \
      3-multiplication\n \
      4-division')
num=input('Choose number of operation : ')
a=int(input('Enter the fisrt number of operation : '))
b=int(input('Enter the second number of operation : '))
# a=10
# b=5
match num:
    case '1':
        add=a+b
        print (f"the addition result : {add}")
    case '2':
        sub=a-b
        print (f"the subtraction result : {sub}")
    case '3':
        mul=a*b
        print (f"the multiplication result : {mul}")    
    case '4':
        div=a/b
        print (f"the division result : {div}")
    case _:
        print('no exist operation for this choose')

# _________________________________________________________________________________
# Question 2 
# Write a program to filter out even numbers from a list 
# and count how many are left.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count=0
odd_num=[]
for item in numbers:
    if(item %2 !=0):
        count+=1
        odd_num.append(item)
print (odd_num)
print (f"count of even number : {count}")
print (f"count of odd number : {len(odd_num)}")

# _________________________________________________________________________________
# Question 3 
# Write a program to check if a password meets the following criteria:
# - At least 8 characters long.
# - Contains at least one uppercase letter.
# - Contains at least one digit.
# password = "Pass1234"
# # Expected Output: "Valid Password"

password=input('enter password : ')
match password:
    case password if len(password)<8:
        print('invalid : At least 8 characters long')
    case paasword if not any(i.isupper() for i in password):  
        print('invalid : at least one uppercase letter')
    case paasword if not any(i.isdigit() for i in password): 
        print('invalid : at least one digit')
    case _:
        print('vaild password')
        
# _________________________________________________________________________________
# Question 4
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
print(dic1|dic2|dic3)

# _________________________________________________________________________________
# Question 5
# takes a string and prints the longest alphabetical ordered substring occured.
# For example, if the string is 'abdulrahman' then the output is:
# Longest substring in alphabetical order is: abdu
string='abdulrahman'
curr_sub=string[0]
long_sub=string[0]

for i in range(len(string)-1):
    if ord(string[i])<=ord(string[i+1]):
        curr_sub += string[i + 1]
        if len(curr_sub)>len(long_sub):
            long_sub=curr_sub
    else:
        curr_sub=string[i+1]
print(f"Longest substring in alphabetical order is : {long_sub}")

# _________________________________________________________________________________
# # Question 6
# # Write a program to check if a Email meets the following criteria:
# # - Ensures the email follows a standard format (e.g., local@domain.com).
# # - Does not check if the email actually exists or is deliverable.
email=input('Enter your email : ').lower()
if '@' in email and '.' in email.split('@')[-1]:
    print('vaild email')
    print(email)
else :
    print('invaild email')







