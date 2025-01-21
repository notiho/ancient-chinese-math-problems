"""
今有黃金一觔直錢一十萬。問：兩直幾何？
術曰：置錢一十萬，以一十六兩除之，即得。
答曰： a錢 。
"""

"""
To solve this problem, we need to calculate the value of one "兩" (tael) of gold when one "觔" (jin) of gold is worth 100,000 coins. Since one "觔" equals 16 "兩," we divide 100,000 by 16.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_value = 100000  # coins for 1 jin
jin_to_liang = 16     # 1 jin = 16 liang

# Calculation
a = Fraction(total_value, jin_to_liang)  # value of 1 liang in coins

# Result
a  # This represents the value of 1 liang in coins


"""


The value of `a` will be the answer in coins.
"""


"""
"""
