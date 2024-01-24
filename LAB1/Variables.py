#Examples

#===Python variables===
x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x))
print(type(y))

x = "John"
# is the same as
x = 'John'

a = 4
A = "Sally"
#A will not overwrite a

#===Variable names===

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#2myvar = "John"
#my-var = "John"  Mistake
#my var = "John"

myVariableName = "John" #Camel case
MyVariableName = "John" #Pascal case
my_variable_name = "John" #Snake case

#===Assign multiple values===

#Many Values to Multiple Variables
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#===Output variables===

x = "Python is awesome"
print(x)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

#x = 5
#y = "John"    Mistake
#print(x + y)

x = 5
y = "John"
print(x, y)

#===Global variables===

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()



def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)



def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Variable exercises

#1 
carname = "Volvo"

#2
x = 50

#3
x = 5
y = 10
print(x + y)

#4
x = 5
y = 10
z = x + y
print(z)

#5
x,y,z = "Orange", "Banana", "Cherry"

#6
x = y = z = "Orange"

#7
def myfunc():
  global x
  x = "fantastic"







