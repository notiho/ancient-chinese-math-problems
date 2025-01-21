"""
今有五百六十五户，共責絲八石五斤三两八銖。問：户出絲㡬何？
答曰： a斤 b 两 c銖 。
"""

"""
Suppose there are 565 households, and together they owe 8 shi, 5 jin, 3 liang, and 8 zhu of silk.
Question: how much silk does each household owe?

Answer: each household owes *a* jin, *b* liang, and *c* zhu.
"""

# Total silk owed
絲_石 = 8  # 1 石 = 100 斤
絲_斤 = 5  # 1 斤 = 16 兩
絲_兩 = 3  # 1 兩 = 24 銖
絲_銖 = 8

# Convert everything to zhu for easier calculations
總絲_銖 = (絲_石 * 100 * 16 * 24) + (絲_斤 * 16 * 24) + (絲_兩 * 24) + 絲_銖

# Total households
戶數 = 565

# Divide total silk (in zhu) by the number of households
每戶_銖 = 總絲_銖 // 戶數
剩餘_銖 = 總絲_銖 % 戶數

# Convert back to jin, liang, and zhu
a = 每戶_銖 // (16 * 24)  # Convert to jin
剩餘_銖 = 每戶_銖 % (16 * 24)

b = 剩餘_銖 // 24  # Convert to liang
c = 剩餘_銖 % 24  # Remaining zhu

# Final result
a, b, c
"""
Variable 'b' has wrong value. Expected: 11, Actual: 6
Variable 'c' has wrong value. Expected: 8, Actual: 19"""
