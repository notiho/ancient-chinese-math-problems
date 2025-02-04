"""
今有五百六十五户户責絲一斤十一两八銖問計絲㡬何
術曰列一斤通作十六两納十一两得二十七两以二十四銖乘之納八銖得六百五十六銖以乘户五百六十五得三十七萬六百四十銖以二十四銖除之得一萬五千四百四十三两奇八銖又以十六两除之得九百六十五斤奇三两以三十斤除之得三十二鈞奇五斤又以四鈞除之即得
答曰 a石 
"""

#----- content starts here -----
"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang. Add 11 liang, obtaining 27 liang.
Multiply this by 24 zhu, and add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide by 24 zhu, obtaining 15,443 liang with a remainder of 8 zhu.
Divide by 16 liang, obtaining 965 jin with a remainder of 3 liang.
Divide by 30 jin, obtaining 32 jun with a remainder of 5 jin.
Divide by 4 jun, obtaining the final result.

Answer: *a* shi.
"""

# 戶數
戶數 = 565

# 一斤通作十六两
一斤 = 16  # 1 jin = 16 liang

# 納十一两，得二十七两
總两 = 一斤 + 11

# 以二十四銖乘之，納八銖，得六百五十六銖
一戶銖 = (總两 * 24) + 8

# 以乘户五百六十五，得三十七萬六百四十銖
總銖 = 一戶銖 * 戶數

# 以二十四銖除之，得一萬五千四百四十三两奇八銖
總两 = 總銖 // 24
奇銖 = 總銖 % 24

# 又以十六两除之，得九百六十五斤奇三两
總斤 = 總两 // 16
奇两 = 総两 % 16

# 以三十斤除之，得三十二鈞奇五斤
總鈞 = 總斤 // 30
奇斤 = 總斤 % 30

# 又以四鈞除之，即得
總石 = 總鈞 // 4
奇鈞 = 總鈞 % 4

a = Fraction(總石)  # Final result in 石 (shi)#----- content ends here -----

"""
Code error: name '総两' is not defined"""
