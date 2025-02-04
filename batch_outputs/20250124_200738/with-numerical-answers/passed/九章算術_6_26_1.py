"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a(=175/16)斗 。
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints.
The outer checkpoint takes 1 for every 3, the middle checkpoint takes 1 for every 5, and the inner checkpoint takes 1 for every 7.
After passing through all checkpoints, 5 dou of rice remain.
Question: how much rice was originally carried?

The procedure says: Place the remaining rice, 5 dou.
Multiply it by the tax rates of 3, 5, and 7, obtaining the dividend.
Multiply the untaxed portions (2, 4, and 6) with each other, obtaining the divisor.
Divide the dividend by the divisor to find the original amount of rice.

Answer: *a*(=175/16) dou.
"""

# 餘米五斗
餘米 = Fraction(5)

# 所稅者三、五、七
稅率_外關 = 3
稅率_中關 = 5
稅率_內關 = 7

# 餘不稅者二、四、六
不稅_外關 = 稅率_外關 - 1
不稅_中關 = 稅率_中關 - 1
不稅_內關 = 稅率_內關 - 1

# 以所稅者三之，五之，七之，為實
實 = 餘米 * 稅率_外關 * 稅率_中關 * 稅率_內關

# 以餘不稅者二、四、六相乘為法
法 = 不稅_外關 * 不稅_中關 * 不稅_內關

# 實如法得一斗
a = Fraction(實, 法) # 175/16
#----- content ends here -----

"""
"""
