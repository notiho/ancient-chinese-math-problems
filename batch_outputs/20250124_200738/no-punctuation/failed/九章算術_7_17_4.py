"""
今有黃金九枚白銀一十一枚稱之重適等交易其一金輕十三兩問金銀一枚各重幾何
術曰假令黃金三斤白銀二斤一十一分斤之五不足四十九於右行令之黃金二斤白銀一斤一十一分斤之七多一十五於左行以分母各乘其行內之數以盈不足維乘所出率并以為實并盈不足為法實如法得黃金重分母乘法以除得銀重約之得分也
荅曰金重 a斤 銀重 b斤 
"""

#----- content starts here -----
"""
Suppose there are 9 pieces of gold and 11 pieces of silver, and their total weight is equal. 
In a transaction, one piece of gold is 13 liang lighter than one piece of silver.
Question: how much does one piece of gold weigh, and how much does one piece of silver weigh?

The procedure says: Suppose gold weighs 3 jin per piece, and silver weighs 2 jin and 5/11 jin per piece. 
This is insufficient by 49 (liang) on the right side. 
Suppose gold weighs 2 jin per piece, and silver weighs 1 jin and 7/11 jin per piece. 
This is excessive by 15 (liang) on the left side.
Multiply the denominators of the fractions by the respective numbers in each case. 
Use the excess or deficiency to adjust the results. 
Combine the rates and use them as the dividend. 
Combine the excess and deficiency as the divisor. 
Divide the dividend by the divisor to find the weight of gold. 
Multiply the denominator by the divisor to find the weight of silver. 
Simplify the fractions to get the results.

Answer: the weight of gold is *a* jin, and the weight of silver is *b* jin.
"""

from fractions import Fraction

# 黃金九枚，白銀一十一枚
金枚 = 9
銀枚 = 11

# 假令黃金三斤，白銀二斤一十一分斤之五
金重1 = 3
銀重1 = 2 + Fraction(5, 11)

# 不足四十九於右行
不足 = 49

# 假令黃金二斤，白銀一斤一十一分斤之七
金重2 = 2
銀重2 = 1 + Fraction(7, 11)

# 多一十五於左行
多 = 15

# 以分母各乘其行內之數
分母 = 11
右實 = 分母 * 不足
左實 = 分母 * 多

# 維乘所出率并以為實
實 = (銀重1 - 金重1) * 右實 + (金重2 - 銀重2) * 左實

# 并盈不足為法
法 = 不足 + 多

# 實如法得黃金重
金重 = Fraction(實, 法)

# 分母乘法以除得銀重
銀重 = 金重 + Fraction(13, 16)

# 約之得分
a = 金重
b = 銀重#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143/64, Actual: -117/32
Variable 'b' has wrong value. Expected: 117/64, Actual: -91/32"""
