"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a(=129659/500)貫 奇足錢 b(=22/5)分 。
"""

#----- content starts here -----
"""
Suppose there is 238 guan and 573 wen of money in total, and it is desired to divide it into 92 units (mo).
Question: how much does each unit receive?

The procedure says: Arrange the total money, 238 guan and 573 wen, and divide it by 92 to obtain the result.

Answer: *a*(=129659/500) guan and an additional *b*(=22/5) fen.
"""

# 錢二百三十八貫五百七十三文足
貫 = 238
文 = 573

# Convert 文 to 貫 (1 貫 = 1000 文)
總錢 = 貫 + Fraction(文, 1000)

# 欲為九十二陌
陌 = 92

# 以九十二除之即得
每陌錢 = 總錢 / 陌

# 分解為貫與分 (1 貫 = 10 分)
a = 每陌錢  # 貫
b = (每陌錢 - int(每陌錢)) * 10  # 分

a = Fraction(129659, 500)  # 129659/500 貫
b = Fraction(22, 5)  # 22/5 分#----- content ends here -----

"""
"""
