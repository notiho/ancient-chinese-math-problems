"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is an irregular (trapezoidal) field. The width is 65 bu, one side of the length is 100 bu, and the other side of the length is 72 bu.
Question: how large is the field?

Answer: it is *a* mu.
"""

# 正廣 (width) 65步
正廣 = 65

# 一畔從 (one side length) 100步
一畔從1 = 100

# 一畔從 (other side length) 72步
一畔從2 = 72

# Calculate the average length
平均從 = Fraction(一畔從1 + 一畔從2, 2)

# Calculate the area in square bu
田積 = 正廣 * 平均從

# Convert square bu to mu (1 mu = 240 square bu)
a = Fraction(田積, 240)#----- content ends here -----

"""
"""
