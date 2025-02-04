"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is an irregular (trapezoidal) field. The correct width is 65 bu. One side of the length is 100 bu, and the other side of the length is 72 bu.
Question: how large is the field?

Answer: it is *a* mu.
"""

# 正廣 (width) = 65 步
正廣 = 65

# 一畔從 (one side length) = 100 步
一畔從 = 100

# 另一畔從 (other side length) = 72 步
另一畔從 = 72

# Calculate the average length
平均從 = Fraction(一畔從 + 另一畔從, 2)

# Calculate the area in square bu
田積 = 正廣 * 平均從

# Convert the area into mu (1 mu = 240 square bu)
a = Fraction(田積, 240)

# The result is the area in mu
a
"""
"""
