# The Dictionary Data Type
myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}

spam = {12345: 'Luggage Combination', 42: 'The Answer'}

# Dictionaries vs. Lists



birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthdays:
        print(f"{birthdays[name]} is the birthday of {name}")
    else:
        print(f"I do not have birthday information for {name}")
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')


picnicItems = {'apples': 5, 'cups': 2}
'I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.' # 'I am bringing 2 cups.'
'I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.' # 'I am bringing 0 eggs.'

spam = {'name': 'Pooka', 'age': 5}
spam.setdefault('color', 'black') # 'black'
spam # {'color': 'black', 'age': 5, 'name': 'Pooka'}
spam.setdefault('color', 'white') # 'black'
spam # {'color': 'black', 'age': 5, 'name': 'Pooka'}

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)



import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)