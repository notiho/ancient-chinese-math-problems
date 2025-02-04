"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
荅曰： a斤 。
"""

"""
Suppose 14 jin of silk is given to someone, and in return, 10 jin of silk fabric (jian) is obtained.
Now, if 45 jin and 8 liang of silk are given, how much silk fabric (jian) will be obtained?

Answer: *a* jin.
"""

# Conversion: 1 jin = 16 liang
絲_斤_1 = 14  # First case: 14 jin of silk
縑_斤_1 = 10  # First case: 10 jin of fabric

絲_斤_2 = 45  # Second case: 45 jin of silk
絲_兩_2 = 8   # Second case: 8 liang of silk

# Total silk in the second case (convert to jin)
絲_總_2 = 絲_斤_2 + Fraction(絲_兩_2, 16)

# Ratio of silk to fabric
ratio = Fraction(縑_斤_1, 絲_斤_1)

# Calculate fabric obtained in the second case
a = ratio * 絲_總_2
"""
"""
