"""
今有黃金九枚，白銀一十一枚，稱之重適等。交易其一，金輕十三兩。問︰金、銀一枚各重幾何？
術曰：假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行。令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行。以分母各乘其行內之數，以盈不足維乘所出率，并以為實。并盈不足為法。實如法，得黃金重。分母乘法以除，得銀重。約之得分也。
荅曰：金重 a(=143/64)斤 ，銀重 b(=117/64)斤 。
"""

#----- content starts here -----
"""
Suppose there are 9 pieces of gold and 11 pieces of silver, and their total weights are equal.
If one piece is exchanged, the gold becomes lighter by 13 liang.
Question: how much does one piece of gold and one piece of silver weigh?

The procedure says: Suppose gold weighs 3 jin, and silver weighs 2 jin and 5/11 of a jin. This is 49 less on the right side.
Suppose gold weighs 2 jin, and silver weighs 1 jin and 7/11 of a jin. This is 15 more on the left side.
Multiply the denominators by the numbers within their respective sides, and multiply by the excess or deficit to obtain the rates.
Add the excess and deficit to form the divisor.
Divide the results by the divisor to obtain the weight of the gold.
Multiply the denominator by the divisor and divide to obtain the weight of the silver.
Simplify the fractions to get the results.

Answer: *a*(=143/64) jin for gold, and *b*(=117/64) jin for silver.
"""

from fractions import Fraction

# 假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行
黃金假1 = 3
白銀假1 = 2 + Fraction(5, 11)
不足1 = 49

# 令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行
黃金假2 = 2
白銀假2 = 1 + Fraction(7, 11)
多2 = 15

# 以分母各乘其行內之數，以盈不足維乘所出率，并以為實
分母1 = 11
分母2 = 11

實1 = 分母1 * (黃金假1 + 白銀假1) * 不足1
實2 = 分母2 * (黃金假2 + 白銀假2) * 多2

# 并盈不足為法
法 = 不足1 + 多2

# 實如法，得黃金重
黃金重 = Fraction(實1 + 實2, 法)

# 分母乘法以除，得銀重
銀重 = Fraction(法 * 分母1, 實1 + 實2)

# 答案
a = 黃金重  # 143/64
b = 銀重    # 117/64#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143/64, Actual: 885/16
Variable 'b' has wrong value. Expected: 117/64, Actual: 176/885"""
