"""
今有錢二百三十八貫五百七十三文足欲為九十二陌問得㡬何
術曰列錢二百三十八貫五百七十三文足以九十二除之即得
答曰 a貫 奇足錢 b分 
"""

"""
Suppose there are 238 guan and 573 wen of money in total. It is desired to convert this into 92 mo.
Question: how much does each mo get?

The procedure says: Place the 238 guan and 573 wen of money in total. Divide it by 92, and the result is obtained.

Answer: *a* guan and *b* wen.
"""

# 錢二百三十八貫五百七十三文足
錢 = 238 * 1000 + 573  # Convert guan to wen (1 guan = 1000 wen)

# 欲為九十二陌
陌 = 92

# 以九十二除之
每陌錢 = Fraction(錢, 陌)

# 得貫數與餘文數
a = 每陌錢 // 1000  # Whole guan
b = 每陌錢 % 1000   # Remaining wen
"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/92"""
