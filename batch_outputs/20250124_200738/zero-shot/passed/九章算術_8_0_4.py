"""
今有上禾三秉，中禾二秉，下禾一秉，實三十九斗；上禾二秉，中禾三秉，下禾一秉，實三十四斗；上禾一秉，中禾二秉，下禾三秉，實二十六斗。問︰上、中、下禾實一秉各幾何？
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：上禾一秉， a斗 ，中禾一秉， b斗 ，下禾一秉， c斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves solving a system of linear equations to find the values of `a`, `b`, and `c`, which represent the amount of grain (in "斗") for one秉 of 上禾, 中禾, and 下禾, respectively.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# The system of equations is:
# 3a + 2b + 1c = 39
# 2a + 3b + 1c = 34
# 1a + 2b + 3c = 26

# Solving using substitution or elimination:
# Multiply the first equation by 3, the second by 1, and the third by 2 to align coefficients of 'c'
# 9a + 6b + 3c = 117
# 2a + 3b + 1c = 34
# 2a + 4b + 6c = 52

# Subtract the second equation from the first:
# (9a + 6b + 3c) - (2a + 3b + 1c) = 117 - 34
# 7a + 3b + 2c = 83

# Subtract the third equation from the second:
# (2a + 3b + 1c) - (2a + 4b + 6c) = 34 - 52
# -1b - 5c = -18
# b + 5c = 18

# Substitute b = 18 - 5c into 7a + 3b + 2c = 83:
# 7a + 3(18 - 5c) + 2c = 83
# 7a + 54 - 15c + 2c = 83
# 7a - 13c = 29
# a = (29 + 13c) / 7

# Substitute a = (29 + 13c) / 7 and b = 18 - 5c into the first equation:
# 3((29 + 13c) / 7) + 2(18 - 5c) + c = 39
# (87 + 39c) / 7 + 36 - 10c + c = 39
# (87 + 39c) / 7 + 36 - 9c = 39
# (87 + 39c) / 7 = 3 + 9c
# 87 + 39c = 21 + 63c
# 87 - 21 = 63c - 39c
# 66 = 24c
# c = 66 / 24 = 11 / 4

# Substitute c = 11 / 4 into b = 18 - 5c:
# b = 18 - 5(11 / 4)
# b = 18 - 55 / 4
# b = 72 / 4 - 55 / 4
# b = 17 / 4

# Substitute c = 11 / 4 into a = (29 + 13c) / 7:
# a = (29 + 13(11 / 4)) / 7
# a = (29 + 143 / 4) / 7
# a = (116 / 4 + 143 / 4) / 7
# a = 259 / 4 / 7
# a = 259 / 28

# Final values:
a = Fraction(259, 28)  # 上禾一秉
b = Fraction(17, 4)    # 中禾一秉
c = Fraction(11, 4)    # 下禾一秉

# Results
a, b, c
#----- content ends here -----


"""


### Explanation of the Solution:
1. The problem is translated into a system of three linear equations.
2. The equations are solved step-by-step using substitution and elimination.
3. The `Fraction` class is used to ensure precise calculations with fractions.
4. The final values of `a`, `b`, and `c` are computed and stored in variables with the same names.

### Final Answer:
- 上禾一秉: \( a = \frac{259}{28} \) 斗
- 中禾一秉: \( b = \frac{17}{4} \) 斗
- 下禾一秉: \( c = \frac{11}{4} \) 斗
"""


"""
"""
