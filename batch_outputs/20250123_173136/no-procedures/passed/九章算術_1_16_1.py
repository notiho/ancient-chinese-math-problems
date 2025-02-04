"""
今有七人，分八錢三分錢之一。問：人得幾何？
荅曰：人得 a錢 。
"""

"""
Suppose there are 7 people, and they are to divide 8 qian and 1/3 of a qian equally.
Question: how much does each person get?

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# Total amount of qian
total_qian = 8 + Fraction(1, 3)

# Number of people
people = 7

# Divide the total qian by the number of people
a = total_qian / people

# Result
a
"""
"""
