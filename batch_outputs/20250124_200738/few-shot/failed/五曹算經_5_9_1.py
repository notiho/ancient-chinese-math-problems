"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

#----- content starts here -----
"""
Suppose there are 238 guan and 573 wen in total. It is desired to divide this into 92 units (mo).
Question: how much does each unit receive?

The procedure says: Place the total amount of money, 238 guan and 573 wen, and divide it by 92. The result is the amount per unit.

Answer: *a* guan and the remainder *b* wen.
"""

from fractions import Fraction

# 錢二百三十八貫五百七十三文足
貫 = 238
文 = 573

# Convert everything to wen (1 貫 = 1000 文)
總文數 = 貫 * 1000 + 文

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
每陌文數 = Fraction(總文數, 陌)

# Convert back to 貫 and 文
a = 每陌文數 // 1000  # Whole 貫
b = 每陌文數 % 1000   # Remaining 文#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
