"""
今有黃金一觔直錢一十萬。問：兩直幾何？
答曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of gold worth 100,000 qian.
Question: how much is 1 liang worth?

Answer: it is worth *a* qian.
"""

# 黃金一觔直錢一十萬
金價_一觔 = 100000

# 1 觔 = 16 兩
觔_to_兩 = 16

# Calculate the value of 1 liang
a = Fraction(金價_一觔, 觔_to_兩)#----- content ends here -----

"""
"""
