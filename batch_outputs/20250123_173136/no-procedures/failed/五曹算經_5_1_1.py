"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household contribute?

Answer: each household contributes *a* jin.
"""

# Total households
戶數 = 565

# Total silk owed in units of shi, jin, liang, and zhu
絲_石 = 8
絲_斤 = 5
絲_兩 = 3
絲_銖 = 8

# Conversion factors:
# 1 石 = 100 斤
# 1 斤 = 16 兩
# 1 兩 = 24 銖

# Convert everything to 銖 (smallest unit)
總絲_銖 = (絲_石 * 100 * 16 * 24) + (絲_斤 * 16 * 24) + (絲_兩 * 24) + 絲_銖

# Divide by the number of households to get silk per household in 銖
戶出絲_銖 = Fraction(總絲_銖, 戶數)

# Convert back to jin (斤), liang (兩), and zhu (銖)
戶出絲_斤 = 戶出絲_銖 // (16 * 24)  # Whole jin
剩餘_銖 = 戶出絲_銖 % (16 * 24)  # Remaining zhu after jin

戶出絲_兩 = 剩餘_銖 // 24  # Whole liang
戶出絲_銖 = 剩餘_銖 % 24  # Remaining zhu after liang

# Final answer
a = f"{戶出絲_斤}斤 {戶出絲_兩}兩 {戶出絲_銖}銖"
a
"""
Variable 'a' has wrong value. Expected: 41/24, Actual: 1斤 6兩 2176/113銖"""
