"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
答曰： a貫 奇足錢 b分 。
"""

"""
Suppose there are 238 guan and 573 wen of money, and it is desired to divide it into 92 bundles (mo).
Question: how much does each bundle contain?

Answer: each bundle contains *a* guan and *b* wen.
"""

from fractions import Fraction

# Total money in wen (1 guan = 1000 wen)
total_wen = 238 * 1000 + 573

# Number of bundles (mo)
bundles = 92

# Divide total money by the number of bundles
wen_per_bundle = Fraction(total_wen, bundles)

# Convert to guan and wen
a = wen_per_bundle // 1000  # Whole guan
b = wen_per_bundle % 1000   # Remaining wen

# Results
a = int(a)  # Convert to integer for guan
b = int(b)  # Convert to integer for wen
"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 593"""
