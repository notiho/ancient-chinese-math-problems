"""
今有七百三十八户，共請絲二十七斤五两。問：户得㡬何？
答曰： a銖 奇 b銖 。
"""

"""
Suppose there are 738 households, and together they request 27 jin and 5 liang of silk.
Question: how much silk does each household get?

Answer: each household gets *a* zhu and an additional *b* zhu.
"""

# Total households
戶數 = 738

# Total silk in jin and liang
絲_斤 = 27
絲_兩 = 5

# Convert silk to zhu (1 jin = 16 liang, 1 liang = 24 zhu)
總絲_銖 = (絲_斤 * 16 + 絲_兩) * 24

# Divide total silk by the number of households
每戶_銖 = Fraction(總絲_銖, 戶數)

# Extract the integer part (a) and the remainder (b)
a = 每戶_銖.numerator // 每戶_銖.denominator
b = 每戶_銖.numerator % 每戶_銖.denominator

a, b
"""
Variable 'a' has wrong value. Expected: 1421/100, Actual: 14
Variable 'b' has wrong value. Expected: 51/50, Actual: 26"""
