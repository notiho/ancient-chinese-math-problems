"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric in return.
Now, if 45 jin and 8 liang of silk are given, how much silk fabric will be obtained?

The procedure says: Take the numbers of 14 jin as the divisor.
Take 10 jin and multiply it by the current number of silk (in liang) as the dividend.
Do the division, obtaining the number of jin of silk fabric.

Answer: *a* jin.
"""

# 與人絲一十四斤
絲_原 = 14

# 約得縑一十斤
縑_原 = 10

# 今與人絲四十五斤八兩
絲_今_斤 = 45
絲_今_兩 = 8

# Convert 今與人絲 to liang (1 斤 = 16 兩)
絲_今_總兩 = (絲_今_斤 * 16) + 絲_今_兩

# 以一十四斤兩數為法 (convert 14 斤 to liang for consistency)
法 = 絲_原 * 16

# 以一十斤乘今有絲兩數為實 (convert 10 斤 to liang for consistency)
實 = 縑_原 * 16 * 絲_今_總兩

# 實如法得縑數
縑_總兩 = Fraction(實, 法)

# Convert 縑_總兩 back to 斤 and 兩
縑_斤 = 縑_總兩 // 16
縑_兩 = 縑_總兩 % 16

a = f"{縑_斤}斤 {縑_兩}兩"
"""
Variable 'a' has wrong value. Expected: 65/2, Actual: 32斤 8兩"""
