"""
今有黃金一觔直錢一十萬。問：兩直幾何？
術曰：置錢一十萬，以一十六兩除之，即得。
答曰： a錢 。
"""

"""
Suppose there is one jin of gold worth 100,000 qian.
Question: how much is one liang worth?

The procedure says: Place 100,000 qian, and divide it by 16 liang, obtaining the result.

Answer: *a* qian.
"""

# 黃金一觔直錢一十萬
錢 = 100000

# 一觔等於十六兩
兩 = 16

# 以一十六兩除之，即得
a = Fraction(錢, 兩)
"""
"""
