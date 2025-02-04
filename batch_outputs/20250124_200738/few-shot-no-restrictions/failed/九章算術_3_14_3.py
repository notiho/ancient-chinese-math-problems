"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric in return.
Now, if 45 jin and 8 liang of silk are given, how much silk fabric will be obtained?

The procedure says: Take the total weight of 14 jin as the divisor.
Multiply the 10 jin of silk fabric by the total weight of the current silk (in liang) as the dividend.
Divide the dividend by the divisor to obtain the amount of silk fabric.

Answer: *a* jin.
"""

from fractions import Fraction

# Conversion constants
JIN_TO_LIANG = 16  # 1 jin = 16 liang

# Given values
絲_原 = 14  # 14 jin of silk
縑_原 = 10  # 10 jin of fabric
絲_今_jin = 45  # 45 jin
絲_今_liang = 8  # 8 liang

# Convert current silk weight to liang
絲_今_total_liang = (絲_今_jin * JIN_TO_LIANG) + 絲_今_liang

# Procedure
# 法 = 絲_原 converted to liang
法 = 絲_原 * JIN_TO_LIANG

# 實 = 縑_原 converted to liang, multiplied by 絲_今_total_liang
實 = 縑_原 * JIN_TO_LIANG * 絲_今_total_liang

# 縑數 = 實 / 法, converted back to jin
縑數_liang = Fraction(實, 法)
a =縑數_liang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 65/2, Actual: 520"""
