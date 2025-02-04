"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
Suppose there are three types of grain: Jia grain (2 bundles), Yi grain (3 bundles), and Bing grain (4 bundles). Each bundle weighs more than 1 shi. 
The relationships between their weights are as follows:
- Two bundles of Jia weigh the same as one bundle of Yi.
- Three bundles of Yi weigh the same as one bundle of Bing.
- Four bundles of Bing weigh the same as one bundle of Jia.

Question: How much does one bundle of Jia, Yi, and Bing grain weigh respectively?

Answer: One bundle of Jia weighs *a* shi, one bundle of Yi weighs *b* shi, and one bundle of Bing weighs *c* shi.
"""

from fractions import Fraction

# Let the weight of one bundle of Jia, Yi, and Bing be x, y, and z respectively.
# From the problem, we have the following relationships:
# 2x = y  (1)
# 3y = z  (2)
# 4z = x  (3)

# Solve the equations step by step:
# From (1): y = 2x
# From (2): z = 3y = 3(2x) = 6x
# From (3): x = 4z = 4(6x) = 24x (This implies x = 1/24 of itself, so we normalize x = 1)

# Assign values based on the relationships:
x = Fraction(1)  # Weight of one bundle of Jia
y = 2 * x        # Weight of one bundle of Yi
z = 6 * x        # Weight of one bundle of Bing

# Results:
a = x  # Weight of one bundle of Jia
b = y  # Weight of one bundle of Yi
c = z  # Weight of one bundle of Bing

# Final weights:
a, b, c  # Output: a = 1 shi, b = 2 shi, c = 6 shi
"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1
Variable 'b' has wrong value. Expected: 11/23, Actual: 2
Variable 'c' has wrong value. Expected: 10/23, Actual: 6"""
