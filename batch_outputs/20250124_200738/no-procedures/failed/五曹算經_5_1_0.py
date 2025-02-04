"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 。
"""

#----- content starts here -----
"""
Suppose there are 565 households collectively responsible for contributing 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

Answer: each household contributes *a* jin.
"""

# Total households
戶數 = 565

# Total silk in units of shi, jin, liang, and zhu
絲_石 = 8
絲_斤 = 5
絲_兩 = 3
絲_銖 = 8

# Conversion factors
石_to_斤 = 120  # 1 石 = 120 斤
斤_to_兩 = 16   # 1 斤 = 16 兩
兩_to_銖 = 24   # 1 兩 = 24 銖

# Convert everything to 銖 (smallest unit)
總絲_銖 = (
    絲_石 * 石_to_斤 * 斤_to_兩 * 兩_to_銖 +
    絲_斤 * 斤_to_兩 * 兩_to_銖 +
    絲_兩 * 兩_to_銖 +
    絲_銖
)

# Divide total silk in 銖 by the number of households
戶均絲_銖 = Fraction(總絲_銖, 戶數)

# Convert back to jin (primary unit)
戶均絲_斤 = 戶均絲_銖 // (斤_to_兩 * 兩_to_銖)  # Whole jin
剩餘_銖 = 戶均絲_銖 % (斤_to_兩 * 兩_to_銖)  # Remaining zhu

戶均絲_兩 = 剩餘_銖 // 兩_to_銖  # Whole liang
剩餘_銖 = 剩餘_銖 % 兩_to_銖  # Remaining zhu

戶均絲_銖 = 剩餘_銖  # Remaining zhu

# Final answer in jin, liang, and zhu
a = (戶均絲_斤, 戶均絲_兩, 戶均絲_銖)
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 41/24, Actual: (1, 11, Fraction(8, 1))"""
