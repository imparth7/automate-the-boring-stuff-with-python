# Chapter 5: Dictionaries and Structuring Data

## The Dictionary Data Type
```py
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
myCat['size'] # 'fat'
```

## Dictionaries vs. Lists
```py
spam = ['cats', 'dogs', 'moose']
bacon = ['dogs', 'moose', 'cats']
spam == bacon # False

eggs = {'name': 'Zophie', 'species': 'cat', 'age': '8'}
ham = {'species': 'cat', 'age': '8', 'name': 'Zophie'}
eggs == ham # True
```

## The keys(), values(), and items() Methods
```py
spam = {'color': 'red', 'age': 42}

for k in spam.keys():
    print(k)
# color, age

for v in spam.values():
    print(v)
# red, 42

for i in spam.items():
    print(i)
# ('color', 'red'), ('age', 42)

for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + str(v))
# Key: age Value: 42, Key: color Value: red
```

## Checking Whether a Key or Value Exists in a Dictionary
```py
spam = {'name': 'Zophie', 'age': 7}
'name' in spam.keys() # True
'Zophie' in spam.values() # True
'color' in spam.keys() # False
'color' not in spam.keys() # True
'color' in spam # False
```

## The get() Method
```py
picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.' # 'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' # 'I am bringing 0 eggs.'
```

## The setdefault() Method
```py
spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black') # 'black'
spam # {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white') # 'black'
spam # {'color': 'black', 'age': 5, 'name': 'Pooka'}
```

## Pretty Printing
```py
import pprint
message = 'It was a bright cold day in April, and the clocks were striking
thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)
```

## Using Data Structures to Model Real-World Things

### A Tic-Tac-Toe Board
```py
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}
```


## Practice Questions

1. What does the code for an empty dictionary look like?
> empty_dict = {}, empty_dict = dict()

2. What does a dictionary value with a key 'foo' and a value 42 look like?
> my_dict = {'name': 'Ram'}

3. What is the main difference between a dictionary and a list?
> A dictionary stores key-value pairs for fast access by keys, while a list stores ordered items accessed by their index.

4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
> If you try to access `spam['foo']` when `spam` is `{'bar': 100}`, you will get a `KeyError` because the key `'foo'` does not exist in the dictionary.

5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?
> Both expressions, 'cat' in spam and 'cat' in spam.keys(), check for the presence of the key 'cat' in the dictionary spam.

6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?
> 'cat' in spam checks for the key 'cat', while 'cat' in spam.values() checks for the value 'cat'.

7. What is a shortcut for the following code? 
if 'color' not in spam:
    spam['color'] = 'black'
> spam.setdefault('color', 'black')

8. What module and function can be used to “pretty print” dictionary values?
> ```py
> import pprint
> pprint.pprint(your_dict)
> ```