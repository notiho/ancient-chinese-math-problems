"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of `a`, `b`, and `c`, which represent the number of "斗" (a unit of volume) for each type of grain.

The system of equations is as follows:
1. \( 3a + 2b + c = 39 \)
2. \( 2a + 3b + c = 34 \)
3. \( a + 2b + 3c = 26 \)

We will solve this system using substitution and elimination. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# 3a + 2b + c = 39
# 2a + 3b + c = 34
# a + 2b + 3c = 26

# Step 1: Eliminate 'c' by subtracting equations
# Subtract (2a + 3b + c = 34) from (3a + 2b + c = 39)
# This gives: a - b = 5
# Subtract (a + 2b + 3c = 26) from (2a + 3b + c = 34)
# This gives: a + b - 2c = 8

# Step 2: Solve for 'a' and 'b' in terms of 'c'
# From a - b = 5, we get: a = b + 5
# Substitute a = b + 5 into a + b - 2c = 8
# (b + 5) + b - 2c = 8
# 2b + 5 - 2c = 8
# 2b - 2c = 3
# b - c = Fraction(3, 2)

# Step 3: Solve for 'b' and 'c'
# From b - c = 3/2, we get: b = c + 3/2
# Substitute b = c + 3/2 and a = b + 5 into the first equation
# 3a + 2b + c = 39
# 3(b + 5) + 2(c + 3/2) + c = 39
# 3b + 15 + 2c + 3 + c = 39
# 3b + 3c + 18 = 39
# 3(c + 3/2) + 3c + 18 = 39
# 3c + 9/2 + 3c + 18 = 39
# 6c + 9/2 + 18 = 39
# 6c + 45/2 = 39
# 6c = 39 - 45/2
# 6c = 78/2 - 45/2
# 6c = 33/2
# c = 33/12
# c = Fraction(11, 4)

# Step 4: Solve for 'b' and 'a'
# b = c + 3/2
# b = 11/4 + 3/2
# b = 11/4 + 6/4
# b = 17/4

# a = b + 5
# a = 17/4 + 20/4
# a = 37/4

# Final results
a = Fraction(37, 4)  # 上禾一秉
b = Fraction(17, 4)  # 中禾一秉
c = Fraction(11, 4)  # 下禾一秉

# Print the results
a, b, c
#----- content ends here -----


"""


The solution is:
- \( a = \frac{37}{4} \) 斗
- \( b = \frac{17}{4} \) 斗
- \( c = \frac{11}{4} \) 斗
"""


"""
"""
