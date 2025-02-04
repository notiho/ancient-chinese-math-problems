"""
今有句五步，股十二步。問︰句中容方幾何？
術曰：并句、股為法，句股相乘為實，實如法而一，得方一步。
荅曰：方 a(=60/17)步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: how large is the square that can fit inside the triangle?

The procedure says: Add the base and height together to form the divisor.
Multiply the base and height together to form the dividend.
Divide the dividend by the divisor to obtain the side length of the square.

Answer: the side length of the square is *a*(=60/17) bu.
"""

# 句五步
句 = 5

# 股十二步
股 = 12

# 并句、股為法
法 = 句 + 股

# 句股相乘為實
實 = 句 * 股

# 實如法而一，得方一步
a = Fraction(實, 法) # 60/17#----- content ends here -----

"""
"""
