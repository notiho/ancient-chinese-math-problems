"""
今有善行者行一百步，不善行者行六十步。今不善行者先行一百步，善行者追之，問︰幾何步及之？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose a good walker can walk 100 steps in the same time a poor walker can walk 60 steps.
Now, the poor walker starts first and walks 100 steps ahead. The good walker starts afterward and chases the poor walker.
Question: how many steps does the good walker need to catch up?

Answer: *a* steps.
"""

# Define the speeds of the good walker and poor walker
善行者速度 = 100  # steps per unit time
不善行者速度 = 60   # steps per unit time

# The poor walker is 100 steps ahead
不善行者先行 = 100

# The relative speed difference
相對速度 = 善行者速度 - 不善行者速度

# The time it takes for the good walker to catch up
追及時間 = Fraction(不善行者先行, 相對速度)

# The number of steps the good walker takes to catch up
a = 善行者速度 * 追及時間

a  # Output the result#----- content ends here -----

"""
"""
