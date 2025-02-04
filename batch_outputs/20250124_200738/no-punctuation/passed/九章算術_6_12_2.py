"""
今有不善行者先行一十里善行者追之一百里先至不善行者二十里問善行者幾何里及之
術曰置不善行者先行一十里以善行者先至二十里增之以為法以不善行者先行一十里乘善行者一百里為實實如法得一里
荅曰 a里 
"""

#----- content starts here -----
"""
Suppose there is a slow traveler who first travels 10 li. A fast traveler pursues them for 100 li and overtakes the slow traveler by 20 li.
Question: how many li does the fast traveler travel to catch up?

The procedure says: Place the 10 li that the slow traveler first travels.
Add the 20 li by which the fast traveler overtakes the slow traveler, making the divisor.
Multiply the 10 li that the slow traveler first travels by the 100 li of the fast traveler, making the dividend.
Divide the dividend by the divisor, obtaining the number of li.

Answer: *a* li.
"""

# 不善行者先行一十里
不善行者先行 = 10

# 善行者追之一百里
善行者追 = 100

# 先至不善行者二十里
先至 = 20

# 以善行者先至二十里增之，以為法
法 = 不善行者先行 + 先至

# 以不善行者先行一十里乘善行者一百里，為實
實 = 不善行者先行 * 善行者追

# 實如法得一里
a = Fraction(實, 法)#----- content ends here -----

"""
"""
