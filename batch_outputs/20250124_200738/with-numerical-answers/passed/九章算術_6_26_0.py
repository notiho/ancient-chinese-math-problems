"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a(=175/16)斗 。
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints. 
The outer checkpoint takes 1/3 of the rice, the middle checkpoint takes 1/5, and the inner checkpoint takes 1/7. 
After passing all three checkpoints, 5 dou of rice remain.
Question: how much rice was originally carried?

The procedure says: Place the remaining rice as 5 dou. 
Multiply it by the fractions of rice taken at each checkpoint: 3, 5, and 7, to obtain the dividend.
Multiply the fractions of rice not taken at each checkpoint: 2, 4, and 6, to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of rice.

Answer: *a*(=175/16) dou.
"""

# 餘米五斗
餘米 = Fraction(5)

# 所稅者：三、五、七
稅率_外關 = 3
稅率_中關 = 5
稅率_內關 = 7

# 餘不稅者：二、四、六
不稅率_外關 = 2
不稅率_中關 = 4
不稅率_內關 = 6

# 以所稅者三之，五之，七之，為實
實 = 餘米 * 稅率_外關 * 稅率_中關 * 稅率_內關

# 以餘不稅者二、四、六相乘為法
法 = 不稅率_外關 * 不稅率_中關 * 不稅率_內關

# 實如法得一斗
a = Fraction(實, 法) # 175/16
#----- content ends here -----

"""
"""
