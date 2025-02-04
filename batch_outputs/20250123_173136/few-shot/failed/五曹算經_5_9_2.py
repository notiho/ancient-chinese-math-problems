"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

"""
Suppose there is 238 guan and 573 wen of money in total, and it is desired to divide it into 92 units (mo).
Question: how much does each unit receive?

The procedure says: Place the total money of 238 guan and 573 wen, and divide it by 92. The result is obtained.

The answer says: *a* guan and *b* wen.
"""

# 錢二百三十八貫五百七十三文足
總錢 = 238 * 1000 + 573  # Convert guan to wen (1 guan = 1000 wen)

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
每陌錢 = Fraction(總錢, 陌)

# 答曰：a貫 奇足錢 b分
a = 每陌錢 // 1000  # Extract the guan part
b = 每陌錢 % 1000  # Extract the remaining wen part
"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
