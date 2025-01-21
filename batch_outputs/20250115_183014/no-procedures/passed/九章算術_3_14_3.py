"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
荅曰： a斤 。
"""

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

# Given silk in jin and liang
給絲_斤 = 45
給絲_兩 = 8

# Convert given silk to total liang
給絲_總兩 = 給絲_斤 * 一斤 + 給絲_兩

# Calculate the amount of fabric in liang
得縑_總兩 = ratio * 給絲_總兩

# Convert the result back to jin and liang
得縑_斤 = 得縑_總兩 // 一斤
得縑_兩 = 得縑_總兩 % 一斤

# Final answer in jin
a = Fraction(得縑_總兩, 一斤)  # Represent the result as a fraction of jin

a
"""
"""
