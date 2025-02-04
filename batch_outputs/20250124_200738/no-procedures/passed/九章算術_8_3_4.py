"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

#----- content starts here -----
"""
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾). 
The problem provides the following relationships:

1. 5 bundles (秉) of upper grain lose 1 dou and 1 sheng (11 sheng total) when converted to 7 bundles of lower grain.
2. 7 bundles of upper grain lose 2 dou and 5 sheng (25 sheng total) when converted to 5 bundles of lower grain.

Question: How much grain does one bundle of upper grain (上禾) and one bundle of lower grain (下禾) yield?

Answer: One bundle of upper grain yields *a* sheng, and one bundle of lower grain yields *b* sheng.
"""

from fractions import Fraction

# Given data
upper_5_to_lower_7_loss = 10 + 1  # 1 dou 1 sheng = 11 sheng
upper_7_to_lower_5_loss = 20 + 5  # 2 dou 5 sheng = 25 sheng

# Let:
# a = amount of grain in one bundle of upper grain (in sheng)
# b = amount of grain in one bundle of lower grain (in sheng)

# Equations based on the problem:
# 1. 5a - 7b = 11
# 2. 7a - 5b = 25

# Solve the system of equations
# Multiply the first equation by 7 and the second equation by 5 to eliminate `a`:
# 35a - 49b = 77
# 35a - 25b = 125

# Subtract the second equation from the first:
# -49b + 25b = 77 - 125
# -24b = -48
b = Fraction(-48, -24)  # b = 2 (sheng per bundle of lower grain)

# Substitute b = 2 into the first equation:
# 5a - 7(2) = 11
# 5a - 14 = 11
# 5a = 25
a = Fraction(25, 5)  # a = 5 (sheng per bundle of upper grain)

# Final answer
print(f"上禾一秉 a = {a} 升")  # 5 sheng
print(f"下禾一秉 b = {b} 升")  # 2 sheng#----- content ends here -----

"""
"""
