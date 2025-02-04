"""
今有黃金一觔直錢一十萬。問：兩直幾何？
答曰： a錢 。
"""

"""
Suppose there is 1 jin of gold worth 100,000 qian.
Question: how much is 1 liang worth?

Answer: it is worth *a* qian.
"""

# 黃金一觔直錢一十萬
金價 = 100000  # Total value of 1 jin in qian

# 1 觔 = 16 兩
觔_to_兩 = 16

# Calculate the value of 1 liang
a = Fraction(金價, 觔_to_兩)  # Value of 1 liang in qian

a  # Output the result
"""
"""
