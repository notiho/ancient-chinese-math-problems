"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

#----- content starts here -----
"""
Suppose there is a total of 238 guan and 573 wen of money, and it is desired to divide it into 92 equal parts.
Question: how much money does each part receive?

The procedure says: Place the total money of 238 guan and 573 wen, and divide it by 92. The result is the amount per part.

Answer: *a* guan and *b* wen.
"""

from fractions import Fraction

# Total money in guan and wen
total_guan = 238
total_wen = 573

# Convert everything to wen (1 guan = 1000 wen)
total_wen += total_guan * 1000

# Number of parts
parts = 92

# Divide total wen by the number of parts
wen_per_part = Fraction(total_wen, parts)

# Convert back to guan and wen
a = wen_per_part // 1000  # Whole guan
b = wen_per_part % 1000   # Remaining wen

a = int(a)
b = int(b)

# Output
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 593"""
