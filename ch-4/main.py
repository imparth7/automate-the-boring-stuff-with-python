# The List Data Type
nums = [1, 2, 3]
animals = ["cat", "rat", "elephants"]
data = [1, 2, True, "rat", False, None, 5.31]

# Getting Individual Values in a List with Indexes
spam = ["cat", "bat", "rat", "elephant"]
spam[0]
spam[1]

spam = [["cat", "bat"], [10, 20, 30, 40, 50]]
spam[0]  # ['cat', 'bat']
spam[0][1]  # 'bat'
spam[1][4]  # 50

# Negative Indexes
spam = ["cat", "bat", "rat", "elephant"]
spam[-1]
spam[-3]

# Getting Sublists with Slices
spam = ["cat", "bat", "rat", "elephant"]
spam[0:4]  # ['cat', 'bat', 'rat', 'elephant']

# Getting a List’s Length with len()
spam = ["cat", "dog", "moose"]
len(spam)  # 3

# Changing Values in a List with Indexes
spam = ["cat", "bat", "rat", "elephant"]
spam[1] = "aardvark"
spam  # ['cat', 'aardvark', 'rat', 'elephant']

# List Concatenation and List Replication
lists = [1, 2, 3] + ["A", "B", "C"]
lists  # [1, 2, 3, 'A', 'B', 'C']

# Removing Values from Lists with del Statements
spam = ["cat", "bat", "rat", "elephant"]
del spam[2]
spam  # ['cat', 'bat', 'elephant']

# Working with Lists
catNames = []
while True:
    print(
        "Enter the name of cat "
        + str(len(catNames) + 1)
        + " (Or enter nothing to stop.):"
    )
    name = input()
    if name == "":
        break
    catNames = catNames + [name]  # list concatenation
print("The cat names are:")
for name in catNames:
    print(" " + name)


# Using for Loops with Lists
supplies = ["pens", "staplers", "flame-throwers", "binders"]
for i in range(len(supplies)):
    print("Index " + str(i) + " in supplies is: " + supplies[i])

# The in and not in Operators
"howdy" in ["hello", "hi", "howdy", "heyas"]

spam = ["hello", "hi", "howdy", "heyas"]
"cat" in spam


myPets = ["Zophie", "Pooka", "Fat-tail"]
print("Enter a pet name:")
name = input()
if name not in myPets:
    print("I do not have a pet named " + name)
else:
    print(name + " is my pet.")


# The Multiple Assignment Trick
cat = ["fat", "black", "loud"]
size = cat[0]
color = cat[1]
disposition = cat[2]

cat = ["fat", "black", "loud"]
size, color, disposition = cat

# Finding a Value in a List with the index() Method
spam = ["hello", "hi", "howdy", "heyas"]
spam.index("hello")  # 0
spam.index("heyas")  # 3

# Adding Values to Lists with the append() and insert() Methods
spam = ["cat", "dog", "bat"]
spam.append("moose")
spam  # ['cat', 'dog', 'bat', 'moose']

spam = ["cat", "dog", "bat"]
spam.insert(1, "chicken")
spam  # ['cat', 'chicken', 'dog', 'bat']

# Removing Values from Lists with remove()
spam = ["cat", "bat", "rat", "elephant"]
spam.remove("bat")
spam  # ['cat', 'rat', 'elephant']

# Sorting the Values in a List with the sort() Method
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam  # [-7, 1, 2, 3.14, 5]

spam = ["ants", "cats", "dogs", "badgers", "elephants"]
spam.sort()
spam  # ['ants', 'badgers', 'cats', 'dogs', 'elephants']

spam.sort(reverse=True)
spam  # ['elephants', 'dogs', 'cats', 'badgers', 'ants']

spam = ["Alice", "ants", "Bob", "badgers", "Carol", "cats"]
spam.sort()
spam  # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

spam = ["a", "z", "A", "Z"]
spam.sort(key=str.lower)
spam  # ['a', 'A', 'z', 'Z']


# Magic 8 Ball with a List
import random

messages = [
    "It is certain",
    "It is decidedly so",
    "Yes definitely",
    "Reply hazy try again",
    "Ask again later",
    "Concentrate and ask again",
    "My reply is no",
    "Outlook not so good",
    "Very doubtful",
]
print(messages[random.randint(0, len(messages) - 1)])




name = 'Zophie'
name[0] # 'Z'
name[-2] # 'i'
name[0:4] # 'Zoph'
'Zo' in name # True
'z' in name # False
'p' not in name # False
for i in name:
    print('* * * ' + i + ' * * *')
'''
* * * Z * * *
* * * o * * *
* * * p * * *
* * * h * * *
* * * i * * *
* * * e * * *
'''

# Mutable and Immutable Data Types
name = 'Zophie a cat'
name[7] = 'the' # Error




# Tuple
eggs = ('hello', 42, 0.5)
eggs[0] # 'hello'
eggs[1:3] # (42, 0.5)
len(eggs) # 3

# Mutable and Immutable Data Types
eggs = ('hello', 42, 0.5)
eggs[1] = 99 # Error



type(('hello',)) # <class 'tuple'>
type(('hello')) # <class 'str'>

tuple(['cat', 'dog', 5]) # ('cat', 'dog', 5)
list(('cat', 'dog', 5)) # ['cat', 'dog', 5]
list('hello') # ['h', 'e', 'l', 'l', 'o']




spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello!"
spam
cheese



## Practice Projects
## 1: Comma Code
def comma_code(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return ' and '.join(items)
    else:
        return ', '.join(items[:-1]) + ', and ' + items[-1]

# Example usage
spam = ['apples', 'bananas', 'tofu', 'cats']
result = comma_code(spam)
print(result)  # Output: apples, bananas, tofu, and cats

## 2: Character Picture Grid
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

for y in range(len(grid[0])):
    for x in range(len(grid)):
        print(grid[x][y], end='')
    print()
