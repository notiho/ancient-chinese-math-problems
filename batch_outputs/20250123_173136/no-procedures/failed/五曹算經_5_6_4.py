"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
答曰：各 a鈞 。
"""

"""
Suppose there is expensive silk, where 1 liang costs 56 wen, and cheap silk, where 1 liang costs 42 wen. 
There is a total of 131,810 wen available. 
Question: how many *jin* (1 jin = 16 liang) of each type of silk can be purchased?

Answer: each type gets *a* jin.
"""

from fractions import Fraction

# Prices per liang
貴絲價格 = 56  # wen per liang
賤絲價格 = 42  # wen per liang

# Total money available
總錢 = 131810  # wen

# Let x be the amount of expensive silk in liang, and y be the amount of cheap silk in liang.
# We know:
# 貴絲價格 * x + 賤絲價格 * y = 總錢
# x + y = 總量 (in terms of liang)

# Solve for x and y:
# Multiply the second equation by 貴絲價格 to eliminate x:
# 貴絲價格 * x + 賤絲價格 * y = 總錢
# 貴絲價格 * x + 貴絲價格 * y = 貴絲價格 * 總量

# Subtract the two equations:
# (賤絲價格 - 貴絲價格) * y = 總錢 - 貴絲價格 * 總量

# Calculate the total amount of silk in liang:
總量 = 總錢 // ((貴絲價格 + 賤絲價格) // 2)

# Calculate the amount of cheap silk in liang:
賤絲量 = Fraction(總錢 - 貴絲價格 * 總量, 賤絲價格 - 貴絲價格)

# Calculate the amount of expensive silk in liang:
貴絲量 = 總量 - 賤絲量

# Convert to jin (1 jin = 16 liang):
a_貴絲 = 貴絲量 / 16
a_賤絲 = 賤絲量 / 16

a_貴絲, a_賤絲
"""
Missing variable in output: 'a'"""
