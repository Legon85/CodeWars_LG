# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3

# mine method
# def zero(*args): return (args[0][0](0, args[0][1])) if args else 0
# def one(*args): return (args[0][0](1, args[0][1])) if args else 1
# def two(*args): return (args[0][0](2, args[0][1])) if args else 2
# def three(*args): return (args[0][0](3, args[0][1])) if args else 3
# def four(*args): return (args[0][0](4, args[0][1])) if args else 4
# def five(*args): return (args[0][0](5, args[0][1])) if args else 5
# def six(*args): return (args[0][0](6, args[0][1])) if args else 6
# def seven(*args): return (args[0][0](7, args[0][1])) if args else 7
# def eight(*args): return (args[0][0](8, args[0][1])) if args else 8
# def nine(*args): return (args[0][0](9, args[0][1])) if args else 9
#
#
# def plus(*args): return (plus, args[0]) if len(args) < 2 else sum(args)
# def minus(*args): return (minus, args[0]) if len(args) < 2 else args[0] - args[1]
# def times(*args): return (times, args[0]) if len(args) < 2 else args[0] * args[1]
# def divided_by(*args): return (divided_by, args[0]) if len(args) < 2 else args[0] // args[1]


# 2nd method
def zero(p=None): return 0  if p is None  else p(0)
def one(p=None): return 1  if p is None  else p(1)
def two(p=None): return 2  if p is None  else p(2)
def three(p=None): return 3  if p is None  else p(3)
def four(p=None): return 4  if p is None  else p(4)
def five(p=None): return 5  if p is None  else p(5)
def six(p=None): return 6  if p is None  else p(6)
def seven(p=None): return 7  if p is None  else p(7)
def eight(p=None): return 8  if p is None  else p(8)
def nine(p=None): return 9  if p is None  else p(9)


def plus(y): return lambda x: x + y
def minus(y): return lambda x: x - y
def times(y): return lambda x: x * y
def divided_by(y): return lambda x: x // y





print(four(plus(nine())))
# print(eight(minus(three())))
# print(seven(times(five())))
# print(six(divided_by(two())))
# print(nine(divided_by(one())))