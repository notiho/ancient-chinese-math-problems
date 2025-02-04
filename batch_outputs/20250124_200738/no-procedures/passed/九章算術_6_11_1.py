"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a good walker can walk 100 steps in the same time a poor walker can walk 60 steps.
Now, the poor walker starts walking 100 steps ahead, and the good walker begins to chase.
Question: how many steps does the good walker need to catch up?

Answer: *a* steps.
"""

# 善行者每單位時間行 100 步
善行者速度 = 100

# 不善行者每單位時間行 60 步
不善行者速度 = 60

# 不善行者先行 100 步
不善行者先行 = 100

# 善行者每步追趕的距離
每步追趕距離 = 善行者速度 - 不善行者速度

# 善行者追趕所需步數
a = Fraction(不善行者先行 * 善行者速度, 每步追趕距離)#----- content ends here -----

"""
"""
