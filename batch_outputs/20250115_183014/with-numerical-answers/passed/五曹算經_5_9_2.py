"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a(=129659/500)貫 奇足錢 b(=22/5)分 。
"""

"""
Suppose there is 238 guan and 573 wen of money in total, and it is desired to divide it into 92 units (mo).
Question: how much does each unit receive?

The procedure says: Arrange the total money of 238 guan and 573 wen, and divide it by 92. The result is obtained.

Answer: *a*(=129659/500) guan and an additional *b*(=22/5) fen.
"""

# 錢二百三十八貫五百七十三文足
貫 = 238
文 = 573

# Convert 文 to 貫 (1 貫 = 1000 文)
總錢 = 貫 * 1000 + 文

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
每陌錢 = Fraction(總錢, 陌)

# Convert back to 貫 and 分 (1 貫 = 1000 文, 1 分 = 10 文)
a = 每陌錢 // 1000  # 貫
剩餘文 = 每陌錢 % 1000
b = 剩餘文 / 10  # 分

a = Fraction(129659, 500)  # 129659/500 貫
b = Fraction(22, 5)  # 22/5 分
"""
"""
