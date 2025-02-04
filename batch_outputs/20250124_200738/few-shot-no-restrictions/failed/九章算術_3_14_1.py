"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric (jian).
Now, if 45 jin and 8 liang of silk are given, how much silk fabric (jian) will be obtained?

The procedure says: Take the 14 jin (and liang, if any) as the divisor.
Multiply the 10 jin by the current amount of silk (in jin and liang) to get the dividend.
Divide the dividend by the divisor to get the amount of silk fabric.

Answer: *a* jin.
"""

from fractions import Fraction

# Conversion constants
LIANG_PER_JIN = 16  # 16 liang = 1 jin

# Given data
絲_原 = 14  # 14 jin
縑_原 = 10  # 10 jin

絲_今_斤 = 45  # 45 jin
絲_今_兩 = 8  # 8 liang

# Convert current silk to total liang
絲_今_總兩 = (絲_今_斤 * LIANG_PER_JIN) + 絲_今_兩

# Convert original silk to total liang
絲_原_總兩 = 絲_原 * LIANG_PER_JIN

# Convert original silk fabric to total liang
縑_原_總兩 = 縑_原 * LIANG_PER_JIN

# Calculate the total silk fabric in liang
縑_今_總兩 = Fraction(縑_原_總兩 * 絲_今_總兩, 絲_原_總兩)

# Convert the result back to jin and liang
縑_今_斤 = 縑_今_總兩 // LIANG_PER_JIN
縑_今_兩 = 縑_今_總兩 % LIANG_PER_JIN

a = f"{縑_今_斤}斤 {縑_今_兩}兩"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 65/2, Actual: 32斤 8兩"""
