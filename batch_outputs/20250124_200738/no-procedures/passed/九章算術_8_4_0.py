"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

#----- content starts here -----
"""
Suppose there are 6 bundles of upper-grade grain, which lose 1 dou and 8 sheng of grain, equivalent to 10 bundles of lower-grade grain.
Additionally, 15 bundles of lower-grade grain lose 5 sheng of grain, equivalent to 5 bundles of upper-grade grain.
Question: How much grain does one bundle of upper-grade grain and one bundle of lower-grade grain contain?

Answer: One bundle of upper-grade grain contains *a* sheng, and one bundle of lower-grade grain contains *b* sheng.
"""

from fractions import Fraction

# Define the given values
上禾_損實 = 1 * 10 + 8  # 1 dou 8 sheng = 18 sheng
上禾_秉數 = 6
下禾_秉數_當上禾 = 10

下禾_損實 = 5  # 5 sheng
下禾_秉數 = 15
上禾_秉數_當下禾 = 5

# Let the grain in one bundle of upper-grade grain be `a` sheng
# Let the grain in one bundle of lower-grade grain be `b` sheng

# Equation 1: 6a - 10b = 18
# Equation 2: 15b - 5a = 5

# Solve for `a` and `b`
# From Equation 1: a = (10b + 18) / 6
# Substitute into Equation 2:
# 15b - 5((10b + 18) / 6) = 5
# Multiply through by 6 to eliminate fractions:
# 90b - 50b - 90 = 30
# 40b = 120
# b = 3

# Substitute b = 3 into Equation 1:
# 6a - 10(3) = 18
# 6a - 30 = 18
# 6a = 48
# a = 8

# Results
a = Fraction(8)  # Upper-grade grain per bundle
b = Fraction(3)  # Lower-grade grain per bundle

# Final output
a, b  # a = 8 sheng, b = 3 sheng#----- content ends here -----

"""
"""
