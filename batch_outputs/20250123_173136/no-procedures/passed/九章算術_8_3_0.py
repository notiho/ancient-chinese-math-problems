"""
今有上禾五秉，損實一斗一升，當下禾七秉。上禾七秉，損實二斗五升，當下禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉 a升 ，下禾一秉 b升 。
"""

"""
Suppose there are two types of grain, "upper grain" (上禾) and "lower grain" (下禾). 
The problem provides the following relationships:

1. Five bundles of upper grain (上禾) lose 1 dou and 1 sheng of grain when converted to seven bundles of lower grain (下禾).
2. Seven bundles of upper grain (上禾) lose 2 dou and 5 sheng of grain when converted to five bundles of lower grain (下禾).

Question: How much grain does one bundle of upper grain (上禾) and one bundle of lower grain (下禾) contain?

Answer: One bundle of upper grain contains *a* sheng, and one bundle of lower grain contains *b* sheng.
"""

# Represent the known quantities
# Conversion factors for dou and sheng (1 dou = 10 sheng)
斗 = 10  # 1 dou = 10 sheng

# First relationship: 5 bundles of upper grain lose 1 dou and 1 sheng to make 7 bundles of lower grain
上禾_1 = 5  # 5 bundles of upper grain
下禾_1 = 7  # 7 bundles of lower grain
損失_1 = 1 * 斗 + 1  # 1 dou and 1 sheng = 11 sheng

# Second relationship: 7 bundles of upper grain lose 2 dou and 5 sheng to make 5 bundles of lower grain
上禾_2 = 7  # 7 bundles of upper grain
下禾_2 = 5  # 5 bundles of lower grain
損失_2 = 2 * 斗 + 5  # 2 dou and 5 sheng = 25 sheng

# Let the grain in one bundle of upper grain be `a` sheng, and in one bundle of lower grain be `b` sheng
# From the first relationship:
# 5a - 7b = 11  (Equation 1)

# From the second relationship:
# 7a - 5b = 25  (Equation 2)

# Solve the system of linear equations
# Multiply Equation 1 by 7 and Equation 2 by 5 to eliminate `a`:
# 35a - 49b = 77  (from Equation 1)
# 35a - 25b = 125 (from Equation 2)

# Subtract the two equations:
# (35a - 49b) - (35a - 25b) = 77 - 125
# -24b = -48
b = Fraction(-48, -24)  # b = 2 (lower grain per bundle in sheng)

# Substitute `b` into Equation 1 to solve for `a`:
# 5a - 7(2) = 11
# 5a - 14 = 11
# 5a = 25
a = Fraction(25, 5)  # a = 5 (upper grain per bundle in sheng)

# Final results
a  # Upper grain per bundle in sheng
b  # Lower grain per bundle in sheng
"""
"""
