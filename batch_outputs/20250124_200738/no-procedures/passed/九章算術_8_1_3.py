"""
今有上禾七秉，損實一斗，益之下禾二秉，而實一十斗。下禾八秉，益實一斗與上禾二秉，而實一十斗。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a斗 ，下禾一秉實 b斗 。
"""

#----- content starts here -----
"""
Suppose there are two types of grain: upper grain (上禾) and lower grain (下禾). 
- Seven bundles (秉) of upper grain lose 1 dou of grain, and adding 2 bundles of lower grain results in a total of 10 dou.
- Eight bundles of lower grain gain 1 dou of grain, and adding 2 bundles of upper grain results in a total of 10 dou.

Question: How much grain does one bundle of upper grain (上禾) and one bundle of lower grain (下禾) yield, respectively?

Answer: One bundle of upper grain yields *a* dou, and one bundle of lower grain yields *b* dou.
"""

from fractions import Fraction

# Let x represent the yield of one bundle of upper grain (上禾)
# Let y represent the yield of one bundle of lower grain (下禾)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Solve for x and y
# From Equation 1: 7x + 2y = 11
# From Equation 2: 2x + 8y = 9

# Multiply Equation 1 by 4 to align coefficients of y
# 28x + 8y = 44
# 2x + 8y = 9

# Subtract the second equation from the first
# (28x + 8y) - (2x + 8y) = 44 - 9
# 26x = 35
x = Fraction(35, 26)

# Substitute x into Equation 1: 7x + 2y = 11
# 7 * (35/26) + 2y = 11
# 245/26 + 2y = 11
# 2y = 11 - 245/26
# 2y = (286/26) - (245/26)
# 2y = 41/26
y = Fraction(41, 52)

# Final results
a = x  # Yield of one bundle of upper grain
b = y  # Yield of one bundle of lower grain

a, b  # Output the results#----- content ends here -----

"""
"""
