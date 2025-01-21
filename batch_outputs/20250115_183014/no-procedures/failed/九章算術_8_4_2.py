"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 實 b升 ，下禾 c秉 實 d升 。
"""

"""
Suppose there are 6 bundles of upper-grade grain, which lose 1 dou and 8 sheng of grain when processed, equivalent to 10 bundles of lower-grade grain.  
Additionally, 15 bundles of lower-grade grain lose 5 sheng of grain when processed, equivalent to 5 bundles of upper-grade grain.  
Question: How much grain does one bundle of upper-grade and lower-grade grain yield, respectively?

Answer: One bundle of upper-grade grain yields *b* sheng, and one bundle of lower-grade grain yields *d* sheng.
"""

from fractions import Fraction

# Given data
上禾_秉_1 = 6  # 6 bundles of upper-grade grain
上禾_損實 = 1 * 10 + 8  # 1 dou 8 sheng = 18 sheng
上禾_當下禾 = 10  # Equivalent to 10 bundles of lower-grade grain

下禾_秉_1 = 15  # 15 bundles of lower-grade grain
下禾_損實 = 5  # 5 sheng
下禾_當上禾 = 5  # Equivalent to 5 bundles of upper-grade grain

# Step 1: Calculate the yield of one bundle of upper-grade grain
# Let the yield of one bundle of upper-grade grain be `a` sheng
# Let the yield of one bundle of lower-grade grain be `b` sheng

# From the first condition:
# 6 bundles of upper-grade grain lose 18 sheng and are equivalent to 10 bundles of lower-grade grain
# 6 * a - 18 = 10 * b  (Equation 1)

# From the second condition:
# 15 bundles of lower-grade grain lose 5 sheng and are equivalent to 5 bundles of upper-grade grain
# 15 * b - 5 = 5 * a  (Equation 2)

# Solve the system of equations
# From Equation 1: a = (10 * b + 18) / 6
# Substitute into Equation 2:
# 15 * b - 5 = 5 * ((10 * b + 18) / 6)
# Multiply through by 6 to eliminate the fraction:
# 90 * b - 30 = 50 * b + 90
# Simplify:
# 40 * b = 120
# b = 3 (yield of one bundle of upper-grade grain)

# Substitute b = 3 into Equation 1 to find a:
# 6 * a - 18 = 10 * 3
# 6 * a - 18 = 30
# 6 * a = 48
# a = 8 (yield of one bundle of lower-grade grain)

# Final results
上禾_實 = 8  # Yield of one bundle of upper-grade grain in sheng
下禾_實 = 3  # Yield of one bundle of lower-grade grain in sheng

# Output
a = 上禾_秉_1
b = 上禾_實
c = 下禾_秉_1
d = 下禾_實

a, b, c, d
"""
Variable 'a' has wrong value. Expected: 1, Actual: 6
Variable 'c' has wrong value. Expected: 1, Actual: 15"""
