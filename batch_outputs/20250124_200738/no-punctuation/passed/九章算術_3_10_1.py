"""
今有絲一斤價直三百四十五今有絲七兩一十二銖問得錢幾何
術曰以一斤銖數為法以一斤價數乘七兩一十二銖為實實如法得錢數
荅曰 a錢 
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk worth 345 qian.
Now there is 7 liang and 12 zhu of silk.
Question: how much money is it worth?

The procedure says: Take the number of zhu in 1 jin as the divisor.
Multiply the price of 1 jin by the amount of 7 liang and 12 zhu, obtaining the dividend.
Divide the dividend by the divisor, obtaining the amount of qian.

The answer says: *a* qian.
"""

# 一斤價直三百四十五
一斤價 = 345

# 一斤銖數
一斤銖數 = 16 * 24  # 1 jin = 16 liang, 1 liang = 24 zhu

# 七兩一十二銖
絲重量 = 7 * 24 + 12  # Convert to zhu (7 liang = 7 * 24 zhu, plus 12 zhu)

# 以一斤價數乘七兩一十二銖，為實
實 = 一斤價 * 絲重量

# 以一斤銖數為法
法 = 一斤銖數

# 實如法得錢數
a = Fraction(實, 法)#----- content ends here -----

"""
"""
