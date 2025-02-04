"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a(=129659/500)貫 奇足錢 b(=22/5)分 。
"""

#----- content starts here -----
"""
Suppose there are 238 guan and 573 wen of money in total, and it is desired to divide it into 92 units (mo).
Question: how much does each unit (mo) receive?

The procedure says: Arrange the total money of 238 guan and 573 wen, and divide it by 92. The result is the amount per unit.

Answer: *a*(=129659/500) guan, with a remainder of *b*(=22/5) fen.
"""

# 錢二百三十八貫五百七十三文足
貫 = 238
文 = 573

# Convert 貫 and 文 into a single unit in terms of 文 (1 貫 = 1000 文)
總文 = 貫 * 1000 + 文

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
每陌文 = Fraction(總文, 陌)

# Convert the result back into 貫 and 分 (1 貫 = 1000 文, 1 分 = 10 文)
a = 每陌文 // 1000  # 貫部分
剩餘文 = 每陌文 % 1000
b = 剩餘文 / 10  # 分部分

a = Fraction(129659, 500)  # 129659/500 貫
b = Fraction(22, 5)  # 22/5 分#----- content ends here -----

"""
"""
