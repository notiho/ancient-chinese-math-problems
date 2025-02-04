"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
術曰：置善行者一百步，減不善行者六十步，餘四十步，以為法。以善行者之一百步，乘不善行者先行一百步，為實。實如法得一步。
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a good walker can walk 100 steps in a given time, while a slower walker can walk 60 steps in the same time.
Now, the slower walker starts 100 steps ahead, and the good walker chases them.
Question: how many steps will the good walker take to catch up?

The procedure says: Take the 100 steps of the good walker and subtract the 60 steps of the slower walker, leaving 40 steps as the divisor.
Multiply the 100 steps of the good walker by the 100 steps the slower walker started ahead, giving the dividend.
Divide the dividend by the divisor to get the number of steps.

Answer: *a* steps.
"""

from fractions import Fraction

# 善行者行一百步
善行者步數 = 100

# 不善行者行六十步
不善行者步數 = 60

# 不善行者先行一百步
不善行者先行 = 100

# 置善行者一百步，減不善行者六十步，餘四十步，以為法
法 = 善行者步數 - 不善行者步數

# 以善行者之一百步，乘不善行者先行一百步，為實
實 = 善行者步數 * 不善行者先行

# 實如法得一步
a = Fraction(實, 法)

a  # Output the result#----- content ends here -----

"""
"""
