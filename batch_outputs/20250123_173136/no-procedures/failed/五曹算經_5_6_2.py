"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
答曰：各 a鈞 。
"""

"""
Suppose there is expensive silk, 1 liang of which costs 56 wen, and cheap silk, 1 liang of which costs 42 wen. 
There is a total of 131,810 wen available. 
Question: how many *jin* (1 jin = 16 liang) of each type of silk can be purchased?

Answer: each gets *a* jin.
"""

from fractions import Fraction

# Prices per liang
貴絲價 = 56  # wen per liang
賤絲價 = 42  # wen per liang

# Total money available
總錢 = 131810  # wen

# Let x be the amount of expensive silk in liang, and y be the amount of cheap silk in liang.
# The total cost equation is:
# 貴絲價 * x + 賤絲價 * y = 總錢
# The total weight equation is:
# x + y = 總重量 (in liang)

# Solve for the total weight in liang:
總重量 = 總錢 / ((貴絲價 + 賤絲價) / 2)

# Calculate the amount of each type of silk in liang:
貴絲量_liang = Fraction(總重量 * 賤絲價, 貴絲價 + 賤絲價)
賤絲量_liang = Fraction(總重量 * 貴絲價, 貴絲價 + 賤絲價)

# Convert from liang to jin (1 jin = 16 liang):
貴絲量_jin = 貴絲量_liang / 16
賤絲量_jin = 賤絲量_liang / 16

# Results
a_貴絲 = 貴絲量_jin
a_賤絲 = 賤絲量_jin

a_貴絲, a_賤絲
"""
Code error: both arguments should be Rational instances"""
