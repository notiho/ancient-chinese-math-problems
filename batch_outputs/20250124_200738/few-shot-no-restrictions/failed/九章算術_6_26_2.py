"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose a person carries rice through three checkpoints. 
At the outer checkpoint, 1/3 of the rice is taken as tax. 
At the middle checkpoint, 1/5 of the rice is taken as tax. 
At the inner checkpoint, 1/7 of the rice is taken as tax. 
After passing through all three checkpoints, 5 dou of rice remain.
Question: how much rice did the person originally carry?

The procedure says: Place the remaining rice (5 dou). 
Multiply the tax rates (3, 5, 7) together to obtain the dividend. 
Multiply the untaxed portions (2, 4, 6) together to obtain the divisor. 
Divide the dividend by the divisor to obtain the original amount of rice.

Answer: *a* dou.
"""

from fractions import Fraction

# 餘米五斗
餘米 = 5

# 稅率
外關稅率 = Fraction(1, 3)
中關稅率 = Fraction(1, 5)
內關稅率 = Fraction(1, 7)

# 未稅率
外關未稅率 = 1 - 外關稅率  # 2/3
中關未稅率 = 1 - 中關稅率  # 4/5
內關未稅率 = 1 - 內關稅率  # 6/7

# 稅率相乘為實
實 = 3 * 5 * 7

# 未稅率相乘為法
法 = 外關未稅率 * 中關未稅率 * 內關未稅率

# 實如法得本持米
a = Fraction(餘米 * 實, 法)

a  # Original amount of rice in dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 175/16, Actual: 18375/16"""
