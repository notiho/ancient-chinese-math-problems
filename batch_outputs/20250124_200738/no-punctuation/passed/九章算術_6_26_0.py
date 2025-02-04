"""
今有人持米出三關外關三而取一中關五而取一內關七而取一餘米五斗問本持米幾何
術曰置米五斗以所稅者三之五之七之為實以餘不稅者二四六相乘為法實如法得一斗
荅曰 a斗 
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints.
The outer checkpoint takes 1 out of every 3 dou, the middle checkpoint takes 1 out of every 5 dou, and the inner checkpoint takes 1 out of every 7 dou.
After passing through all three checkpoints, 5 dou of rice remain.
Question: how much rice did they originally carry?

The procedure says: Place the remaining 5 dou of rice.
For the tax rates, multiply by 3, 5, and 7 respectively, obtaining the dividend.
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
a = Fraction(實, 法)#----- content ends here -----

"""
"""
