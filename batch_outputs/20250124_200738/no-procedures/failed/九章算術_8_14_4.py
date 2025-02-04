"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

#----- content starts here -----
"""
Suppose there are three types of grain: Jia (甲), Yi (乙), and Bing (丙). Jia has 2 bundles, Yi has 3 bundles, and Bing has 4 bundles, and their total weight exceeds 1 shi (石). 
The relationships between their weights are as follows:
- 2 bundles of Jia weigh the same as 1 bundle of Yi.
- 3 bundles of Yi weigh the same as 1 bundle of Bing.
- 4 bundles of Bing weigh the same as 1 bundle of Jia.

Question: How much does one bundle of Jia, Yi, and Bing weigh respectively?

Answer: One bundle of Jia weighs *a* shi, one bundle of Yi weighs *b* shi, and one bundle of Bing weighs *c* shi.
"""

from fractions import Fraction

# Let the weight of one bundle of Jia, Yi, and Bing be `a`, `b`, and `c` respectively.
# From the problem, we have the following relationships:
# 2a = b
# 3b = c
# 4c = a

# Solve for `a`, `b`, and `c`:
# From 2a = b, we get b = 2a.
# From 3b = c, substituting b = 2a, we get c = 3 * 2a = 6a.
# From 4c = a, substituting c = 6a, we get 4 * 6a = a, or 24a = a.
# This implies a = 1/24.

# Calculate `a`, `b`, and `c`:
a = Fraction(1, 24)  # Weight of one bundle of Jia
b = 2 * a           # Weight of one bundle of Yi
c = 6 * a           # Weight of one bundle of Bing

# Final results:
a, b, c  # a = 1/24 shi, b = 1/12 shi, c = 1/4 shi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1/24
Variable 'b' has wrong value. Expected: 11/23, Actual: 1/12
Variable 'c' has wrong value. Expected: 10/23, Actual: 1/4"""
