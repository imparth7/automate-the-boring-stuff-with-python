# Chapter 4: Lists

## The List Data Type
```py
nums = [1, 2, 3]
animals = ['cat', 'rat', 'elephants']
data = [1, 2, True, 'rat', False, None, 5.31]
```

### Getting Individual Values in a List with Indexes
```py
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0]
spam[1]
```

```py
spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
spam[0] # ['cat', 'bat']
spam[0][1] # 'bat'
spam[1][4] # 50
```

### Negative Indexes
```py
spam = ['cat', 'bat', 'rat', 'elephant']
spam[-1]
spam[-3]
```

### Getting Sublists with Slices
```py
spam = ['cat', 'bat', 'rat', 'elephant']
spam[0:4] # ['cat', 'bat', 'rat', 'elephant']
```

### Getting a List’s Length with len()
```py
spam = ['cat', 'dog', 'moose']
len(spam) # 3
```

### Changing Values in a List with Indexes
```py
spam = ['cat', 'bat', 'rat', 'elephant']
spam[1] = 'aardvark'
spam # ['cat', 'aardvark', 'rat', 'elephant']
```

### List Concatenation and List Replication
```py
lists = [1, 2, 3] + ['A', 'B', 'C']
lists # [1, 2, 3, 'A', 'B', 'C']
```

### Removing Values from Lists with del Statements
```py
spam = ['cat', 'bat', 'rat', 'elephant']
del spam[2]
spam # ['cat', 'bat', 'elephant']
```

## Working with Lists
```py
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation
print('The cat names are:')
for name in catNames:
    print(' ' + name)
```

## Using for Loops with Lists
```py
for i in range(4):
    print(i)
```

```py
for i in [0, 1, 2, 3]:
    print(i)
```

```py
supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])
```

## The in and not in Operators
```py
'howdy' in ['hello', 'hi', 'howdy', 'heyas']
# True
```

```py
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam
# False
```

## The Multiple Assignment Trick
```py
cat = ['fat', 'black', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
```

```py
cat = ['fat', 'black', 'loud']
size, color, disposition = cat
```

## Augmented Assignment Operators
Augmented assignment | Equivalent assignment statement
---------------------|--------------------------------
spam = spam + 1      | spam += 1
spam = spam - 1      | spam -= 1
spam = spam * 1      | spam *= 1
spam = spam / 1      | spam /= 1
spam = spam % 1      | spam %= 1

## Finding a Value in a List with the index() Method
```py
spam = ['hello', 'hi', 'howdy', 'heyas']
spam.index('hello') # 0
spam.index('heyas') # 3
```

## Adding Values to Lists with the append() and insert() Methods
```py
spam = ['cat', 'dog', 'bat']
spam.append('moose')
spam # ['cat', 'dog', 'bat', 'moose']
```

```py
spam = ['cat', 'dog', 'bat']
spam.insert(1, 'chicken')
spam # ['cat', 'chicken', 'dog', 'bat']
```

## Removing Values from Lists with remove() 
```py
spam = ['cat', 'bat', 'rat', 'elephant']
spam.remove('bat')
spam # ['cat', 'rat', 'elephant']
```

## Sorting the Values in a List with the sort() Method
```py
spam = [2, 5, 3.14, 1, -7]
spam.sort()
spam # [-7, 1, 2, 3.14, 5]

spam = ['ants', 'cats', 'dogs', 'badgers', 'elephants']
spam.sort()
spam # ['ants', 'badgers', 'cats', 'dogs', 'elephants']
```

```py
spam.sort(reverse=True)
spam # ['elephants', 'dogs', 'cats', 'badgers', 'ants']
```

```py
spam = ['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
spam.sort()
spam # ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']

spam = ['a', 'z', 'A', 'Z']
spam.sort(key=str.lower)
spam # ['a', 'A', 'z', 'Z']
```

## Magic 8 Ball with a List
```py
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
```

## List-like Types: Strings and Tuples
### String data type
```py
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
```

#### Mutable and Immutable Data Types
```py
name = 'Zophie a cat'
name[7] = 'the' # Error
```

### The Tuple Data Type
```py
eggs = ('hello', 42, 0.5)
eggs[0] # 'hello'
eggs[1:3] # (42, 0.5)
len(eggs) # 3
```

#### Mutable and Immutable Data Types
```py
eggs = ('hello', 42, 0.5)
eggs[1] = 99 # Error
```

### Data types
```py
type(('hello',)) # <class 'tuple'>
type(('hello')) # <class 'str'>
```

## Converting Types with the list() and tuple() Functions
```py
tuple(['cat', 'dog', 5]) # ('cat', 'dog', 5)
list(('cat', 'dog', 5)) # ['cat', 'dog', 5]
list('hello') # ['h', 'e', 'l', 'l', 'o']
```

## The copy Module’s copy() and deepcopy() Functions
```py
spam = [0, 1, 2, 3, 4, 5]
cheese = spam
cheese[1] = "Hello!"
spam
cheese
```

```py
import copy
spam = ['A', 'B', 'C', 'D']
cheese = copy.copy(spam)
cheese[1] = 42
spam # ['A', 'B', 'C', 'D']
cheese # ['A', 42, 'C', 'D']
```

## Practice Questions

1. What is []?
> List, empty list

2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? (Assume spam contains [2, 4, 6, 8, 10].) For the following three questions, let’s say spam contains the list ['a', 'b', 'c', 'd'].
> spam[2] = "hello"

3. What does spam[int('3' * 2) / 11] evaluate to?
> spam[3]

4. What does spam[-1] evaluate to?
> spam list last element

5. What does spam[:2] evaluate to?
> ['a', 'b']

For the following three questions, let’s say bacon contains the list [3.14, 'cat', 11, 'cat', True].

6. What does bacon.index('cat') evaluate to?
> 1

7. What does bacon.append(99) make the list value in bacon look like?
> [3.14, 'cat', 11, 'cat', True, 99]

8. What does bacon.remove('cat') make the list value in bacon look like?
> [3.14, 11, True, 99]

9. What are the operators for list concatenation and list replication?
> + for list concatenation and * for list replication

10. What is the difference between the append() and insert() list methods?
> append() Adds an element to the end of the list and insert() Adds an element at a specified index in the list.

11. What are two ways to remove values from a list?
> remove(value) Removes the first occurrence of the specified value and pop(index) Removes and returns the element at the specified index (or the last element if no index is provided).

12. Name a few ways that list values are similar to string values.
> Both can be indexed and sliced, iterated over (using loops) and concatenated and replicated using + and *.

13. What is the difference between lists and tuples?
> Lists Mutable (can be changed after creation) and Tuples Immutable (cannot be changed after creation).

14. How do you type the tuple value that has just the integer value 42 in it?
> (42, )

15. How can you get the tuple form of a list value? How can you get the list form of a tuple value?
> tuple(list_value) and list(tuple_value)

16. Variables that “contain” list values don’t actually contain lists directly. What do they contain instead?
> They contain references to the list objects in memory.

17. What is the difference between copy.copy() and copy.deepcopy()?
> copy.copy(): Creates a shallow copy of the object; it copies the object but not the nested objects (references are maintained).\
> copy.deepcopy(): Creates a deep copy of the object; it copies the object and all nested objects, creating entirely independent copies.