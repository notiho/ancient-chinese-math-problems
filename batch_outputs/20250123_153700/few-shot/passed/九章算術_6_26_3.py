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
Multiply the taxed portions by 3, 5, and 7, obtaining the dividend. 
Multiply the untaxed portions (2, 4, and 6) with each other, obtaining the divisor. 
Divide the dividend by the divisor, obtaining the original amount of rice.

Answer: *a* dou.
"""

# 餘米五斗
餘米 = 5

# 稅率
外關稅率 = 3
中關稅率 = 5
內關稅率 = 7

# 不稅率
外關不稅率 = 外關稅率 - 1
中關不稅率 = 中關稅率 - 1
內關不稅率 = 內關稅率 - 1

# 以所稅者三之，五之，七之，為實
實 = 外關稅率 * 中關稅率 * 內關稅率 * 餘米

# 以餘不稅者二、四、六相乘為法
法 = 外關不稅率 * 中關不稅率 * 內關不稅率

# 實如法得一斗
a = Fraction(實, 法)
"""
"""
