"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a貫 奇足錢 b分 。
"""

"""
Suppose there is 238 guan and 573 wen of money in total, and it is desired to divide it into 92 units (mo).
Question: how much does each unit (mo) receive?

The procedure says: Place the total money of 238 guan and 573 wen, and divide it by 92. The result is obtained.

Answer: *a* guan and *b* wen.
"""

# 列錢二百三十八貫五百七十三文足
總錢 = 238 * 1000 + 573  # Convert guan to wen (1 guan = 1000 wen)

# 以九十二除之
每陌 = Fraction(總錢, 92)

# 取整數部分為貫
a = 每陌 // 1000  # Convert back to guan (integer part)

# 取餘數部分為文
b = 每陌 % 1000  # Remaining wen after converting to guan
"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
