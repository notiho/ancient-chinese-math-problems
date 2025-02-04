"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

"""
Suppose there is 238 guan and 573 wen of money in total, and it is desired to divide it into 92 units (mo).
Question: how much does each unit get?

The procedure says: Place the total money of 238 guan and 573 wen, and divide it by 92. The result is obtained.

Answer: *a* guan and the remainder is *b* wen.
"""

from fractions import Fraction

# 錢二百三十八貫五百七十三文足
貫 = 238
文 = 573

# Convert everything to wen (1 貫 = 1000 文)
總文 = 貫 * 1000 + 文

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
每陌文 = Fraction(總文, 陌)

# Convert back to 貫 and 文
a = 每陌文 // 1000  # Whole 貫
b = 每陌文 % 1000   # Remaining 文
"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
