"""
今有與人絲一十四斤，約得縑一十斤。今與人絲四十五斤八兩，問︰得縑幾何？
荅曰： a斤 。
"""

#----- content starts here -----
"""
Suppose you give someone 14 jin of silk, and in return, you receive 10 jin of woven silk fabric (jian).
Now, if you give someone 45 jin and 8 liang of silk, how much woven silk fabric (jian) will you receive?

Answer: *a* jin.
"""

# Conversion: 1 jin = 16 liang
# Given: 14 jin of silk produces 10 jin of woven silk fabric
silk_to_fabric_ratio = Fraction(10, 14)

# Convert 45 jin and 8 liang to total liang
total_liang = 45 * 16 + 8

# Convert total liang to jin
total_silk_in_jin = Fraction(total_liang, 16)

# Calculate the amount of woven silk fabric
a = total_silk_in_jin * silk_to_fabric_ratio

# Result
a#----- content ends here -----

"""
"""
