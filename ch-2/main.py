# Boolean
True
False

# Comperison Operator
# ==
# !=
# >
# <
# >=
# <=

# Boolean Operators
## Binary Boolean Operators
True and True
True and False
False and False
False and True

True or True
True or False
False or False
False or True

## not Operator
not True
not False
not not True

# Mixing Boolean and Comparison Operators
print((4 > 5) and (5 > 3))

# Flow Control
if True:
    print(True)

if 4 > 5:
    print(False)
else:
    print(True)
    
if 0 > 1:
    print(0)
elif 1 > 0:
    print(1)
else:
    print("equal")
    

# Loop Statements
## while loop
i = 0
while i < 5:
    print(i)
    i = i + 1
    
i = 0
while True:
    print(i)
    i = i + 1
    if i == 5:
        continue
    if i > 10:
        break
    
    
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password == 'swordfish':
        print('Access granted.')
        break
    
    
## for loop
sum = 0
for num in range(10):
    sum = sum + num
print(sum)

for i in range(0, 10, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)

import random
for i in range(5):
    print(random.randint(1, 10))


# Ending a Program Early with sys.exit()
import sys
while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')