# Q1- Why do we call Python as a general purpose and high-level programming language?
#Answer--> Beacause it can be used to create a variety of different programs and is not specialized for any specific problems.
#  This versatility, along with its beginner-friendliness,
#  has made it one of the most-used programming languages today.
#It is high level programming language beacause it is easy to use, read, write and learn.


#Q2- Why is Python called a dynamically typed language?
# Answer--> Because  We don't have to declare the type of variable while assigning a value to a variable in Python.
# Other languages like C, C++, Java, etc.., there is a strict declaration of variables before assigning values to them.


#Q3- List some pros and cons of Python programming language?
#Answer-->          pros
#  1. Python is easy to learn and read.
# 2. Python has a vast collection of libraries.
# 3. Python is free, open-source, and has a vibrant community.
# 4. Python is an interpreted language.
# 5. Python is a portable programming language.

#                   cons
# 1. Python has speed limitations.
# 2. Python is not easy to test.
# 3. Python can have runtime errors.


#Q4-  In what all domains can we use Python?
# Answer--> Big Data
# Data Science and Machine Learning
# Data analytics and data visualization 
# Web development
# Game development
# Mobile app development


#Q5- What are variable and how can we declare them?
# Answer--> A variable is a reserved memory area(memory address) to store values.
# A variable name should be Start with a alphabetic character or a underscore.
#  We can't use special symbol in it.
# Python has no command for declaring a variable.
#  Thus, declaring a variable in Python is very simple-

# Just name the variable.
# Assign the required value to it.
# The data type of the variable will be automatically
# determined from the value assigned, we need not define it explicitly.


# Q6-  How can we take an input from the user in Python?
#Answer-->  The input() function is used to take the input from the user.
# It first takes the input from the user and converts it into a string.
#Example-
name = input("Enter username:")
print("Name is: " + name)


# Q7- What is the default datatype of the value that has been taken as an input using input() function?
# Answer--> String datatype is the default datatype of the value that has been taken as an input using input() function​.


# Q8- What is type casting?
# Answer--> The method to convert the variable data type into a certain data type in order to the operation required 
# to be performed by users is called type casting.


# Q9- Can we take more than one input from the user using single input() function? If yes, how? If no, why?
# Answer--> Yes, we take more than one input or multiple input from the user using single input() function.

x = input("Enter First Name: ")
y = input("Enter Last Name: ") 
print("First Name is: ", x) 
print("Second Name is: ", y)


# Q10- What are keywords?
# Answer--> Keywords are predefined, reserved words used in Python programming that have special meanings to the compiler.
# We cannot use a keyword as a variable name, function name, or any other identifier.
# They are used to define the syntax and structure of the Python language.


#Q11- Can we use keywords as a variable? Support your answer with reason.
# Answer--> No, can't use keywords as a variable beacause the key words are the reserved words.
# They are used to define the syntax and structure of the Python language.

# Q12- What is indentation? What's the use of indentation in Python?
# Answer--> Indentation refers to the spaces at the beginning of a code line.
# Indentation is a very important concept of Python because without properly indenting the Python code,
# you will end up seeing IndentationError and the code will not get compiled.
# Python uses indentation to indicate a block of code.


# Q13- How can we throw some output in Python?
# Answer--> We can use print statement to throw some output.


#Q14- What are operators in Python?
# Answer--> Operators are special symbols that perform specific operation on one or more operands
# and return the results.
# There are many types-
# 1. Arthimetic operators--> ( +, -, *, /, //, **, % )
# 2. Comparison operators-->  ( >,<,=,>=,<=,!= )
# 3. Assignment operator-->  (+=, =, -=, *=, /=, %=... ) 
# 4. Logical operator-->  (and, or, not )


#Q15- What is difference between / and // operators?
# Answer--> / is used for normal division or float division.
# and // is used for integer division or floor division.


#Q16- Write a code that gives following as an output
''' iNeuroniNeuroniNeuroniNeuron '''
# Answer--> 

name02 = "iNeuron" * 4
print("string =", name02) 


# Q17-  Write a code to take a number as an input from the user and check if the number is odd or even.
# Answer-->  
digit = int(input("Enter the Number = "))

if (digit % 2) == 0:
    print("The Number is even")
else: print("The number is odd")



# Q18-   What are boolean operator?
# Answer--> The logical operators and, or and not are also referred to as boolean operators.
# While and as well as or operator needs two operands, which may evaluate to true or false,
# not operator needs one operand evaluating to true or false.

#Example -
# Boolean and operator returns true if both operands return true.
#  a=50
#  b=25
#  a>40 and b>40
#  False

#  a>0 and b>0
#  True

# Boolean or operator returns true if any one operand is true.
#  a=50
#  b=25
#  a>40 or b>40
#  True

# a==0 or b==0
# False

# The not operator returns true if its operand is a false expression and returns false if it is true.
#  a=10
#  a>10
#  False
#  not(a>10)
#  True
    

# Q19-  What will the output of the following?
'''
1 or 0

0 and 0                    

True and False and True

1 or 0 or 0

'''
#Answer--> 
a = 1 or 0

b = 0 and 0                    

c = True and False and True

d = 1 or 0 or 0
print(a)
print(b)
print(c)
print(d)



# Q20- What are conditional statements in Python?
# Answer-->  Conditional statements are also called decision-making statements.
# We use those statements while we want to execute a block of code when the given condition is true or false.
 
# Type of condition statement in Python:
# If statement.
# If Else statement.
# Elif statement.                                   
# Nested if statement.
# Nested if else statement.


# Q21- What is use of 'if', 'elif' and 'else' keywords?
# Answer--> if statement --
# If the condition following the keyword if evaluates as true, the block of code will execute.

x = 5

if x > 4:
  print("The condition was true!") #this statement executes

# else statement --
# You can optionally add an else response that will execute if the condition is false:  

y = 3

if y > 4:
  print("I won't print!") #this statement does not execute
else:
  print("The condition wasn't true!") #this statement executes

# elif statement
# Multiple conditions can be checked by including one or more elif checks after your initial if statement.
# Just keep in mind that only one condition will execute:  

z = 7

if z > 8:
  print("I won't print!") #this statement does not execute
elif z > 5:
  print("I will!") #this statement will execute
elif z > 6:
  print("I also won't print!") #this statement does not execute
else:
  print("Neither will I!") #this statement does not execute


# Q22-  Write a code to take the age of person as an input and if age >= 18 display "I can vote".
# If age is < 18 display "I can't vote".

Age = int(input("Enter the Age = "))
if Age >= 18:
    print("I can vote")
else:print("I can't vote")


# Q23- Q23. Write a code that displays the sum of all the even numbers from the given list.
numbers = [12, 75, 150, 180, 145, 525, 50]

# Answer-->  
numbers = [12, 75, 150, 180, 145, 525, 50]

# iterating each number in list
for num in numbers:

	# checking condition
	if num % 2 == 0:
		print(num, end=" ")

# Q24- Write a code to take 3 numbers as an input from the user and display the greatest no as output.
# Answer--> 
num1 = int(input("Enter the First Number = "))
num2 = int(input("Enter the Second Number = "))
num3 = int(input("Enter the Third Number = "))

if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)

#Q25. Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five

# If the number is greater than 150, then skip it and move to the next number

# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]
# Answer--> 
multiple =print(list(filter(lambda numbers:numbers%5==0,[12, 75, 150, 180, 145, 525, 50])))

