"""
今有人持米出三關外關三而取一中關五而取一內關七而取一餘米五斗問本持米幾何
術曰置米五斗以所稅者三之五之七之為實以餘不稅者二四六相乘為法實如法得一斗
荅曰 a斗 
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints.
At the outer checkpoint, 1/3 of the rice is taken as tax.
At the middle checkpoint, 1/5 of the remaining rice is taken as tax.
At the inner checkpoint, 1/7 of the remaining rice is taken as tax.
After passing all three checkpoints, 5 dou of rice remain.
Question: how much rice was originally carried?

The procedure says: Place the remaining rice, 5 dou.
Multiply it by the fractions of tax at each checkpoint: 3, 5, and 7, to obtain the dividend.
For the divisor, take the fractions of untaxed rice: 2, 4, and 6, and multiply them together to obtain the divisor.
Divide the dividend by the divisor to obtain the original amount of rice.

Answer: *a* dou.
"""

# 餘米五斗
餘米 = 5

# 所稅者三之五之七之為實
稅率外關 = 3
稅率中關 = 5
稅率內關 = 7
實 = 餘米 * 稅率外關 * 稅率中關 * 稅率內關

# 餘不稅者二四六相乘為法
不稅率外關 = 2
不稅率中關 = 4
不稅率內關 = 6
法 = 不稅率外關 * 不稅率中關 * 不稅率內關

# 實如法得一斗
a = Fraction(實, 法)#----- content ends here -----

"""
"""
