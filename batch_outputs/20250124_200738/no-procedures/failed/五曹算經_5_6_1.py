"""
今有貴絲一两直錢五十六文，賤絲一两直錢四十二文，有錢一百三十一貫八百一十文。問：各得㡬何？
答曰：各 a鈞 。
"""

#----- content starts here -----
"""
Suppose there is expensive silk, where 1 liang costs 56 wen, and cheap silk, where 1 liang costs 42 wen.
There is a total of 131,810 wen available. 
Question: how much of each type of silk can be purchased?

Answer: *a* jun (a unit of weight).
"""

# 貴絲一兩直錢五十六文
貴絲價 = 56

# 賤絲一兩直錢四十二文
賤絲價 = 42

# 總錢數
總錢 = 131810

# Let 貴絲重量 = x (in liang), 賤絲重量 = y (in liang)
# The total cost equation is:
# 56x + 42y = 131810
# The total weight equation (in jun) is:
# x + y = a (where a is the total weight in jun)

# To simplify, convert the total weight to liang (1 jun = 100 liang):
總重量 = Fraction(131810, 貴絲價 + 賤絲價)

# 貴絲重量 (x) = (賤絲價 / (貴絲價 + 賤絲價)) * 總重量
貴絲重量 = Fraction(賤絲價, 貴絲價 + 賤絲價) * 總重量

# 賤絲重量 (y) = (貴絲價 / (貴絲價 + 賤絲價)) * 總重量
賤絲重量 = Fraction(貴絲價, 貴絲價 + 賤絲價) * 總重量

# Convert the total weight back to jun
a = Fraction(總重量, 100)

# Final results
貴絲重量_in_jun = Fraction(貴絲重量, 100)
賤絲重量_in_jun = Fraction(賤絲重量, 100)

# Outputs
貴絲重量_in_jun, 賤絲重量_in_jun#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 269/96, Actual: 269/20"""
