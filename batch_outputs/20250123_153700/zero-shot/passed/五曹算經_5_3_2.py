"""
今有絲一两直錢五文，有絲一百八十八斤一十两。問：計直㡬何？
術曰：列絲一百八十八斤，以一十六两乘之、納十两，得三千一十八两；以五文乘之即得。
答曰： a貫 。
"""

"""
To solve this problem, we need to calculate the total value of 188斤 (jin) and 10两 (liang) of silk, where 1两 of silk is worth 5文 (wen). Here's the Python code:


"""


from fractions import Fraction

# Given values
silk_price_per_liang = 5  # 5 wen per liang
silk_weight_jin = 188  # 188 jin
silk_weight_liang = 10  # 10 liang
liang_per_jin = 16  # 16 liang in 1 jin

# Convert the total weight to liang
total_liang = silk_weight_jin * liang_per_jin + silk_weight_liang

# Calculate the total price in wen
total_price_wen = total_liang * silk_price_per_liang

# Convert the total price to guan (1 guan = 1000 wen)
a = Fraction(total_price_wen, 1000)

# Result
a  # The total value in guan


"""


The variable `a` will contain the total value in 貫 (guan).
"""


"""
"""
