"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
答曰： a貫 。
"""

"""
Suppose 1 liang of silk is worth 5 wen. There are 188 jin and 10 liang of silk in total.
Question: what is the total value?

Answer: it is worth *a* guan.
"""

# 1 jin = 16 liang
liang_per_jin = 16

# Total silk in liang
total_liang = 188 * liang_per_jin + 10

# Value of 1 liang of silk
value_per_liang = 5  # in wen

# Total value in wen
total_value_wen = total_liang * value_per_liang

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(total_value_wen, 1000)  # in guan
"""
"""
