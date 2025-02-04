"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a good walker can walk 100 steps in the same time a poor walker can walk 60 steps.
Now, the poor walker starts first and walks 100 steps before the good walker begins to chase.
Question: how many steps does the good walker need to take to catch up?

Answer: *a* steps.
"""

# 善行者每單位時間行 100 步
善行者速度 = 100

# 不善行者每單位時間行 60 步
不善行者速度 = 60

# 不善行者先行 100 步
不善行者先行距離 = 100

# 善行者追趕時，兩者的距離縮短速度是兩者速度之差
相對速度 = 善行者速度 - 不善行者速度

# 善行者需要的時間為不善行者先行距離除以相對速度
追趕時間 = Fraction(不善行者先行距離, 相對速度)

# 善行者在追趕時間內行走的步數
a = 善行者速度 * 追趕時間

a  # Output the result#----- content ends here -----

"""
"""
