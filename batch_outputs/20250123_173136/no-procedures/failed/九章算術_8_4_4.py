"""
今有上禾六秉，損實一斗八升，當下禾一十秉。下禾十五秉，損實五升，當上禾五秉。問︰上、下禾實一秉各幾何？
荅曰：上禾一秉實 a升 ，下禾一秉實 b升 。
"""

"""
Suppose there are 6 bundles of upper-grade grain (上禾), which lose 1 dou and 8 sheng of grain when processed. This is equivalent to 10 bundles of lower-grade grain (下禾).
Additionally, 15 bundles of lower-grade grain lose 5 sheng of grain when processed. This is equivalent to 5 bundles of upper-grade grain.
Question: how much grain does one bundle of upper-grade grain (上禾) and one bundle of lower-grade grain (下禾) yield?

Answer: one bundle of upper-grade grain yields *a* sheng, and one bundle of lower-grade grain yields *b* sheng.
"""

from fractions import Fraction

# Known values
上禾_損實 = 1 * 10 + 8  # 1 dou 8 sheng = 18 sheng
上禾_秉數 = 6
下禾_秉數_當上禾 = 10

下禾_損實 = 5  # 5 sheng
下禾_秉數 = 15
上禾_秉數_當下禾 = 5

# Let 上禾一秉實 = a (sheng), 下禾一秉實 = b (sheng)
# From the problem:
# 6a = 18 + 10b  (Equation 1)
# 15b = 5a + 5   (Equation 2)

# Solve Equation 1 for a:
# a = (18 + 10b) / 6
a = Fraction(18 + 10 * Fraction(1, 1), 6)

# Solve Equation 2 for b:
# b = (5a + 5) / 15
b = Fraction(5 * a + 5, 15)

# Final values
a = Fraction(18 + 10 * b, 6)
b = Fraction(5 * a + 5, 15)

a, b
"""
Variable 'a' has wrong value. Expected: 8, Actual: 166/27
Variable 'b' has wrong value. Expected: 3, Actual: 193/81"""
