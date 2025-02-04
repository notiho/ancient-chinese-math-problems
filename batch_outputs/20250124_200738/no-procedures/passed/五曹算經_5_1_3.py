"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households collectively responsible for producing 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household produce?

Answer: each household produces *a* jin.
"""

# Total number of households
戶數 = 565

# Total silk in units of shi, jin, liang, and zhu
絲_石 = 8
絲_斤 = 5
絲_兩 = 3
絲_銖 = 8

# Conversion factors:
# 1 石 = 120 斤
# 1 斤 = 16 兩
# 1 兩 = 24 銖

# Convert everything to zhu for calculation
總絲_銖 = (絲_石 * 120 * 16 * 24) + (絲_斤 * 16 * 24) + (絲_兩 * 24) + 絲_銖

# Divide by the number of households to get silk per household in zhu
戶出絲_銖 = Fraction(總絲_銖, 戶數)

# Convert back to jin (1 斤 = 16 兩 = 384 銖)
a = Fraction(戶出絲_銖, 384)  # Each household's contribution in jin

a  # Output the result#----- content ends here -----

"""
"""
