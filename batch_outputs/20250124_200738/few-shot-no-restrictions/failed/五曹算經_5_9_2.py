"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

#----- content starts here -----
"""
Suppose there is 238 guan and 573 wen of money in total, and it is desired to divide it into 92 units (mo).
Question: how much does each unit receive?

The procedure says: Place the total money of 238 guan and 573 wen, and divide it by 92 to obtain the result.

Answer: *a* guan and *b* wen.
"""

from fractions import Fraction

# Total money in wen (1 guan = 1000 wen)
total_money_wen = 238 * 1000 + 573

# Number of units (mo)
units = 92

# Divide total money by the number of units
money_per_unit = Fraction(total_money_wen, units)

# Convert the result into guan and wen
a = money_per_unit // 1000  # Whole guan
b = money_per_unit % 1000   # Remaining wen

# Output the result
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
