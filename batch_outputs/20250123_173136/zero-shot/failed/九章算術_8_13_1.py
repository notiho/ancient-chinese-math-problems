"""
今有白禾二步、青禾三步、黃禾四步、黑禾五步，實各不滿斗。白取青、黃，青取黃、黑，黃取黑、白，黑取白、青，各一步，而實滿斗。問︰白、青、黃、黑禾實一步各幾何？
術曰：如方程，各置所取，以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：白禾一步實 a斗 ，青禾一步實 b斗 ，黃禾一步實 c斗 ，黑禾一步實 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves solving a system of linear equations. Here's the Python code:


"""


from fractions import Fraction

# Define the system of equations based on the problem description:
# Let a, b, c, d represent the amount of grain (in dou) for white, green, yellow, and black grains respectively.
# The equations are:
# 1. a + b + c = 1
# 2. b + c + d = 1
# 3. c + d + a = 1
# 4. d + a + b = 1

# Solve the system of equations manually:
# Add all four equations:
# (a + b + c) + (b + c + d) + (c + d + a) + (d + a + b) = 4
# 3a + 3b + 3c + 3d = 4
# a + b + c + d = Fraction(4, 3)

# Subtract the first equation from the sum:
# (a + b + c + d) - (a + b + c) = Fraction(4, 3) - 1
# d = Fraction(1, 3)

# Subtract the second equation from the sum:
# (a + b + c + d) - (b + c + d) = Fraction(4, 3) - 1
# a = Fraction(1, 3)

# Subtract the third equation from the sum:
# (a + b + c + d) - (c + d + a) = Fraction(4, 3) - 1
# b = Fraction(1, 3)

# Subtract the fourth equation from the sum:
# (a + b + c + d) - (d + a + b) = Fraction(4, 3) - 1
# c = Fraction(1, 3)

# Assign the solutions to variables:
a = Fraction(1, 3)  # White grain
b = Fraction(1, 3)  # Green grain
c = Fraction(1, 3)  # Yellow grain
d = Fraction(1, 3)  # Black grain

# Print the results:
print("White grain (a):", a, "dou")
print("Green grain (b):", b, "dou")
print("Yellow grain (c):", c, "dou")
print("Black grain (d):", d, "dou")


"""


### Explanation:
1. The problem describes a system of four linear equations where the sum of three grains equals one dou for each equation.
2. By adding all four equations, we derive the total sum of all grains.
3. Subtracting individual equations from the total sum gives the value of each grain.
4. The solution is represented using the `Fraction` class to ensure precision.

### Output:
```
White grain (a): 1/3 dou
Green grain (b): 1/3 dou
Yellow grain (c): 1/3 dou
Black grain (d): 1/3 dou
```
"""


"""
Variable 'a' has wrong value. Expected: 11/37, Actual: 1/3
Variable 'b' has wrong value. Expected: 28/111, Actual: 1/3
Variable 'c' has wrong value. Expected: 17/111, Actual: 1/3
Variable 'd' has wrong value. Expected: 10/111, Actual: 1/3"""
