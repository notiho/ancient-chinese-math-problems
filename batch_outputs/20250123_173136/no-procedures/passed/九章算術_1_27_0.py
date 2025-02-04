"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
荅曰： a畝 。
"""

"""
Suppose there is an irregular (trapezoidal) field. The width is 65 bu, one side of the length is 100 bu, and the other side of the length is 72 bu.
Question: how large is the field?

Answer: it makes *a* mu.
"""

# 正廣 (width) = 65 步
正廣 = 65

# 一畔從 (one side length) = 100 步
從一 = 100

# 一畔從 (other side length) = 72 步
從二 = 72

# Calculate the average length
平均從 = Fraction(從一 + 從二, 2)

# Calculate the area in square bu
面積_步 = 正廣 * 平均從

# Convert the area to mu (1 mu = 240 square bu)
a = Fraction(面積_步, 240)

a  # Output the result in mu
"""
"""
