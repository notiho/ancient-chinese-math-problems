"""
今有句五步股十二步問句中容方幾何
術曰并句股為法句股相乘為實實如法而一得方一步
荅曰方 a步 
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (ju) of 5 bu and a height (gu) of 12 bu.
Question: how large of a square can fit inside the base (ju)?

The procedure says: Add the base (ju) and the height (gu) together to form the divisor.
Multiply the base (ju) and the height (gu) together to form the dividend.
Divide the dividend by the divisor, obtaining the side length of the square.

The answer says: the square has a side length of *a* bu.
"""

# 句五步
句 = 5

# 股十二步
股 = 12

# 并句股為法
法 = 句 + 股

# 句股相乘為實
實 = 句 * 股

# 實如法而一得方一步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
