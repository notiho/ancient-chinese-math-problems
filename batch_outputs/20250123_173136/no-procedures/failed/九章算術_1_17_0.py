"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
荅曰：人得 a錢 。
"""

"""
Suppose there are three people. Each person gets:
- 1/3 of a person’s share,
- 1/3 of 6 qian,
- and 3/4 of 4 qian.

Question: How much does each person get?

Answer: Each person gets *a* qian.
"""

from fractions import Fraction

# Total qian to be divided
total_qian = Fraction(6, 1) + Fraction(1, 3) + Fraction(3, 4)

# Number of people
people = 3

# Each person's share
a = total_qian / people

# Result
a
"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 85/36"""
