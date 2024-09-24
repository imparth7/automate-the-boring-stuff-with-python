# Chapter 3: Functions

## def Statements with Parameters
```py
def hello():
    print("Hello world")

hello()
```

## Return Values and return Statements
```py
import random
def randomNum():
    return random.randint(1, 10)

randomNum()
```

## The None Value
```py
spam = None
```

## Keyword Arguments and print()
```py
print("Hello", "World", sep=", ", end=".")
```

## Local and Global Scope
### Local Variables Cannot Be Used in the Global Scope
```py
def hello():
    num = 10

hello()
# print(num) # Error: num cannot access outside the function
```

### Local Scopes Cannot Use Variables in Other Local Scopes
```py
def hello():
    num = 10
    world()

def world():
    print(num) # Error: num cannot access in other function scope

hello()
```

### Global Variables Can Be Read from a Local Scope
```py
def hello():
    print(num)

num = 10
hello()
```

### Local and Global Variables with the Same Name
```py
def spam():
    eggs = 'spam local'
    print(eggs) # prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'
eggs = 'global'
bacon()
print(eggs) # prints 'global'
```

### The global Statement
```py
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)
```

If you ever want to modify the value stored in a global variable from in a function, you must use a global statement on that variable.

## Exception Handling
```py
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(12))
print(spam(0))
```

## Practice Questions

1. Why are functions advantageous to have in your programs?
> Functions promote code reusability, improve readability, and simplify debugging in programs.

2. When does the code in a function execute: when the function is defined or when the function is called?
> The code in a function executes when the function is called.

3. What statement creates a function?
> `def` statement creates a function in Python.

4. What is the difference between a function and a function call?
> A function is a block of reusable code defined to perform a specific task, while a function call is the execution of that function.

5. How many global scopes are there in a Python program? How many local scopes?
> In a Python program, there is typically one global scope and multiple local scopes (one for each function or block of code).

6. What happens to variables in a local scope when the function call returns?
> When a function call returns, variables in the local scope are destroyed and no longer accessible.

7. What is a return value? Can a return value be part of an expression?
> A return value is the output value that a function sends back when it completes; yes, a return value can be part of an expression.

8. If a function does not have a return statement, what is the return value of a call to that function?
> If a function does not have a return statement, the return value of a call to that function is `None`.

9. How can you force a variable in a function to refer to the global variable?
> The `global` keyword within the function to force a variable to refer to the global variable.

10. What is the data type of None?
> The data type of `None` is `NoneType`.

11. What does the import areallyourpetsnamederic statement do?
> The statement `import areallyourpetsnamederic` imports the module named `areallyourpetsnamederic`, allowing you to use its functions and classes in your program.

12. If you had a function named bacon() in a module named spam, how would you call it after importing spam?
> Call it using `spam.bacon()`.

13. How can you prevent a program from crashing when it gets an error?
> A program from crashing by using try-except blocks to handle exceptions.

14. What goes in the try clause? What goes in the except clause?
> In the try clause, you place the code that might raise an exception, and in the except clause, you handle the potential exception that may occur.