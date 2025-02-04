"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints. 
The outer checkpoint takes 1/3 of the rice, the middle checkpoint takes 1/5 of the rice, and the inner checkpoint takes 1/7 of the rice. 
After passing all three checkpoints, 5 dou of rice remain.
Question: how much rice did the person originally carry?

The procedure says: Place the remaining rice as 5 dou. 
Multiply the fractions taken at each checkpoint (1/3, 1/5, 1/7) by the remaining rice to calculate the total tax. 
For the divisor, multiply the complements of the fractions (2/3, 4/5, 6/7). 
Divide the total tax by the divisor to find the original amount of rice.

Answer: *a* dou.
"""

from fractions import Fraction

# 餘米五斗
餘米 = 5

# 稅率
外關稅率 = Fraction(1, 3)
中關稅率 = Fraction(1, 5)
內關稅率 = Fraction(1, 7)

# 不稅率 (complement of the tax rates)
外關不稅率 = 1 - 外關稅率
中關不稅率 = 1 - 中關稅率
內關不稅率 = 1 - 內關稅率

# 以所稅者三之，五之，七之，為實
實 = 餘米 / (外關不稅率 * 中關不稅率 * 內關不稅率)

# 答案
a = 實
a#----- content ends here -----

"""
"""
