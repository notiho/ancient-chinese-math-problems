"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is an irregular (trapezoidal) field. The width is 65 bu, one side of the length is 100 bu, and the other side of the length is 72 bu.
Question: how large is the field?

Answer: it is *a* mu.
"""

from fractions import Fraction

# 正廣 (width) = 65 bu
正廣 = 65

# 一畔從 (one side of the length) = 100 bu
一畔從 = 100

# 另一畔從 (the other side of the length) = 72 bu
另一畔從 = 72

# Calculate the average length
平均從 = Fraction(一畔從 + 另一畔從, 2)

# Calculate the area in bu²
田積_in_bu2 = 正廣 * 平均從

# Convert the area to mu (1 mu = 240 bu²)
a = Fraction(田積_in_bu2, 240)

# Output the result
a
"""
"""
