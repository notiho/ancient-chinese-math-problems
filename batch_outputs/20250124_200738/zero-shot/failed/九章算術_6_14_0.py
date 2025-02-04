"""
今有人持金十二斤出關。關稅之，十分而取一。今關取金二斤，償錢五千。問︰金一斤值錢幾何？
術曰：以一十乘二斤，以十二斤減之，餘為法。以一十乘五千為實。實如法得一錢。
荅曰： a 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating the value of one jin (斤) of gold in terms of money. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_gold = 12  # in jin
tax_rate = Fraction(1, 10)  # 10% tax
gold_taken = 2  # in jin
money_paid = 5000  # in qian (錢)

# Calculation
# The formula is: (10 * gold_taken) / (10 * total_gold - gold_taken) = value of 1 jin in qian
a = Fraction(10 * money_paid, 10 * total_gold - gold_taken)

# The value of one jin of gold in qian
a
#----- content ends here -----


"""


The variable `a` will store the value of one jin of gold in qian (錢).
"""


"""
Variable 'a' has wrong value. Expected: 6250, Actual: 25000/59"""
