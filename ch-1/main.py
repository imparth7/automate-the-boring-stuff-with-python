# Data type
int1 = 10
float1 = 3.14
str1 = "Hello world"

print("A" + "B")
# print("A" + 10) # Error
print("A" * 5) # "AAAAA"
# print("A" * "B") # Error


# First Program
print("Hello world!")
print("What is your name?")
name = input()
print("It is good to meet you, " + name)
print("Your name length is:", len(name))
print("What is your age?")
age = input()
print("You will be " + str(int(age)+1) + " in a year.")