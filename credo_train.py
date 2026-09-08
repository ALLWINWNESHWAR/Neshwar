'''
#print statement
print("allwin","\ngopal","balaji",)
# end argument and separation argument
print("Hi","Hi", end='...', sep='...')
'''
'''
#Escape sequence
print("Escape\nsequence")           
print("Escape\t\tsequence")
print("Escape\nsequence")
print('This is Allwin\'s phone')  ,  print("This is Allwin's phone")
print("This is a backslash:\\")

print("'Is's Hero Time!\n \t\t-Ben10")
'''
'''
#Data types -- int, str, float, bool
name= "allwin"
age = 23
salary = 17000.5
virgin= True
print(type(name))
print(type(age))
print(type(salary)) 
print(type(virgin))
'''
'''
#Dynamic Typing
name= "allwin"
print(type(name))
name= 23        
print(type(name))
'''
'''
#string is a IMMUTABLE 
#arithematice operators
print(10+5*3) #BODMAS RULE
print(20-10/5*2)
print(2*3**(2%10))

# comparision operator or relational operator
# to find the asci valu
print("asci valu of S:", ord("S"))

#membership operator
list1=[1,2,3,4,5]
print(4 in list1)
print(6 not in list1)

#bitwise operator
a=2
b=3
print(a<<1)     #Left shift 
print(b>>1)     #Right shift 
print( a & b)  # bitwise AND 
print(a | b)    # bitwise OR
print(a^b)     # bitwise NOT

#string replication
q="allwin "
print(q*1000)
#string concatination
w=" w neshwar"
print("concatination:",q+w)
'''
'''
#user to get input
num=int(input("enter number:"))
num2=float(input("enter decimal number:"))

#average of numbers
m1=float(input("enter mark 1:"))
m2=float(input("enter mark 2:"))
m3=float(input("enter mark 3:"))
total=m1+m2+m3
average =(total/3)
print("total mark=",total)
print("Average mark=",average)
'''
'''
#unit degit
#this one is string
a=input("enter:" )
print(a[len(a) - 1])
#this one is number
b=int(input("enter number:"))
print(b%10)
#if you want tenth digit
num=int(input("enter to find tenth digit number:"))
num=num//10
print(num%10)
'''

#type of statements
# 1.simple statements
# 2.compund statements --(conditional statements)
# 3.Empty statements -- (pass,break,continue)
'''
#conditional statement syntax
if (condition):
    statement

if (condition):
    statement
else:
    statement

if (condition):
    statement
elif (condition):
    statement
elif (condition):
    statement
else:
    statement
'''

x=5
y=10
if x>y:
    largest=x
else:
    largest=y
print(largest)

#Ternary operator
age=int(input("enter the age:"))
print("child" if (age<18) else "adult")

