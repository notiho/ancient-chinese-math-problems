"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose 1 liang of silk is worth 5 wen. There are 188 jin and 10 liang of silk.
Question: what is the total value?

Answer: *a* guan.
"""

# 1 jin = 16 liang
liang_per_jin = 16

# Convert 188 jin and 10 liang to total liang
total_liang = 188 * liang_per_jin + 10

# 1 liang of silk is worth 5 wen
value_per_liang = 5

# Total value in wen
total_value_in_wen = total_liang * value_per_liang

# Convert wen to guan (1 guan = 1000 wen)
a = Fraction(total_value_in_wen, 1000)#----- content ends here -----

"""
"""
