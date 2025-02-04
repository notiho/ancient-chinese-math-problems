"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
術曰：置不善行者先行一十里，以善行者先至二十里增之，以為法。以不善行者先行一十里，乘善行者一百里，為實。實如法得一里。
荅曰： a(=100/3)里 。
"""

"""
Suppose there is a slower traveler who first travels 10 li. A faster traveler chases after him for 100 li and arrives 20 li ahead of the slower traveler.
Question: how many li does the faster traveler need to travel to catch up to the slower traveler?

The procedure says: Place the 10 li that the slower traveler first travels, and add the 20 li by which the faster traveler arrives ahead, to form the divisor.
Take the 10 li that the slower traveler first travels and multiply it by the 100 li that the faster traveler travels, to form the dividend.
Divide the dividend by the divisor to obtain the result.

Answer: *a*(=100/3) li.
"""

# 不善行者先行一十里
不善行者先行 = 10

# 善行者追之一百里
善行者追行 = 100

# 先至不善行者二十里
善行者先至 = 20

# 以善行者先至二十里增之，以為法
法 = 不善行者先行 + 善行者先至

# 以不善行者先行一十里，乘善行者一百里，為實
實 = 不善行者先行 * 善行者追行

# 實如法得一里
a = Fraction(實, 法) # 100/3
"""
"""
