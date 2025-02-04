"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
術曰：如方程，置重過於石之物為負。以正負術入之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the weights of one unit of each type of grain (甲, 乙, 丙) in terms of "石" (a unit of weight). The relationships between the weights are given, and we will use fractions to represent the values.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Let the weights of one unit of 甲, 乙, 丙 be a, b, and c respectively (in 石).
# Given relationships:
# 1. 甲二重如乙一: 2a = b
# 2. 乙三重如丙一: 3b = c
# 3. 丙四重如甲一: 4c = a

# Solve for a, b, and c:
# From 2a = b, we get b = 2a
# From 3b = c, substituting b = 2a, we get c = 3 * 2a = 6a
# From 4c = a, substituting c = 6a, we get 4 * 6a = a
# Simplify: 24a = a
# Solve for a: a = 1/23

a = Fraction(1, 23)  # Weight of 甲禾 in 石
b = 2 * a            # Weight of 乙禾 in 石
c = 6 * a            # Weight of 丙禾 in 石

# The results:
# a = 1/23 石
# b = 2/23 石
# c = 6/23 石
#----- content ends here -----


"""


### Explanation of the Solution:
1. The relationships between the weights are expressed as equations:
   - \( 2a = b \)
   - \( 3b = c \)
   - \( 4c = a \)
2. Substitute \( b = 2a \) into \( 3b = c \) to find \( c = 6a \).
3. Substitute \( c = 6a \) into \( 4c = a \) to find \( 24a = a \), which simplifies to \( a = \frac{1}{23} \).
4. Use \( a \) to calculate \( b \) and \( c \).

The weights of one unit of each type of grain are:
- \( a = \frac{1}{23} \) 石 (甲禾)
- \( b = \frac{2}{23} \) 石 (乙禾)
- \( c = \frac{6}{23} \) 石 (丙禾)
"""


"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1/23
Variable 'b' has wrong value. Expected: 11/23, Actual: 2/23
Variable 'c' has wrong value. Expected: 10/23, Actual: 6/23"""
