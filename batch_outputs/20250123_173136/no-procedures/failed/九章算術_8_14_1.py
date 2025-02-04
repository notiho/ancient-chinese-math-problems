"""
今有甲禾二秉、乙禾三秉、丙禾四秉，重皆過於石。甲二重如乙一，乙三重如丙一，丙四重如甲一。問︰甲、乙、丙禾一秉各重幾何？
荅曰：甲禾一秉重 a石 ，乙禾一秉重 b石 ，丙禾一秉重 c石 。
"""

"""
Suppose there are three types of grain: Jia (甲), Yi (乙), and Bing (丙). Jia has 2 bundles, Yi has 3 bundles, and Bing has 4 bundles. 
The total weight of each type of grain exceeds 1 shi (石). The relationships between their weights are as follows:
- 2 bundles of Jia weigh the same as 1 bundle of Yi.
- 3 bundles of Yi weigh the same as 1 bundle of Bing.
- 4 bundles of Bing weigh the same as 1 bundle of Jia.

Question: How much does 1 bundle of Jia, Yi, and Bing weigh respectively?

Answer: 1 bundle of Jia weighs *a* shi, 1 bundle of Yi weighs *b* shi, and 1 bundle of Bing weighs *c* shi.
"""

from fractions import Fraction

# Let the weight of 1 bundle of Jia, Yi, and Bing be a, b, and c respectively
# From the problem:
# 2a = b
# 3b = c
# 4c = a

# Solve for a, b, and c in terms of a common unit
# From 2a = b, we get b = 2a
# From 3b = c, substitute b = 2a, so c = 3 * 2a = 6a
# From 4c = a, substitute c = 6a, so 4 * 6a = a, which simplifies to 24a = a
# Therefore, a = 1/24

# Now calculate b and c
a = Fraction(1, 24)  # Weight of 1 bundle of Jia
b = 2 * a            # Weight of 1 bundle of Yi
c = 3 * b            # Weight of 1 bundle of Bing

# Final results
a, b, c  # Jia, Yi, Bing weights in shi
"""
Variable 'a' has wrong value. Expected: 17/23, Actual: 1/24
Variable 'b' has wrong value. Expected: 11/23, Actual: 1/12
Variable 'c' has wrong value. Expected: 10/23, Actual: 1/4"""
