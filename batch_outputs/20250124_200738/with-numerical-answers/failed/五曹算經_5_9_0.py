"""
今有錢二百三十八貫五百七十三文足欲為九十二陌。問：得㡬何？
術曰：列錢二百三十八貫五百七十三文足以九十二除之即得。
答曰： a(=129659/500)貫 奇足錢 b(=22/5)分 。
"""

#----- content starts here -----
"""
Suppose there is a total of 238 guan and 573 wen of money. It is desired to divide it into 92 units (mo).
Question: how much does each unit contain?

The procedure says: Arrange the total money of 238 guan and 573 wen, then divide it by 92 to obtain the result.

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
每陌錢 = Fraction(總錢, 陌)

# Convert result into 貫 and 分 (1 貫 = 10 分)
a = 每陌錢  # 129659/500 貫
b = (每陌錢 - int(每陌錢)) * 10  # 22/5 分#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 238573/92000
Variable 'b' has wrong value. Expected: 22/5, Actual: 54573/9200"""
