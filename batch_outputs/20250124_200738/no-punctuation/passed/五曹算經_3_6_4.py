"""
今有錢二十七貫八百三十三文凡五文買棃三枚問得棃㡬何
術曰列錢二十七貫八百三十三文以三乘之得八萬三千四百九十九以五除之即得
答曰 a枚 奇 b文 
"""

#----- content starts here -----
"""
Suppose there are 27 strings of coins and 833 individual coins. 
For every 5 coins, 3 pears can be bought.
Question: how many pears can be obtained?

The procedure says: Arrange the total amount of coins, 27 strings and 833 coins.
Multiply it by 3, obtaining 83499.
Divide it by 5, obtaining the number of pears.
The remainder is the leftover coins.

Answer: *a* pears, with *b* coins remaining.
"""

# 錢二十七貫八百三十三文
貫 = 27
文 = 833

# 每貫為一千文
總文數 = 貫 * 1000 + 文

# 以三乘之
總文數乘三 = 3 * 總文數

# 以五除之
a = 總文數乘三 // 5  # 得到棃的枚數
b = 總文數乘三 % 5   # 剩餘的文數#----- content ends here -----

"""
"""
