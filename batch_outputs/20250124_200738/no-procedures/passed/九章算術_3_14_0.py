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

# Conversion factors
# 1 jin = 16 liang
jin_to_liang = 16

# Known ratio of silk to fabric
silk_given = 14  # in jin
fabric_obtained = 10  # in jin

# Ratio of silk to fabric
ratio = Fraction(fabric_obtained, silk_given)

# Silk given in the second case
silk_given_2 = 45 + Fraction(8, jin_to_liang)  # Convert 45 jin 8 liang to jin

# Calculate fabric obtained
a = silk_given_2 * ratio

# Result
a#----- content ends here -----

"""
"""
