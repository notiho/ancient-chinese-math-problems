"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
答曰： a貫 奇足錢 b分 。
"""

#----- content starts here -----
"""
Suppose there are 238 guan and 573 wen of money, and it is desired to divide it into 92 *mo* (a unit of division).
Question: how much does each *mo* get?

Answer: each *mo* gets *a* guan and an additional *b* wen.
"""

# Total money in wen (1 guan = 1000 wen)
total_wen = 238 * 1000 + 573

# Number of mo
mo = 92

# Divide total money by the number of mo to get the amount per mo
per_mo_wen = Fraction(total_wen, mo)

# Convert the result into guan and wen
a = per_mo_wen // 1000  # Whole guan
b = per_mo_wen % 1000   # Remaining wen

a, b  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
