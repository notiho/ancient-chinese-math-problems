"""
今有黃金一觔直錢一十萬。問：兩直幾何？
術曰：置錢一十萬，以一十六兩除之，即得。
答曰： a錢 。
"""

"""
Here is the Python code to compute the value of the unknown `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
gold_price = 100000  # in 錢
weight_in_jin = 16  # 1 觔 = 16 兩

# Calculation
a = Fraction(gold_price, weight_in_jin)  # price per 兩 in 錢

# Result
a  # in 錢
#----- content ends here -----


"""


The value of `a` will represent the price of 1 兩 of gold in 錢.
"""


"""
"""
