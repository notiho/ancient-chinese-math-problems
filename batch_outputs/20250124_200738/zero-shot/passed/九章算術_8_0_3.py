"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of \(a\), \(b\), and \(c\), which represent the amount of grain (in斗) for one unit of upper, middle, and lower grain respectively.

The equations are:
1. \(3a + 2b + c = 39\)
2. \(2a + 3b + c = 34\)
3. \(a + 2b + 3c = 26\)

We will solve this system of equations using substitution and elimination.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# 3a + 2b + c = 39
# 2a + 3b + c = 34
# a + 2b + 3c = 26

# Step 1: Eliminate 'c' from the first two equations
# Subtract (2a + 3b + c = 34) from (3a + 2b + c = 39)
# This gives: a - b = 5
# a = b + 5

# Step 2: Eliminate 'c' from the second and third equations
# Subtract (a + 2b + 3c = 26) from (2a + 3b + c = 34)
# This gives: a + b - 2c = 8

# Step 3: Substitute a = b + 5 into the equation a + b - 2c = 8
# (b + 5) + b - 2c = 8
# 2b - 2c = 3
# b - c = Fraction(3, 2)
# c = b - Fraction(3, 2)

# Step 4: Substitute a = b + 5 and c = b - Fraction(3, 2) into the first equation
# 3a + 2b + c = 39
# 3(b + 5) + 2b + (b - Fraction(3, 2)) = 39
# 3b + 15 + 2b + b - Fraction(3, 2) = 39
# 6b + 15 - Fraction(3, 2) = 39
# 6b = 39 - 15 + Fraction(3, 2)
# 6b = 24 + Fraction(3, 2)
# 6b = Fraction(48, 2) + Fraction(3, 2)
# 6b = Fraction(51, 2)
# b = Fraction(51, 2) / 6
# b = Fraction(51, 12)

# Step 5: Solve for a and c
# a = b + 5
# a = Fraction(51, 12) + 5
# a = Fraction(51, 12) + Fraction(60, 12)
# a = Fraction(111, 12)

# c = b - Fraction(3, 2)
# c = Fraction(51, 12) - Fraction(18, 12)
# c = Fraction(33, 12)

# Final results
a = Fraction(111, 12)
b = Fraction(51, 12)
c = Fraction(33, 12)

# Print the results
a, b, c
#----- content ends here -----


"""


The solution is:
- \(a = \frac{111}{12}\)斗
- \(b = \frac{51}{12}\)斗
- \(c = \frac{33}{12}\)斗
"""


"""
"""
