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

# Given data
gold_price_per_jin = 100000  # in 錢
jin_to_liang = 16  # 1 觔 = 16 兩

# Calculation
a = Fraction(gold_price_per_jin, jin_to_liang)  # price per 兩 in 錢

# Result
a  # This is the answer in 錢
#----- content ends here -----


"""

"""


"""
"""
