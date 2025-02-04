"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a good walker can walk 100 steps in the same time a poor walker can walk 60 steps.
Now, the poor walker starts 100 steps ahead, and the good walker begins to chase.
Question: how many steps does the good walker need to catch up?

Answer: *a* steps.
"""

# 善行者每步 100
善行者速度 = 100

# 不善行者每步 60
不善行者速度 = 60

# 不善行者先行 100 步
不善行者先行 = 100

# Relative speed difference
相對速度 = 善行者速度 - 不善行者速度

# Steps required for the good walker to catch up
a = Fraction(不善行者先行 * 善行者速度, 相對速度)

a#----- content ends here -----

"""
"""
