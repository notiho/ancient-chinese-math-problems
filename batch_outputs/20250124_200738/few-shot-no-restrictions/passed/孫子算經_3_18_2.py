"""
今有黃金一觔直錢一十萬。問：兩直幾何？
術曰：置錢一十萬，以一十六兩除之，即得。
答曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of gold worth 100,000 qian. 
Question: how much is 1 liang worth?

The procedure says: Place 100,000 qian, divide it by 16 liang (since 1 jin = 16 liang), and the result is obtained.

Answer: *a* qian.
"""

from fractions import Fraction

# 黃金一觔直錢一十萬
錢 = 100000

# 一觔 = 16兩
兩 = 16

# 以一十六兩除之，即得
a = Fraction(錢, 兩)

# Output the result
a#----- content ends here -----

"""
"""
