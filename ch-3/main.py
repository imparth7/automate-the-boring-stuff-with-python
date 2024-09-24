# def Statements with Parameters
def hello():
    print("Hello world")

hello()

# Return Values and return Statements
import random
def randomNum():
    return random.randint(1, 10)

randomNum()

spam = None
print(spam == None)


print('Hello')
print('World')

print('Hello', end=' ')
print('World')

print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=', ')

print("Hello", "World", sep=", ", end=".")


# Local Variables Cannot Be Used in the Global Scope
def hello():
    num = 10

hello()
# print(num) # Error: num cannot access outside the function

# Local Scopes Cannot Use Variables in Other Local Scopes
def hello():
    num = 10
    world()

def world():
    # print(num) # Error: num cannot access in other function scope
    print("World function")

hello()

# Global Variables Can Be Read from a Local Scope
def hello():
    print(num)

num = 10
hello()

# Local and Global Variables with the Same Name
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

# The global Statement
def spam():
    global eggs
    eggs = 'spam'
eggs = 'global'
spam()
print(eggs)

# without global
def spam():
    print(eggs) # ERROR!
    eggs = 'spam local'

eggs = 'global'
spam()


# Exception Handling
def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(12))
print(spam(0))



## A Short Program: Guess the Number
# This is a guess the number game.
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is the correct guess!
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))