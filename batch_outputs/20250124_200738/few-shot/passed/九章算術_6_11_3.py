"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
術曰：置善行者一百步，減不善行者六十步，餘四十步，以為法。以善行者之一百步，乘不善行者先行一百步，為實。實如法得一步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a good walker walks 100 steps, while a poor walker walks 60 steps in the same time.
Now, the poor walker starts 100 steps ahead, and the good walker chases after them.
Question: how many steps will it take for the good walker to catch up?

The procedure says: Place the 100 steps of the good walker and subtract the 60 steps of the poor walker.
The remainder, 40 steps, is taken as the divisor.
Take the 100 steps of the good walker and multiply it by the 100 steps the poor walker started ahead, obtaining the dividend.
Divide the dividend by the divisor to obtain the number of steps.

The answer says: *a* steps.
"""

# 善行者行一百步
善行者步 = 100

# 不善行者行六十步
不善行者步 = 60

# 不善行者先行一百步
不善行者先行 = 100

# 置善行者一百步，減不善行者六十步，餘四十步，以為法
法 = 善行者步 - 不善行者步

# 以善行者之一百步，乘不善行者先行一百步，為實
實 = 善行者步 * 不善行者先行

# 實如法得一步
a = Fraction(實, 法)#----- content ends here -----

"""
"""
