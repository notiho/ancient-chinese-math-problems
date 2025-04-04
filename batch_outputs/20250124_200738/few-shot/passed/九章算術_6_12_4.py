"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
術曰：置不善行者先行一十里，以善行者先至二十里增之，以為法。以不善行者先行一十里，乘善行者一百里，為實。實如法得一里。
荅曰： a里 。
"""

#----- content starts here -----
"""
Suppose there is a slow traveler who first travels 10 li. A fast traveler chases after them for 100 li and arrives 20 li ahead of the slow traveler.
Question: how many li does the fast traveler travel to catch up?

The procedure says: Place the 10 li that the slow traveler first travels, and add the 20 li by which the fast traveler arrives ahead. This becomes the divisor.
Take the 10 li that the slow traveler first travels and multiply it by the 100 li that the fast traveler travels. This becomes the dividend.
Divide the dividend by the divisor to obtain the number of li.

Answer: *a* li.
"""

# 不善行者先行一十里
不善行者先行 = 10

# 善行者追之一百里
善行者追 = 100

# 先至不善行者二十里
善行者先至 = 20

# 以善行者先至二十里增之，以為法
法 = 不善行者先行 + 善行者先至

# 以不善行者先行一十里，乘善行者一百里，為實
實 = 不善行者先行 * 善行者追

# 實如法得一里
a = Fraction(實, 法)#----- content ends here -----

"""
"""
