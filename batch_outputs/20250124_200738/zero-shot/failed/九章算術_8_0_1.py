"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of `a`, `b`, and `c`, which represent the number of "斗" (a unit of volume) for one "秉" (a unit of grain) of upper, middle, and lower grain, respectively.

The equations are:
1. \( 3a + 2b + c = 39 \)
2. \( 2a + 3b + c = 34 \)
3. \( a + 2b + 3c = 26 \)

We will use the `Fraction` class to ensure precise calculations.


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# 3a + 2b + c = 39
# 2a + 3b + c = 34
# a + 2b + 3c = 26

# Step 1: Solve for c in terms of a and b using the first equation
# c = 39 - 3a - 2b
# Substitute c into the second and third equations

# Step 2: Substitute c into the second equation
# 2a + 3b + (39 - 3a - 2b) = 34
# Simplify: -a + b = -5
# Rearrange: a - b = 5  (Equation 4)

# Step 3: Substitute c into the third equation
# a + 2b + 3(39 - 3a - 2b) = 26
# Simplify: -8a - 4b = -91
# Rearrange: 2a + b = 22.75  (Equation 5)

# Step 4: Solve the system of two equations (Equation 4 and Equation 5)
# a - b = 5
# 2a + b = 22.75

# Add the two equations to eliminate b
# (a - b) + (2a + b) = 5 + 22.75
# 3a = 27.75
a = Fraction(27.75, 3)

# Substitute a back into Equation 4 to solve for b
# a - b = 5
b = a - 5

# Substitute a and b into the first equation to solve for c
# 3a + 2b + c = 39
c = 39 - 3*a - 2*b

# Results
a, b, c
#----- content ends here -----


"""


This code will compute the values of `a`, `b`, and `c` as fractions.
"""


"""
Code error: both arguments should be Rational instances"""
