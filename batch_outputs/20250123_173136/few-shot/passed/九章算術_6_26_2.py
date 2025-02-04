"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a斗 。
"""

"""
Suppose a person carries rice through three checkpoints. 
At the outer checkpoint, 1/3 of the rice is taken as tax. 
At the middle checkpoint, 1/5 of the rice is taken as tax. 
At the inner checkpoint, 1/7 of the rice is taken as tax. 
After passing all the checkpoints, 5 dou of rice remain.
Question: how much rice did the person originally carry?

The procedure says: Place the remaining rice as 5 dou. 
Multiply the tax rates (3, 5, 7) together to form the dividend. 
Multiply the untaxed portions (2, 4, 6) together to form the divisor. 
Divide the dividend by the divisor to determine the original amount of rice.

Answer: *a* dou.
"""

from fractions import Fraction

# 餘米五斗
餘米 = 5

# 所稅者三、五、七
稅率_外關 = 3
稅率_中關 = 5
稅率_內關 = 7

# 餘不稅者二、四、六
不稅_外關 = 稅率_外關 - 1
不稅_中關 = 稅率_中關 - 1
不稅_內關 = 稅率_內關 - 1

# 以所稅者三之，五之，七之，為實
實 = 稅率_外關 * 稅率_中關 * 稅率_內關 * 餘米

# 以餘不稅者二、四、六相乘為法
法 = 不稅_外關 * 不稅_中關 * 不稅_內關

# 實如法得一斗
a = Fraction(實, 法)
"""
"""
