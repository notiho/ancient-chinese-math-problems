"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a(=175/16)斗 。
"""

"""
Suppose someone carries rice through three checkpoints. 
The outer checkpoint takes 1/3 of the rice, the middle checkpoint takes 1/5, and the inner checkpoint takes 1/7. 
After passing through all three checkpoints, 5 dou of rice remain.
Question: how much rice was originally carried?

The procedure says: Place the remaining rice as 5 dou. 
Multiply the tax rates (3, 5, 7) to obtain the dividend.
Multiply the remaining portions (2, 4, 6) to obtain the divisor.
Divide the dividend by the divisor to find the original amount of rice.

Answer: *a*(=175/16) dou.
"""

from fractions import Fraction

# 餘米五斗
餘米 = 5

# 所稅者三之，五之，七之，為實
稅率 = [3, 5, 7]
實 = 1
for 稅 in 稅率:
    實 *= 稅

# 餘不稅者二、四、六相乘為法
不稅率 = [2, 4, 6]
法 = 1
for 不稅 in 不稅率:
    法 *= 不稅

# 實如法得一斗
a = Fraction(實 * 餘米, 法)  # 175/16

"""
"""
