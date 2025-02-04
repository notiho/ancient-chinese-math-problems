"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose 1 jin of silk is worth 345 qian. Now there is 7 liang and 12 zhu of silk.
Question: how much money is it worth?

Answer: it is worth *a* qian.
"""

from fractions import Fraction

# 1 jin = 16 liang, 1 liang = 24 zhu
jin_to_liang = 16
liang_to_zhu = 24

# Price of 1 jin of silk
price_per_jin = 345

# Amount of silk: 7 liang and 12 zhu
silk_liang = 7
silk_zhu = 12

# Convert the silk amount to a fraction of a jin
silk_in_jin = Fraction(silk_liang, jin_to_liang) + Fraction(silk_zhu, jin_to_liang * liang_to_zhu)

# Calculate the price
a = silk_in_jin * price_per_jin

# Result
a#----- content ends here -----

"""
"""
