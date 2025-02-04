"""
今有人持米出三關，外關三而取一，中關五而取一，內關七而取一，餘米五斗。問︰本持米幾何？
術曰：置米五斗。以所稅者三之，五之，七之，為實。以餘不稅者二、四、六相乘為法。實如法得一斗。
荅曰： a斗 。
"""

#----- content starts here -----
"""
Suppose someone carries rice through three checkpoints. 
At the outer checkpoint, 1/3 is taken as tax. 
At the middle checkpoint, 1/5 is taken as tax. 
At the inner checkpoint, 1/7 is taken as tax. 
After passing all checkpoints, 5 dou of rice remain.
Question: how much rice was originally carried?

The procedure says: Place the remaining rice as 5 dou. 
Multiply the tax rates (3, 5, 7) together to obtain the dividend. 
Multiply the untaxed portions (2, 4, 6) together to obtain the divisor. 
Divide the dividend by the divisor to obtain the original amount of rice.

Answer: *a* dou.
"""

# 餘米五斗
餘米 = 5

# 所稅者三之，五之，七之，為實
稅率 = [3, 5, 7]
實 = 1
for 稅 in 稅率:
    # Multiply the tax rates together
    稅 = 稅 * 實

# 餘不稅者二、四、六相乘為法
#----- content ends here -----

"""
Missing variable in output: 'a'"""
