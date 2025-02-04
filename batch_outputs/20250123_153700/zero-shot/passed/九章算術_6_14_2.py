"""
今有人持金十二斤出關。關稅之，十分而取一。今關取金二斤，償錢五千。問︰金一斤值錢幾何？
術曰：以一十乘二斤，以十二斤減之，餘為法。以一十乘五千為實。實如法得一錢。
荅曰： a 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
total_gold = 12  # in jin
tax_rate = Fraction(1, 10)  # 10% tax
gold_taken = 2  # in jin
money_paid = 5000  # in qian

# Calculation
a = (10 * money_paid) / (10 * gold_taken - total_gold)

# The value of a (gold per jin in qian)
a = Fraction(a)

# Result
a


"""


The variable `a` represents the value of 1 jin of gold in qian.
"""


"""
"""
