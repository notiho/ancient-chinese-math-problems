"""
今有黃金九枚白銀一十一枚稱之重適等交易其一金輕十三兩問金銀一枚各重幾何
術曰假令黃金三斤白銀二斤一十一分斤之五不足四十九於右行令之黃金二斤白銀一斤一十一分斤之七多一十五於左行以分母各乘其行內之數以盈不足維乘所出率并以為實并盈不足為法實如法得黃金重分母乘法以除得銀重約之得分也
荅曰金重 a斤 銀重 b斤 
"""

"""
Suppose there are 9 pieces of gold and 11 pieces of silver. Their weights are equal when balanced.
If one piece of gold is 13 liang lighter than one piece of silver, how much does each piece of gold and silver weigh?

The procedure says:
Assume gold weighs 3 jin and silver weighs 2 jin and 5/11 jin. The total is 49 liang too light, so move to the right.
Assume gold weighs 2 jin and silver weighs 1 jin and 7/11 jin. The total is 15 liang too heavy, so move to the left.
Multiply the denominators by the respective numbers in each case, and multiply the excess or deficiency by the resulting rates.
Add these to form the dividend. Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to get the weight of gold. Multiply the denominator by the divisor to get the weight of silver.
Simplify the result to get the fractions.

Answer: Gold weighs *a* jin, and silver weighs *b* jin.
"""

from fractions import Fraction

# 黃金九枚，白銀一十一枚
金數 = 9
銀數 = 11

# 假令黃金三斤，白銀二斤一十一分斤之五
金假1 = 3
銀假1 = 2 + Fraction(5, 11)
不足1 = 49

# 假令黃金二斤，白銀一斤一十一分斤之七
金假2 = 2
銀假2 = 1 + Fraction(7, 11)
多2 = 15

# 以分母各乘其行內之數
分母 = 11
實1 = 分母 * (金假1 * 金數 + 銀假1 * 銀數)
實2 = 分母 * (金假2 * 金數 + 銀假2 * 銀數)

# 以盈不足維乘所出率并以為實
實 = 不足1 * 實2 + 多2 * 實1

# 并盈不足為法
法 = 不足1 + 多2

# 實如法得黃金重
金重 = Fraction(實, 法)

# 分母乘法以除得銀重
銀重 = Fraction(分母 * 金重, 法)

# 答案
a = 金重
b = 銀重
"""
Variable 'a' has wrong value. Expected: 143/64, Actual: 14157/32
Variable 'b' has wrong value. Expected: 117/64, Actual: 155727/2048"""
