"""
今有黃金九枚白銀一十一枚稱之重適等交易其一金輕十三兩問金銀一枚各重幾何
術曰假令黃金三斤白銀二斤一十一分斤之五不足四十九於右行令之黃金二斤白銀一斤一十一分斤之七多一十五於左行以分母各乘其行內之數以盈不足維乘所出率并以為實并盈不足為法實如法得黃金重分母乘法以除得銀重約之得分也
荅曰金重 a斤 銀重 b斤 
"""

"""
Suppose there are 9 pieces of gold and 11 pieces of silver, and their total weight is exactly equal. 
In a trade, one piece of gold is 13 liang lighter than one piece of silver.
Question: how much does one piece of gold and one piece of silver weigh?

The procedure says: 
Suppose the weight of one piece of gold is 3 jin, and one piece of silver is 2 jin and 5/11 jin. 
This is insufficient by 49 liang on the right side. 
Now suppose the weight of one piece of gold is 2 jin, and one piece of silver is 1 jin and 7/11 jin. 
This is excessive by 15 liang on the left side. 
Take the denominators of the fractions and multiply them by the numbers in their respective cases. 
Use the excess and deficiency to adjust the results. 
Add the results together to form the dividend. 
Add the excess and deficiency together to form the divisor. 
Divide the dividend by the divisor to find the weight of one piece of gold. 
Multiply the denominator by the divisor to find the weight of one piece of silver. 
Simplify the fractions to obtain the final result.

Answer: the weight of one piece of gold is *a* jin, and the weight of one piece of silver is *b* jin.
"""

from fractions import Fraction

# 黃金九枚，白銀一十一枚
黃金枚數 = 9
白銀枚數 = 11

# 假令黃金三斤，白銀二斤一十一分斤之五
金重假1 = 3
銀重假1 = 2 + Fraction(5, 11)

# 不足四十九於右行
不足 = 49

# 假令黃金二斤，白銀一斤一十一分斤之七
金重假2 = 2
銀重假2 = 1 + Fraction(7, 11)

# 多一十五於左行
多 = 15

# 以分母各乘其行內之數
分母 = 11
實1 = 分母 * (金重假1 * 黃金枚數 + 銀重假1 * 白銀枚數)
實2 = 分母 * (金重假2 * 黃金枚數 + 銀重假2 * 白銀枚數)

# 以盈不足維乘所出率并以為實
實 = 不足 * 實2 + 多 * 实1

# 并盈不足為法
法 = 不足 + 多

# 實如法得黃金重
金重 = Fraction(實, 法)

# 分母乘法以除得銀重
銀重 = Fraction(分母 * 金重, 法)

# 約之得分
a = 金重
b = 銀重
"""
Code error: name '实1' is not defined"""
