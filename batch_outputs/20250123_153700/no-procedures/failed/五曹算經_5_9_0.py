"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
答曰： a貫 奇足錢 b分 。
"""

"""
Suppose there are 238 guan and 573 wen of money, and it is desired to divide it into 92 bundles (mo).
Question: how much does each bundle contain?

Answer: each bundle contains *a* guan and *b* wen.
"""

# Total money in wen (1 guan = 1000 wen)
total_wen = 238 * 1000 + 573

# Number of bundles (mo)
bundles = 92

# Divide total money by the number of bundles to get the amount per bundle
per_bundle_wen = Fraction(total_wen, bundles)

# Convert to guan and wen
a = per_bundle_wen // 1000  # Whole guan
b = per_bundle_wen % 1000  # Remaining wen

a, b
"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
