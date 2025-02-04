"""
今有錢二十七貫八百三十三文凡五文買棃三枚問得棃㡬何
術曰列錢二十七貫八百三十三文以三乘之得八萬三千四百九十九以五除之即得
答曰 a枚 奇 b文 
"""

#----- content starts here -----
"""
Suppose there are 27 guan and 833 wen of money in total. 
For every 5 wen, 3 pears can be bought.
Question: how many pears can be bought, and how much money is left over?

The procedure says: Place the money, 27 guan and 833 wen. Multiply it by 3, obtaining 83499. Divide it by 5, obtaining the number of pears. The remainder is the leftover wen.

Answer: *a* pears, with *b* wen left over.
"""

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 每貫有 1000 文
總文數 = 貫 * 1000 + 文

# 以三乘之
總文數乘三 = 3 * 總文數

# 以五除之
a = 總文數乘三 // 5  # 得到棃的枚數
b = 總文數乘三 % 5   # 得到剩餘的文數#----- content ends here -----

"""
"""
