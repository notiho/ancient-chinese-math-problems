"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
術曰：以一斤銖數為法，以一斤價數，乘七兩一十二銖為實。實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk worth 345 qian. Now there is 7 liang and 12 zhu of silk.
Question: how much money is it worth?

The procedure says: Take the number of zhu in 1 jin as the divisor.
Take the price of 1 jin, and multiply it by the 7 liang and 12 zhu to get the dividend.
Divide the dividend by the divisor to get the amount of qian.

Answer: *a* qian.
"""

# 一斤價直三百四十五
一斤價 = 345

# 一斤銖數為法
一斤銖數 = 16 * 24  # 1 jin = 16 liang, 1 liang = 24 zhu

# 七兩一十二銖
絲重量 = (7 * 24) + 12  # Convert to zhu

# 以一斤價數，乘七兩一十二銖為實
實 = 一斤價 * 絲重量

# 實如法得錢數
a = Fraction(實, 一斤銖數)#----- content ends here -----

"""
"""
