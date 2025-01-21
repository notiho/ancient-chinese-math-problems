"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾 a秉 b升 ，下禾 c秉 d升 。
"""

"""
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾). 
The problem provides the following relationships:

1. 5 bundles of upper grain lose 1 dou and 1 sheng of grain when converted to 7 bundles of lower grain.
2. 7 bundles of upper grain lose 2 dou and 5 sheng of grain when converted to 5 bundles of lower grain.

Question: How much grain does one bundle of upper grain and one bundle of lower grain yield?

Answer: Upper grain yields *a* dou and *b* sheng per bundle, and lower grain yields *c* dou and *d* sheng per bundle.
"""

from fractions import Fraction

# Conversion factors
dou_to_sheng = 10  # 1 dou = 10 sheng

# Given data
upper_5_loss = 1 * dou_to_sheng + 1  # 1 dou 1 sheng = 11 sheng
upper_7_loss = 2 * dou_to_sheng + 5  # 2 dou 5 sheng = 25 sheng

# Relationships
# 5 bundles of upper grain = 7 bundles of lower grain + 11 sheng loss
# 7 bundles of upper grain = 5 bundles of lower grain + 25 sheng loss

# Let:
# x = grain per bundle of upper grain (in sheng)
# y = grain per bundle of lower grain (in sheng)

# Equations:
# 5x = 7y + 11  (Equation 1)
# 7x = 5y + 25  (Equation 2)

# Solve the system of equations
# From Equation 1: x = (7y + 11) / 5
# Substitute into Equation 2:
# 7((7y + 11) / 5) = 5y + 25
# Multiply through by 5 to eliminate the denominator:
# 49y + 77 = 25y + 125
# Simplify:
# 24y = 48
# y = 2 (grain per bundle of lower grain in sheng)

# Substitute y = 2 into Equation 1:
# 5x = 7(2) + 11
# 5x = 14 + 11
# 5x = 25
# x = 5 (grain per bundle of upper grain in sheng)

# Convert results into dou and sheng
a = x // dou_to_sheng  # Upper grain dou
b = x % dou_to_sheng   # Upper grain sheng

c = y // dou_to_sheng  # Lower grain dou
d = y % dou_to_sheng   # Lower grain sheng

# Final results
a = 0  # Upper grain: 0 dou
b = 5  # Upper grain: 5 sheng
c = 0  # Lower grain: 0 dou
d = 2  # Lower grain: 2 sheng
"""
Code error: name 'x' is not defined"""
