"""
今有黃金九枚，白銀一十一枚，稱之重適等。交易其一，金輕十三兩。問︰金、銀一枚各重幾何？
術曰：假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行。令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行。以分母各乘其行內之數，以盈不足維乘所出率，并以為實。并盈不足為法。實如法，得黃金重。分母乘法以除，得銀重。約之得分也。
荅曰：金重 a(=143/64)斤 ，銀重 b(=117/64)斤 。
"""

"""
Suppose there are 9 pieces of gold and 11 pieces of silver, and their total weight is equal.
When one piece is exchanged, the gold becomes lighter by 13 liang.
Question: how much does one piece of gold and one piece of silver weigh?

The procedure says: Suppose gold weighs 3 jin, and silver weighs 2 jin and 5/11 jin. This is insufficient by 49 on the right side.
Suppose gold weighs 2 jin, and silver weighs 1 jin and 7/11 jin. This exceeds by 15 on the left side.
Multiply the denominators by the numbers in their respective rows, and multiply the excess and deficiency by the resulting rates. Add these to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to obtain the weight of gold. Multiply the denominator by the divisor and divide to obtain the weight of silver. Simplify to get the fractions.

Answer: The weight of gold is *a*(=143/64) jin, and the weight of silver is *b*(=117/64) jin.
"""

# 假令黃金三斤，白銀二斤、一十一分斤之五，不足四十九，於右行
黃金假設1 = 3
白銀假設1 = 2 + Fraction(5, 11)
不足 = 49

# 令之黃金二斤，白銀一斤、一十一分斤之七，多一十五於左行
黃金假設2 = 2
白銀假設2 = 1 + Fraction(7, 11)
多 = 15

# 以分母各乘其行內之數
分母1 = 11
分母2 = 11

# 計算盈不足維乘所出率
實1 = 分母1 * 不足
實2 = 分母2 * 多

# 并以為實
實 = 實1 + 實2

# 并盈不足為法
法 = 不足 + 多

# 實如法，得黃金重
黃金重 = Fraction(實, 法)

# 分母乘法以除，得銀重
白銀重 = Fraction(分母1 * 分母2, 法)

# 答案
a = 黃金重  # 143/64
b = 白銀重  # 117/64
"""
Variable 'a' has wrong value. Expected: 143/64, Actual: 11
Variable 'b' has wrong value. Expected: 117/64, Actual: 121/64"""
