# Chapter 1: Python Basics

## Operator Precedence Table
| Precedence Level | Operator(s)        | Description                                          | Example          |
|------------------|--------------------|------------------------------------------------------|------------------|
| 1                | `**`               | Exponentiation                                       | `2 ** 3` → `8`   |
| 2                | `+`, `-` (unary)   | Unary plus and minus                                 | `-5` or `+5`     |
| 3                | `*`, `/`, `//`, `%`| Multiplication, Division, Floor Division, Modulus   | `10 / 2` → `5.0` |
| 4                | `+`, `-`           | Addition and Subtraction                             | `5 + 3` → `8`    |
| 5                | `<<`, `>>`         | Bitwise Shift Operators                              | `1 << 2` → `4`   |
| 6                | `&`                | Bitwise AND                                         | `5 & 3` → `1`    |
| 7                | `^`                | Bitwise XOR                                         | `5 ^ 3` → `6`    |
| 8                | `|`                | Bitwise OR                                          | `5 | 3` → `7`    |
| 9                | `<`, `<=`, `>`, `>=`, `==`, `!=` | Comparison Operators                     | `5 < 3` → `False`|
| 10               | `is`, `is not`     | Identity Operators                                   | `x is y`         |
| 11               | `in`, `not in`     | Membership Operators                                 | `5 in [1, 2, 3, 5]` → `True` |
| 12               | `not`              | Logical NOT                                         | `not True` → `False` |
| 13               | `and`              | Logical AND                                         | `True and False` → `False` |
| 14               | `or`               | Logical OR                                          | `True or False` → `True`  |


## Data type
```py
int1 = 10
float1 = 3.14
str1 = "Hello world"
```


## Variable Names
1. It can be only one word.
2. It can use only letters, numbers, and the underscore (_) character.
3. It can’t begin with a number.

### Valid name
balance, currentBalance, current_balance, _spam, SPAM, account4

### Invalid name
current-balance (hyphens are not allowed)\
current balance (spaces are not allowed)\
4account (can’t begin with a number)\
42 (can’t begin with a number)\
total_$um (special characters like $ are not allowed)\
'hello' (special characters like ' are not allowed)


## Practice Questions

1. Which of the following are operators, and which are values?
> operators: *, -, /, +
> values: -88.8, 'hello', 5

2. Which of the following is a variable, and which is a string?
> spam => Variable, 'spam' => Value

3. Name three data types.
> int, float, str

4. What is an expression made up of? What do all expressions do?
> expression is combination of values, variables, operators, and function calls, expression evaluate the value.

5. This chapter introduced assignment statements, like spam = 10. What is the difference between an expression and a statement?
> expression evaluate the values and statement performa an action.

6. What does the variable bacon contain after the following code runs?
bacon = 20
bacon + 1
> 20

7. What should the following two expressions evaluate to?
'spam' + 'spamspam'
'spam' * 3
> 'spamspamspam'

8. Why is eggs a valid variable name while 100 is invalid?
> 100 is number and variable name never start with the number, and the eggs have all alphabets show it is valid.

9. What three functions can be used to get the integer, floating-point number, or string version of a value?
> int(), float(), str()

10. Why does this expression cause an error? How can you fix it?
'I have eaten ' + 99 + ' burritos.'
> In this expression 99 is number means integer and integer cannot concate with the string, so need to convert 99 to str(99) for the result.