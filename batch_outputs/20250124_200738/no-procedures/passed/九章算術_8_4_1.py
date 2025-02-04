"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

#----- content starts here -----
"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾).
- 6 bundles of upper grain lose 1 dou and 8 sheng (i.e., 18 sheng) and are equivalent to 10 bundles of lower grain.
- 15 bundles of lower grain lose 5 sheng and are equivalent to 5 bundles of upper grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: One bundle of upper grain yields *a* sheng, and one bundle of lower grain yields *b* sheng.
"""

from fractions import Fraction

# Given data
上禾_損實 = 18  # 1 dou 8 sheng = 10 + 8 = 18 sheng
下禾_損實 = 5    # 5 sheng

# Equivalences
上禾_秉數1 = 6
下禾_秉數1 = 10

下禾_秉數2 = 15
上禾_秉數2 = 5

# Let:
# 上禾_一秉 = a (grain per bundle of upper grain, in sheng)
# 下禾_一秉 = b (grain per bundle of lower grain, in sheng)

# Equation 1: 6a - 10b = 18
# Equation 2: 15b - 5a = 5

# Solve the system of equations
# From Equation 1: a = (10b + 18) / 6
# Substitute into Equation 2: 15b - 5((10b + 18) / 6) = 5

# Simplify Equation 2
# 15b - (50b + 90) / 6 = 5
# Multiply through by 6 to eliminate the denominator
# 90b - (50b + 90) = 30
# 90b - 50b - 90 = 30
# 40b = 120
# b = 3

# Substitute b = 3 into Equation 1
# 6a - 10(3) = 18
# 6a - 30 = 18
# 6a = 48
# a = 8

# Final results
a = Fraction(8)  # Upper grain per bundle in sheng
b = Fraction(3)  # Lower grain per bundle in sheng

a, b  # Output the results#----- content ends here -----

"""
"""
