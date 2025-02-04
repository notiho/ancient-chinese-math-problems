"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric in return.
Now, if 45 jin and 8 liang of silk are given, how much silk fabric will be obtained?

The procedure says: Take the 14 jin as the divisor.
Multiply the 10 jin by the current amount of silk (in liang) to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of silk fabric.

Answer: *a* jin.
"""

# 與人絲一十四斤
原絲 = 14

# 約得縑一十斤
原縑 = 10

# 今與人絲四十五斤八兩
今絲_斤 = 45
今絲_兩 = 8
今絲 = 今絲_斤 * 16 + 今絲_兩  # Convert to liang (1 jin = 16 liang)

# 以一十四斤兩數為法
法 = 原絲 * 16  # Convert to liang

# 以一十斤乘今有絲兩數為實
實 = 原縑 * 16 * 今絲  # Convert to liang

# 實如法得縑數
縑數_兩 = Fraction(實, 法)  # Result in liang
a = Fraction(縑數_兩, 16)  # Convert back to jin
"""
"""
