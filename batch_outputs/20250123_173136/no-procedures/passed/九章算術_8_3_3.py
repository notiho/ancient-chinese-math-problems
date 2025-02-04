"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
Suppose there are two types of grain: "upper grain" (上禾) and "lower grain" (下禾). 
The problem provides the following relationships:

1. 5 bundles of upper grain lose 1 dou and 1 sheng of grain, equivalent to 7 bundles of lower grain.
2. 7 bundles of upper grain lose 2 dou and 5 sheng of grain, equivalent to 5 bundles of lower grain.

Question: How much grain does one bundle of upper grain (上禾) and one bundle of lower grain (下禾) yield?

Answer: One bundle of upper grain yields *a* sheng, and one bundle of lower grain yields *b* sheng.
"""

from fractions import Fraction

# Convert dou and sheng into sheng (1 dou = 10 sheng)
loss_1 = 1 * 10 + 1  # 1 dou 1 sheng = 11 sheng
loss_2 = 2 * 10 + 5  # 2 dou 5 sheng = 25 sheng

# Let:
# x = grain per bundle of upper grain (in sheng)
# y = grain per bundle of lower grain (in sheng)

# From the problem:
# 5x - 7y = 11  (Equation 1)
# 7x - 5y = 25  (Equation 2)

# Solve the system of equations using substitution or elimination
# Multiply Equation 1 by 7 and Equation 2 by 5 to eliminate y:
# 35x - 49y = 77  (Equation 3)
# 35x - 25y = 125 (Equation 4)

# Subtract Equation 3 from Equation 4:
# (35x - 25y) - (35x - 49y) = 125 - 77
# 24y = 48
y = Fraction(48, 24)  # y = 2 (grain per bundle of lower grain)

# Substitute y = 2 into Equation 1:
# 5x - 7(2) = 11
# 5x - 14 = 11
# 5x = 25
x = Fraction(25, 5)  # x = 5 (grain per bundle of upper grain)

# Final answers:
a = x  # Upper grain per bundle
b = y  # Lower grain per bundle

# Results:
a, b  # a = 5 sheng, b = 2 sheng
"""
"""
