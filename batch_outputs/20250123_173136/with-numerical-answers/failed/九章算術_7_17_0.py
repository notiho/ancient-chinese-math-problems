"""
今有黃金九枚，白銀一十一枚，稱之重適等。交易其一，金輕十三兩。問︰金、銀一枚各重幾何？
術曰：假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行。令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行。以分母各乘其行內之數，以盈不足維乘所出率，并以為實。并盈不足為法。實如法，得黃金重。分母乘法以除，得銀重。約之得分也。
荅曰：金重 a(=143/64)斤 ，銀重 b(=117/64)斤 。
"""

"""
Suppose there are 9 pieces of gold and 11 pieces of silver, and their total weights are equal.
If one piece is exchanged, the gold becomes lighter by 13 liang.
Question: how much does one piece of gold and one piece of silver weigh respectively?

The procedure says: Suppose gold weighs 3 jin, and silver weighs 2 jin and 5/11 of a jin. This is 49 short on the right side.
Suppose gold weighs 2 jin, and silver weighs 1 jin and 7/11 of a jin. This is 15 more on the left side.
Multiply the denominators by the numbers in their respective rows, and multiply by the surplus or deficit to obtain the rates. Add these to get the dividend.
Add the surplus and deficit to get the divisor.
Divide the dividend by the divisor to get the weight of gold. Multiply the denominator by the divisor and divide to get the weight of silver. Simplify to get the fractions.

Answer: *a*(=143/64) jin for gold, and *b*(=117/64) jin for silver.
"""

from fractions import Fraction

# 假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行
金假1 = 3
銀假1 = 2 + Fraction(5, 11)
不足1 = 49

# 令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行
金假2 = 2
銀假2 = 1 + Fraction(7, 11)
多2 = 15

# 以分母各乘其行內之數，以盈不足維乘所出率，并以為實
分母 = 11
實 = (分母 * 金假1 * 不足1) + (分母 * 金假2 * 多2)

# 并盈不足為法
法 = 不足1 + 多2

# 實如法，得黃金重
金重 = Fraction(實, 法)

# 分母乘法以除，得銀重
銀重 = Fraction(分母 * 法, 實)

# 答案
a = 金重  # 143/64
b = 銀重  # 117/64
"""
Variable 'a' has wrong value. Expected: 143/64, Actual: 1947/64
Variable 'b' has wrong value. Expected: 117/64, Actual: 64/177"""
