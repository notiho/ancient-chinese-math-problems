"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk worth 345 qian. Now, there is 7 liang and 12 zhu of silk.
Question: how much money is it worth?

Answer: it is worth *a* qian.
"""

# 1斤 = 16兩, 1兩 = 24銖
# Total weight of silk in zhu
total_zhu = 7 * 24 + 12

# Total zhu in 1 jin
zhu_per_jin = 16 * 24

# Price per zhu
price_per_zhu = Fraction(345, zhu_per_jin)

# Total price
a = total_zhu * price_per_zhu#----- content ends here -----

"""
"""
