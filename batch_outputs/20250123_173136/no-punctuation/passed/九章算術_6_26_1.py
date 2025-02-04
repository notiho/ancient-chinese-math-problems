"""
今有人持米出三關外關三而取一中關五而取一內關七而取一餘米五斗問本持米幾何
術曰置米五斗以所稅者三之五之七之為實以餘不稅者二四六相乘為法實如法得一斗
荅曰 a斗 
"""

"""
Suppose someone carries rice through three checkpoints.
At the outer checkpoint, 1/3 of the rice is taken as tax.
At the middle checkpoint, 1/5 of the rice is taken as tax.
At the inner checkpoint, 1/7 of the rice is taken as tax.
After passing all three checkpoints, 5 dou of rice remain.
Question: how much rice was originally carried?

The procedure says: Place the remaining 5 dou of rice.
Multiply it by the tax rates of 3, 5, and 7, obtaining the dividend.
Multiply the untaxed portions (2, 4, and 6) with each other, obtaining the divisor.
Divide the dividend by the divisor, obtaining the original amount of rice.

The answer says: *a* dou.
"""

# 餘米五斗
餘米 = 5

# 所稅者三之五之七之，為實
稅率_外關 = 3
稅率_中關 = 5
稅率_內關 = 7
實 = 餘米 * 稅率_外關 * 稅率_中關 * 稅率_內關

# 餘不稅者二四六相乘，為法
不稅_外關 = 2
不稅_中關 = 4
不稅_內關 = 6
法 = 不稅_外關 * 不稅_中關 * 不稅_內關

# 實如法得一斗
a = Fraction(實, 法)
"""
"""
