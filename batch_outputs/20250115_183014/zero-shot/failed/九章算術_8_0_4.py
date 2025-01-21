"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to determine the values of the unknowns. Let's write the Python code:


"""


from fractions import Fraction

# Define the system of equations:
# 3a + 2c + 1e = 39
# 2a + 3c + 1e = 34
# 1a + 2c + 3e = 26

# Solve for e (下禾):
# Multiply the first equation by 1, the second equation by 1, and the third equation by 1:
# 3a + 2c + 1e = 39
# 2a + 3c + 1e = 34
# 1a + 2c + 3e = 26

# Subtract equations to eliminate variables and solve for e:
# Subtract the second equation from the first:
# (3a + 2c + 1e) - (2a + 3c + 1e) = 39 - 34
# a - c = 5

# Subtract the third equation from the second:
# (2a + 3c + 1e) - (1a + 2c + 3e) = 34 - 26
# a + c - 2e = 8

# Solve for c in terms of a from the first simplified equation:
# c = a - 5

# Substitute c = a - 5 into the second simplified equation:
# a + (a - 5) - 2e = 8
# 2a - 5 - 2e = 8
# 2a - 2e = 13
# a - e = 6.5
# e = a - 6.5

# Substitute e = a - 6.5 and c = a - 5 into the first original equation:
# 3a + 2(a - 5) + 1(a - 6.5) = 39
# 3a + 2a - 10 + a - 6.5 = 39
# 6a - 16.5 = 39
# 6a = 55.5
# a = 55.5 / 6
a = Fraction(55.5, 6)

# Solve for c:
c = a - 5

# Solve for e:
e = a - 6.5

# Convert to fractions for clarity:
a = Fraction(55.5, 6)
c = Fraction(a - 5)
e = Fraction(a - 6.5)

# Output the results:
b = a
d = c
f = e

print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}, f = {f}")


"""


This code solves the system of equations step by step and assigns the results to the variables `a`, `b`, `c`, `d`, `e`, and `f`. The `Fraction` class is used to ensure that the results are represented as fractions when necessary.
"""


"""
Code error: both arguments should be Rational instances"""
