"""
今有人持金十二斤出關。關稅之，十分而取一。今關取金二斤，償錢五千。問︰金一斤值錢幾何？
術曰：以一十乘二斤，以十二斤減之，餘為法。以一十乘五千為實。實如法得一錢。
荅曰： a 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the value of one jin (斤) of gold in terms of money (錢). Here's the solution:


"""


from fractions import Fraction

# Given values
total_gold = 12  # Total gold in jin
tax_rate = Fraction(1, 10)  # Tax rate (1/10)
gold_taken = 2  # Gold taken by the customs in jin
money_paid = 5000  # Money paid in qian (錢)

# Calculation
# According to the method described:
# Multiply 10 (denominator of tax rate) by the gold taken (2 jin)
# Subtract the total gold (12 jin) from the result to get the divisor (法)
divisor = 10 * gold_taken - total_gold

# Multiply 10 (denominator of tax rate) by the money paid (5000 qian) to get the dividend (實)
dividend = 10 * money_paid

# Divide the dividend by the divisor to get the value of 1 jin of gold
a = Fraction(dividend, divisor)

# Result
a  # Value of 1 jin of gold in qian


"""


The variable `a` will hold the value of one jin of gold in terms of qian (錢).
"""


"""
"""
