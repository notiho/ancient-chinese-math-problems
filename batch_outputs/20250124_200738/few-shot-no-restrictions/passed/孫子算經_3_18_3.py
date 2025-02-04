"""
今有黃金一觔直錢一十萬。問：兩直幾何？
術曰：置錢一十萬，以一十六兩除之，即得。
答曰： a錢 。
"""

#----- content starts here -----
"""
Suppose there is 1 jin of gold worth 100,000 qian. 
Question: how much is 1 liang worth?

The procedure says: Place 100,000 qian and divide it by 16 liang (since 1 jin = 16 liang). 
The result is the value of 1 liang.

Answer: *a* qian.
"""

from fractions import Fraction

# 黃金一觔直錢一十萬
黃金價值 = 100000  # in qian

# 一觔等於十六兩
一觔 = 16  # in liang

# 以一十六兩除之，即得
a = Fraction(黃金價值, 一觔)

# Output the result
a#----- content ends here -----

"""
"""
