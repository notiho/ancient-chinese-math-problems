"""
今有錢二十七貫八百三十三文凡五文買棃三枚問得棃㡬何
術曰列錢二十七貫八百三十三文以三乘之得八萬三千四百九十九以五除之即得
答曰 a枚 奇 b文 
"""

"""
Suppose there are 27 guan and 833 wen in total. For every 5 wen, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Place the total amount of money, 27 guan and 833 wen.
Multiply it by 3, obtaining 83499.
Divide it by 5, and the result is the number of pears.
The remainder is the leftover wen.

Answer: *a* pears, with *b* wen remaining.
"""

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 1 貫 = 1000 文
總文數 = 貫 * 1000 + 文

# 每五文買三枚棃
每五文得棃 = 3

# 以三乘之
總棃數 = 每五文得棃 * 總文數

# 以五除之
a = 總棃數 // 5  # 棃的整數部分
b = 總棃數 % 5   # 剩餘文數
"""
"""
