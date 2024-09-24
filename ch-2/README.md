# Chapter 2: Flow Control

## Boolean
True
False

## Comperison Operator
==, !=, >, <, >=, <=

## Boolean Operators
### Binary Boolean Operators
True and True
True and False
False and False
False and True

True or True
True or False
False or False
False or True

### not Operator
not True
not False
not not True

## Flow Control
```py
if condition:
    first statement
elif condition:
    second statement
else:
    default statement
```

## Loop Statements
### while loop
```py
while condition:
    statements
```

### for loop
```py
for item in list/range(start, end, step):
    statements
```

## Ending a Program Early with sys.exit()
```py
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
```


## Practice Questions

1. What are the two values of the Boolean data type? How do you write them?
> True and False

2. What are the three Boolean operators?
> and, or, not

3. Write out the truth tables of each Boolean operator (that is, every possible combination of Boolean values for the operator and what they evaluate to).
> and
> A     | B     | A and B
> ------|-------|--------
> True  | True  | True
> True  | False | False
> False | False | False
> False | True  | False

> or
> A     | B     | A or B
> ------|-------|-------
> True  | True  | True
> True  | False | True
> False | False | False
> False | True  | True

> not
> A     | not A
> ------|-------
> True  | False
> False | True

4. What do the following expressions evaluate to?
(5 > 4) and (3 == 5)
> False

not (5 > 4)
> False

(5 > 4) or (3 == 5)
> True

not ((5 > 4) or (3 == 5))
> False

(True and True) and (True == False)
> False

(not False) or (not True)
> True

5. What are the six comparison operators?
> ==, !=, >, <, >=, <=

6. What is the difference between the equal to operator and the assignment operator?
> equal to (==) check equalization of both values and Assignment operator (=) is Assign the value to variable.

7. Explain what a condition is and where you would use one.
> Condition is expression that evaluates and return True or False

8. Identify the three blocks in this code:
> ```py
> spam = 0 # global assignment
> if spam == 10: # outer if block
>     print('eggs') # outer block statement
>     if spam > 5: # inner if block
>         print('bacon') # inner if block statement
>     else: # inner else block
>         print('ham') # inner else block statement
>     print('spam') # outer block statement
> print('spam') # global statement
> ```

9. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, and prints Greetings! if anything else is stored in spam.
> ```py
> spam = 2
> if spam == 1:
>     print("Hello")
> elif spam == 2:
>     print("Howdy")
> else:
>     print("Greetings!")
> ```

10. What can you press if your program is stuck in an infinite loop?
> Ctrl + C

11. What is the difference between break and continue?
> Break is terminate entire loop and Continue is skip one iteration of the loop.

12. What is the difference between range(10), range(0, 10), and range(0, 10, 1) in a for loop?
> range(10) -> 0 to 9
> range(0, 10) -> 0 to 9 but in this specifing the starting point
> range(0, 10, 1) -> 0 to 9 but in this stating and steps are define.

13. Write a short program that prints the numbers 1 to 10 using a for loop. Then write an equivalent program that prints the numbers 1 to 10 using a while loop.
> ```py
> for i in range(1, 11):
>    print(i)
> ```

> ```py
> i = 1
> while i <= 10:
>    print(i)
>    i += 1

14. If you had a function named bacon() inside a module named spam, how would you call it after importing spam?
> Importing Just the Function:
>> from spam import bacon\
>> bacon()

>Calling the Function
>> import spam\
>> spam.bacon()