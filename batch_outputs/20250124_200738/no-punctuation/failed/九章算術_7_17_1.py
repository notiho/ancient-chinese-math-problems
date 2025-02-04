"""
今有黃金九枚白銀一十一枚稱之重適等交易其一金輕十三兩問金銀一枚各重幾何
術曰假令黃金三斤白銀二斤一十一分斤之五不足四十九於右行令之黃金二斤白銀一斤一十一分斤之七多一十五於左行以分母各乘其行內之數以盈不足維乘所出率并以為實并盈不足為法實如法得黃金重分母乘法以除得銀重約之得分也
荅曰金重 a斤 銀重 b斤 
"""

#----- content starts here -----
"""
Suppose there are 9 pieces of gold and 11 pieces of silver, and their weights are exactly equal. 
In a transaction, one piece of gold is 13 liang lighter than one piece of silver.
Question: what is the weight of one piece of gold and one piece of silver?

The procedure says:
Assume gold weighs 3 jin and silver weighs 2 jin. 
Multiply 11 (the number of silver pieces) by 5 (the assumed weight of silver), resulting in 55. 
Subtract 49 (the total weight of gold), and the result is insufficient by 4. Move this to the right column.
Now assume gold weighs 2 jin and silver weighs 1 jin. 
Multiply 11 by 7 (the assumed weight of silver), resulting in 77. 
Subtract 15 (the total weight of gold), and the result is excessive by 15. Move this to the left column.
Take the denominators of the fractions and multiply them by the numbers in their respective columns. 
For the excess and deficiency, multiply them by the rates and sum them to form the dividend. 
Sum the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the weight of gold. 
Multiply the denominator by the divisor to find the weight of silver. Simplify the fraction.

Answer: the weight of gold is *a* jin, and the weight of silver is *b* jin.
"""

# 黃金九枚，白銀一十一枚
金枚數 = 9
銀枚數 = 11

# 金輕十三兩
金輕銀 = Fraction(13, 16)  # 1 liang = 1/16 jin

# 假令黃金三斤，白銀二斤
假金重1 = 3
假銀重1 = 2

# 一十一分斤之五
盈不足1 = 銀枚數 * 假銀重1 - 金枚數 * 假金重1

# 不足四十九於右行
不足 = 49 - 盈不足1

# 令之黃金二斤，白銀一斤
假金重2 = 2
假銀重2 = 1

# 一十一分斤之七
盈不足2 = 銀枚數 * 假銀重2 - 金枚數 * 假金重2

# 多一十五於左行
多 = 盈不足2 - 15

# 以分母各乘其行內之數
分母1 = 5
分母2 = 7

# 盈不足維乘所出率并以為實
實 = (分母1 * 多) + (分母2 * 不足)

# 并盈不足為法
法 = 分母1 + 分母2

# 實如法得黃金重
金重 = Fraction(實, 法)

# 分母乘法以除得銀重
銀重 = Fraction(金重 + 金輕銀)

# 約之得分
a = 金重
b = 銀重#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143/64, Actual: 67/3
Variable 'b' has wrong value. Expected: 117/64, Actual: 1111/48"""
