"""
今有人持金出五關，前關二而稅一，次關三而稅一，次關四而稅一，次關五而稅一，次關六而稅一。并五關所稅，適重一斤。問︰本持金幾何？
術曰：置一斤，通所稅者以乘之為實。亦通其不稅者以減所通，餘為法。實如法得一斤。
荅曰： a斤 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the original amount of gold (`a`) carried through five checkpoints, where each checkpoint taxes a fraction of the gold. The total tax collected from all checkpoints equals one jin (斤). Here's the Python code:


"""


from fractions import Fraction

# Tax rates at each checkpoint
tax_rate_1 = Fraction(1, 2)  # 前關二而稅一
tax_rate_2 = Fraction(1, 3)  # 次關三而稅一
tax_rate_3 = Fraction(1, 4)  # 次關四而稅一
tax_rate_4 = Fraction(1, 5)  # 次關五而稅一
tax_rate_5 = Fraction(1, 6)  # 次關六而稅一

# Total tax collected is 1 jin
total_tax = Fraction(1, 1)

# Calculate the original amount of gold (a)
# The formula is derived from the problem description:
# a = total_tax / (tax_rate_1 + tax_rate_2 + tax_rate_3 + tax_rate_4 + tax_rate_5)
a = total_tax / (tax_rate_1 + tax_rate_2 + tax_rate_3 + tax_rate_4 + tax_rate_5)

# The result
a  # This is the original amount of gold in jin


"""


When you run this code, the variable `a` will contain the original amount of gold in jin, represented as a fraction.
"""


"""
Variable 'a' has wrong value. Expected: 6/5, Actual: 20/29"""
