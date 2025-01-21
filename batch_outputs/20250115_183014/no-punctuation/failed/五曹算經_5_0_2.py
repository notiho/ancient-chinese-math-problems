"""
今有五百六十五户户責絲一斤十一两八銖問計絲㡬何
術曰列一斤通作十六两納十一两得二十七两以二十四銖乘之納八銖得六百五十六銖以乘户五百六十五得三十七萬六百四十銖以二十四銖除之得一萬五千四百四十三两奇八銖又以十六两除之得九百六十五斤奇三两以三十斤除之得三十二鈞奇五斤又以四鈞除之即得
答曰 a石 b 两 c銖 
"""

"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang. Add 11 liang, obtaining 27 liang.
Multiply this by 24 zhu, and add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide this by 24 zhu, obtaining 15,443 liang with a remainder of 8 zhu.
Divide this by 16 liang, obtaining 965 jin with a remainder of 3 liang.
Divide this by 30 jin, obtaining 32 jun with a remainder of 5 jin.
Finally, divide this by 4 jun to obtain the number of shi.

Answer: *a* shi, *b* liang, *c* zhu.
"""

# 戶數
戶數 = 565

# 每戶責絲：1斤11兩8銖
斤 = 1
兩 = 11
銖 = 8

# 列一斤通作十六两
一斤 = 16

# 納十一两，得二十七两
總兩 = 一斤 + 兩

# 以二十四銖乘之
一兩 = 24
總銖 = 總兩 * 一兩

# 納八銖，得六百五十六銖
總銖 += 銖

# 以乘户五百六十五，得三十七萬六百四十銖
總銖 *= 戶數

# 以二十四銖除之，得一萬五千四百四十三两奇八銖
總兩 = 總銖 // 一兩
剩餘銖 = 總銖 % 一兩

# 以十六两除之，得九百六十五斤奇三两
總斤 = 總兩 // 一斤
剩餘兩 = 總兩 % 一斤

# 以三十斤除之，得三十二鈞奇五斤
一鈞 = 30
總鈞 = 總斤 // 一鈞
剩餘斤 = 總斤 % 一鈞

# 以四鈞除之，即得
一石 = 4
總石 = 總鈞 // 一石
剩餘鈞 = 總鈞 % 一石

a = 總石
b = 剩餘鈞 * 一鈞 + 剩餘斤
c = 剩餘兩 * 一兩 + 剩餘銖
"""
Variable 'a' has wrong value. Expected: 193/24, Actual: 8
Variable 'b' has wrong value. Expected: 3, Actual: 5
Variable 'c' has wrong value. Expected: 8, Actual: 80"""
