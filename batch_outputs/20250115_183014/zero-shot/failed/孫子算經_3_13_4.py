"""
今有三人共車，二車空；二人共車，九人步。問：人與車各幾何？
術曰：置二人以三乘之，得六，加步者九人，得車一十五，欲知人者，以二乘車，加九人即得。
答曰： a 車， b人 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Let's break it down step by step:

1. Let the number of cars be `a`.
2. Let the number of people be `b`.

From the problem:
- When 3 people share a car, 2 cars are empty. This means the total number of cars is `a`, and the total number of people is `b`. Thus, the number of cars used is `b / 3`, and the number of empty cars is `a - b / 3`. From the problem, we know that `a - b / 3 = 2`.
  
- When 2 people share a car, 9 people are walking. This means the total number of people is `b`, and the number of cars used is `b / 2`. From the problem, we know that the number of walking people is `b - 2 * (b / 2) = 9`.

We now solve these equations to find `a` (cars) and `b` (people).


"""


from fractions import Fraction

# Equation 1: a - b / 3 = 2
# Equation 2: b - 2 * (b / 2) = 9

# Solve Equation 2 for b:
# b - b = 9
# b = 18
b = 18

# Substitute b into Equation 1 to solve for a:
# a - b / 3 = 2
# a = 2 + b / 3
a = 2 + Fraction(b, 3)

# Results
a, b


"""


The solution is:
- `a` (number of cars) = 8
- `b` (number of people) = 18
"""


"""
Variable 'a' has wrong value. Expected: 15, Actual: 8
Variable 'b' has wrong value. Expected: 39, Actual: 18"""
