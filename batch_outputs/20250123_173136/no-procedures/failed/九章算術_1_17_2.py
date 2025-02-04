"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
荅曰：人得 a錢 。
"""

"""
Suppose there are three people. Each person receives:
- 1/3 of a person’s share,
- 1/3 of 6 qian,
- and 3/4 of a qian.

Question: how much does each person get?

Answer: each person gets *a* qian.
"""

from fractions import Fraction

# Total qian to be divided
total_qian = 6 + Fraction(3, 4)

# Divide total qian equally among 3 people
a = total_qian / 3

# Result
a
"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 9/4"""
