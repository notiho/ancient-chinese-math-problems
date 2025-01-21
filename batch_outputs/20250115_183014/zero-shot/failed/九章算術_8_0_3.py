"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾 a秉 ， b斗 ，中禾 c秉 ， d斗 ，下禾 e秉 ， f斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to determine the values of the unknowns. The equations are:

1. \( 3a + 2c + e = 39 \)
2. \( 2a + 3c + e = 34 \)
3. \( a + 2c + 3e = 26 \)

Here, \( a \), \( c \), and \( e \) represent the number of斗 (a unit of volume) per秉 (a unit of weight) for the upper, middle, and lower grains, respectively.

We will use the `Fraction` class to ensure precise calculations.


"""


from fractions import Fraction

# Define the equations
# 3a + 2c + e = 39
# 2a + 3c + e = 34
# a + 2c + 3e = 26

# Step 1: Solve for e
# Subtract the second equation from the first to eliminate e
# (3a + 2c + e) - (2a + 3c + e) = 39 - 34
# a - c = 5
# Rearrange: a = c + 5

# Subtract the third equation from the second to eliminate e
# (2a + 3c + e) - (a + 2c + 3e) = 34 - 26
# a + c - 2e = 8
# Substitute a = c + 5 into this equation
# (c + 5) + c - 2e = 8
# 2c + 5 - 2e = 8
# 2c - 2e = 3
# c - e = 3/2
# Rearrange: e = c - 3/2

# Step 2: Substitute a = c + 5 and e = c - 3/2 into the first equation
# 3a + 2c + e = 39
# 3(c + 5) + 2c + (c - 3/2) = 39
# 3c + 15 + 2c + c - 3/2 = 39
# 6c + 15 - 3/2 = 39
# 6c + 30/2 - 3/2 = 78/2
# 6c + 27/2 = 78/2
# 6c = 51/2
# c = 51/12
# Simplify: c = 17/4

# Step 3: Solve for e
# e = c - 3/2
# e = 17/4 - 3/2
# e = 17/4 - 6/4
# e = 11/4

# Step 4: Solve for a
# a = c + 5
# a = 17/4 + 5
# a = 17/4 + 20/4
# a = 37/4

# Assign the results to variables
a = Fraction(37, 4)  # Upper grain斗 per秉
c = Fraction(17, 4)  # Middle grain斗 per秉
e = Fraction(11, 4)  # Lower grain斗 per秉

# Output the results
a, c, e


"""


The solution is:
- \( a = 37/4 \)斗 per秉
- \( c = 17/4 \)斗 per秉
- \( e = 11/4 \)斗 per秉
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 37/4
Missing variable in output: 'b'
Variable 'c' has wrong value. Expected: 1, Actual: 17/4
Missing variable in output: 'd'
Variable 'e' has wrong value. Expected: 1, Actual: 11/4
Missing variable in output: 'f'"""
