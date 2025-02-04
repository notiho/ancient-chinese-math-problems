"""
今有絲一斤價直三百四十五。今有絲七兩一十二銖，問︰得錢幾何？
術曰：以一斤銖數為法，以一斤價數，乘七兩一十二銖為實。實如法得錢數。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of silk, priced at 345 qian. Now, there is 7 liang and 12 zhu of silk.
Question: how much money does it yield?

The procedure says: Take the number of zhu in 1 jin as the divisor.
Take the price of 1 jin, and multiply it by the 7 liang and 12 zhu to get the dividend.
Divide the dividend by the divisor to get the amount of money.

Answer: *a* qian.
"""

from fractions import Fraction

# 1斤價直三百四十五
一斤價 = 345  # in 錢

# 1斤 = 16兩, 1兩 = 24銖
一斤銖數 = 16 * 24  # Total 銖 in 1斤

# 絲七兩一十二銖
絲_兩 = 7
絲_銖 = 12
絲總銖數 = (絲_兩 * 24) + 絲_銖  # Convert to total 銖

# 以一斤價數，乘七兩一十二銖為實
實 = 一斤價 * 絲總銖數

# 實如法得錢數
a = Fraction(實, 一斤銖數)

# Output the result
a  # Answer in 錢#----- content ends here -----

"""
"""
