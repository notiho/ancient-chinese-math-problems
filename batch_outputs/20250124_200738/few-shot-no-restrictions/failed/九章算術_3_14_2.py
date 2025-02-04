"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
術曰：以一十四斤兩數為法，以一十斤乘今有絲兩數為實，實如法得縑數。
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and it is agreed to obtain 10 jin of silk fabric in return.
Now, if 45 jin and 8 liang of silk is given, how much silk fabric will be obtained?

The procedure says: Take the total weight of 14 jin as the divisor.
Multiply the 10 jin of silk fabric by the total weight of the current silk (in liang) as the dividend.
Perform the division to obtain the amount of silk fabric.

Answer: *a* jin.
"""

from fractions import Fraction

# Convert jin and liang to liang (1 jin = 16 liang)
絲_原 = 14 * 16  # 14 jin to liang
縑_原 = 10 * 16  # 10 jin to liang

# Current silk: 45 jin 8 liang
絲_今 = 45 * 16 + 8  # Convert to liang

# Procedure
法 = 絲_原  # Divisor
實 = 縑_原 * 絲_今  # Dividend

# Result in liang
縑_今 = Fraction(實, 法)

# Convert back to jin and liang
縑_今_斤 = 縑_今 // 16  # Whole jin
縑_今_兩 = 縑_今 % 16  # Remaining liang

# Final result
a = f"{縑_今_斤}斤 {縑_今_兩}兩"
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 65/2, Actual: 32斤 8兩"""
