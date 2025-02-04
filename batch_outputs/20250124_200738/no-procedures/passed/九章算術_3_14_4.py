"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose 14 jin of silk is given to someone, and in return, 10 jin of silk fabric (jian) is obtained.
Now, if 45 jin and 8 liang of silk are given, how much silk fabric (jian) will be obtained?

Answer: *a* jin.
"""

# Conversion constants
一斤 = 16  # 1 jin = 16 liang

# Known ratio of silk to fabric
絲_斤 = 14
縑_斤 = 10

# Ratio of silk to fabric
ratio = Fraction(縑_斤, 絲_斤)

# Silk given in the second case
絲_第二次_斤 = 45
絲_第二次_兩 = 8
絲_第二次_總量 = 絲_第二次_斤 + Fraction(絲_第二次_兩, 一斤)

# Calculate the amount of fabric obtained
a = ratio * 絲_第二次_總量#----- content ends here -----

"""
"""
