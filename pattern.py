'''
One of the built-in functions of Python is divmod, which takes two arguments and and returns a tuple containing the quotient of first and then the remainder

.

For example:

>>> print divmod(177,10)
(17, 7)

Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.
'''

a,b=int(input()),int(input())
x=divmod(a,b)
print(x[0])
print(x[1])
print(x)

