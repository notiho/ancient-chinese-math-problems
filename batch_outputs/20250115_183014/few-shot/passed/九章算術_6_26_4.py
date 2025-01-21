"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a斗 。
"""

"""
Suppose someone carries rice through three checkpoints. 
At the outer checkpoint, 1/3 of the rice is taxed. 
At the middle checkpoint, 1/5 of the rice is taxed. 
At the inner checkpoint, 1/7 of the rice is taxed. 
After passing all three checkpoints, 5 dou of rice remain. 
Question: how much rice was originally carried?

The procedure says: Place the remaining rice as 5 dou. 
Multiply the taxed portions by 3, 5, and 7 respectively, obtaining the dividend. 
Multiply the untaxed portions (2, 4, and 6) together, obtaining the divisor. 
Divide the dividend by the divisor to obtain the original amount of rice.

Answer: *a* dou.
"""

from fractions import Fraction

# 餘米五斗
餘米 = 5

# 所稅者三、五、七
稅率1 = 3
稅率2 = 5
稅率3 = 7

# 餘不稅者二、四、六
不稅1 = 2
不稅2 = 4
不稅3 = 6

# 以所稅者三之，五之，七之，為實
實 = 稅率1 * 稅率2 * 稅率3 * 餘米

# 以餘不稅者二、四、六相乘為法
法 = 不稅1 * 不稅2 * 不稅3

# 實如法得一斗
a = Fraction(實, 法)
"""
"""
