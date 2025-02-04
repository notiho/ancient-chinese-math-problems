"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric (jian).
Now, if 45 jin and 8 liang of silk is given, how much silk fabric (jian) will be obtained?

The procedure says: Take the numbers of 14 jin (silk) as the divisor.
Take 10 jin (fabric) and multiply it by the current amount of silk (in liang) as the dividend.
Perform the division to obtain the amount of silk fabric.

Answer: *a* jin.
"""

from fractions import Fraction

# Initial silk and fabric amounts
絲_初始 = 14  # 14 jin
縑_初始 = 10  # 10 jin

# Current silk amount (convert jin and liang to liang)
絲_當前 = 45 * 16 + 8  # 1 jin = 16 liang, so 45 jin 8 liang = 45*16 + 8 liang

# Convert initial silk to liang for consistency
絲_初始_兩 = 絲_初始 * 16

# Convert initial fabric to liang for consistency
縑_初始_兩 = 縑_初始 * 16

# Calculate the amount of fabric (in liang) using the given formula
縑_當前_兩 = Fraction(縑_初始_兩 * 絲_當前, 絲_初始_兩)

# Convert the result back to jin and liang
縑_當前_斤 = 縑_當前_兩 // 16  # Whole jin
縑_當前_兩剩餘 = 縑_當前_兩 % 16  # Remaining liang

a = f"{縑_當前_斤}斤 {縑_當前_兩剩餘}兩"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 65/2, Actual: 32斤 8兩"""
