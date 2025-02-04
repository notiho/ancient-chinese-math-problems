"""
今有錢二百三十八貫五百七十三文足欲為九十二陌問得㡬何
術曰列錢二百三十八貫五百七十三文足以九十二除之即得
答曰 a貫 奇足錢 b分 
"""

#----- content starts here -----
"""
Suppose there are 238 guan and 573 wen of money in total. It is desired to convert this into 92 mo.
Question: how much does each mo contain?

The procedure says: Arrange the money as 238 guan and 573 wen. Divide this by 92, and the result is obtained.

Answer: *a* guan and the remainder is *b* wen.
"""

# 錢二百三十八貫五百七十三文足
貫 = 238
文 = 573

# 每貫等於1000文，將貫轉換為文
總文 = 貫 * 1000 + 文

# 欲為九十二陌
陌 = 92

# 以九十二除之
每陌文 = Fraction(總文, 陌)

# 將結果轉換為貫和文
a = 每陌文.numerator // 每陌文.denominator  # 貫
b = 每陌文.numerator % 每陌文.denominator  # 奇足錢 (文)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 129659/500, Actual: 2593
Variable 'b' has wrong value. Expected: 22/5, Actual: 17"""
