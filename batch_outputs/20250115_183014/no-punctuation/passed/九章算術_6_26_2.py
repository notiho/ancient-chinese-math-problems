"""
今有人持米出三關外關三而取一中關五而取一內關七而取一餘米五斗問本持米幾何
術曰置米五斗以所稅者三之五之七之為實以餘不稅者二四六相乘為法實如法得一斗
荅曰 a斗 
"""

"""
Suppose a person carries rice through three checkpoints.
At the outer checkpoint, for every 3 dou, 1 dou is taken as tax.
At the middle checkpoint, for every 5 dou, 1 dou is taken as tax.
At the inner checkpoint, for every 7 dou, 1 dou is taken as tax.
After passing through all three checkpoints, 5 dou of rice remain.
Question: how much rice was originally carried?

The procedure says: Place the remaining rice, 5 dou.
For the tax rates, multiply them by 3, 5, and 7 respectively, obtaining the dividend.
For the untaxed portions, multiply 2, 4, and 6 respectively, obtaining the divisor.
Divide the dividend by the divisor to obtain the original amount of rice.

The answer says: *a* dou.
"""

# 餘米五斗
餘米 = 5

# 所稅者三之五之七之為實
實 = 3 * 5 * 7 * 餘米

# 餘不稅者二四六相乘為法
法 = 2 * 4 * 6

# 實如法得一斗
a = Fraction(實, 法)
"""
"""
