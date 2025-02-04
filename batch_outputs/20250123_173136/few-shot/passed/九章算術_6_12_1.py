"""
今有不善行者先行一十里，善行者追之一百里，先至不善行者二十里。問︰善行者幾何里及之？
術曰：置不善行者先行一十里，以善行者先至二十里增之，以為法。以不善行者先行一十里，乘善行者一百里，為實。實如法得一里。
荅曰： a里 。
"""

"""
Suppose there is a slower traveler who first travels 10 li, and a faster traveler who chases after them for 100 li. 
The faster traveler arrives 20 li ahead of the slower traveler.
Question: how many li does the faster traveler travel to catch up?

The procedure says: Place the 10 li that the slower traveler first traveled, and add the 20 li by which the faster traveler arrives ahead. This becomes the divisor.
Take the 10 li that the slower traveler first traveled and multiply it by the 100 li of the faster traveler. This becomes the dividend.
Divide the dividend by the divisor to obtain the number of li.

Answer: *a* li.
"""

# 不善行者先行一十里
不善行者先行 = 10

# 善行者追之一百里
善行者追行 = 100

# 善行者先至不善行者二十里
善行者先至 = 20

# 置不善行者先行一十里，以善行者先至二十里增之，以為法
法 = 不善行者先行 + 善行者先至

# 以不善行者先行一十里，乘善行者一百里，為實
實 = 不善行者先行 * 善行者追行

# 實如法得一里
a = Fraction(實, 法)
"""
"""
