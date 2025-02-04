"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is an irregular (trapezoidal) field. The straight width is 65 bu, one side length is 100 bu, and the other side length is 72 bu.
Question: how large is the area of the field?

Answer: it is *a* mu.
"""

# 正廣 (straight width)
正廣 = 65

# 一畔從 (one side length)
從1 = 100

# 一畔從 (the other side length)
從2 = 72

# Calculate the average length of the two sides
平均從 = Fraction(從1 + 從2, 2)

# Calculate the area in square bu
面積_步 = 正廣 * 平均從

# Convert the area into mu (1 mu = 240 square bu)
a = Fraction(面積_步, 240)
"""
"""
