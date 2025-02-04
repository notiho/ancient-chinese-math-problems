"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
答曰： a貫 奇足錢 b分 。
"""

#----- content starts here -----
"""
Suppose there are 238 guan and 573 wen in total, and it is desired to divide them into 92 bundles (陌).
Question: how much does each bundle contain?

Answer: each bundle contains *a* guan and *b* wen.
"""

# Total money in wen (1 guan = 1000 wen)
total_wen = 238 * 1000 + 573

# Number of bundles (陌)
bundles = 92

# Divide total wen by the number of bundles to get the amount per bundle
wen_per_bundle = Fraction(total_wen, bundles)

# Extract the integer part (a) and the remainder (b)
a = wen_per_bundle // 1000  # Number of guan
b = wen_per_bundle % 1000   # Remaining wen#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
