"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a(=175/16)斗 。
"""

"""
Suppose someone carries rice through three checkpoints. 
At the outer checkpoint, 1/3 of the rice is taken as tax.
At the middle checkpoint, 1/5 of the rice is taken as tax.
At the inner checkpoint, 1/7 of the rice is taken as tax.
After passing all three checkpoints, 5 dou of rice remains.
Question: how much rice was originally carried?

The procedure says: Place the remaining rice as 5 dou.
Multiply the taxed portions by 3, 5, and 7, obtaining the dividend.
Multiply the untaxed portions (2, 4, 6) with each other, obtaining the divisor.
Divide the dividend by the divisor to obtain the original amount of rice.

Answer: *a*(=175/16) dou.
"""

from fractions import Fraction

# 餘米五斗
餘米 = 5

# 所稅者三之，五之，七之，為實
實 = 3 * 5 * 7 * 餘米

# 餘不稅者二、四、六相乘為法
法 = 2 * 4 * 6

# 實如法得一斗
a = Fraction(實, 法) # 175/16

"""
"""
