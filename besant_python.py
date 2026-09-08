'''
a= int(input("enter number1 :"))
b= int(input("enter number2 :"))
print("addition ", a + b )
print("addition ", a - b )
print("addition ", a * b )
'''
'''
A="Python program"
print(A[0:6])
print(A[2:10])
print(A[10::])
'''
Q="Python "
print(Q* 4)

'''
for i in range(1, 5):
    print("*" * i)
'''
'''
print("   *   ")
print("  **  ")
print("*** ")
print("****")
'''
'''
#operators
a = int(input("enter1:"))
b = int(input("enter2:"))
c= a+b
print("value:",c)
'''
'''
a = input("enter your name:")
print("your name:",a)
print(type(a))
'''
'''
name=input("enter1:")
age=int(input("enter1:"))
print("Name:",name,"\n Age:",age)
'''
'''
a= 30
b=2
print(a+b,"\n",a-b,"\n",a*b,"\n",a/b,"\n",a//b,"\n",a%b)
'''
'''
#logical operator
age=23
print(age>18 and age<30)
print(age>18 or age >30)
condition=True
print(not condition)
print(type(condition))
'''

#if else
#syntac
'''
if (condition):
    satement1
else:
    satement2 


age = int(input("enter age:"))
if age >= 18:
    print("you are eligible")
else:
    print("you are not eligible")


age = int(input("enter age:"))
if age >= 18:
    print("you are eligible")
elif age<1:
    print("wrong value")
else:
    print("you are not eligible")


attendance =int(input("enter the attendance:"))
mark =int(input("enter the mark:"))
if attendance >=75:
    print("attendance is ok")
    if mark >=50:
        print("you are eligible to write exam")
    else:
        print("not eligible to write the exam due to less marks")
else:
    print("you are not eligible to write the exam due to less attendance")

'''
'''
#loop
#while loop

syntax
intialization 
while <condition>:
    statement
    increment


count=0
while count<=9:
    print(count)
    count+=1

count=0

while count<=9:
    print(count,end=" ")
    count+=1
  
#fro loop

for variable in sequence:
    statement

print(" ")
for i in range(1,10,1):
    print(i)


for i in range (2,11):
    print(i,end=",")

print(end="\n")
a= 5
for i in range(0,a+1):
    print(i, end=",")
print(end="\n")

for i in range(1,11):
    if i%2==0:
        print(i)
'''
#1. print the number greather than 10 sequence upto 20
#2. print the odd numbers 1 to 20

for i in range (11,21):
    print(i)

for i in range (1,20,2):
    print(i,end=" ")

print()
#Q4. Square of a Number
def square(n):
  return n**2

a=int(input("Enter a number:"))
print(square(a))