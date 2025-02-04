"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
術曰：列一斤通作十六两，納十一两得二十七两；以二十四銖乘之、納八銖，得六百五十六銖；以乘户五百六十五，得三十七萬六百四十銖；以二十四銖除之，得一萬五千四百四十三两奇八銖；又以十六两除之，得九百六十五斤奇三两；以三十斤除之，得三十二鈞奇五斤；又以四鈞除之即得。
答曰： a石 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang, and add 11 liang, obtaining 27 liang.
Multiply this by 24 zhu, and add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide this by 24 zhu, obtaining 15,443 liang and 8 zhu.
Divide this by 16 liang, obtaining 965 jin and 3 liang.
Divide this by 30 jin, obtaining 32 jun and 5 jin.
Finally, divide this by 4 jun to obtain the total in shi.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲：1斤11兩8銖
斤 = 1
兩 = 11
銖 = 8

# 列一斤通作十六两，納十一两得二十七两
兩總 = 16 * 斤 + 兩

# 以二十四銖乘之、納八銖，得六百五十六銖
銖總 = 24 * 兩總 + 銖

# 以乘户五百六十五，得三十七萬六百四十銖
總銖 = 銖總 * 戶數

# 以二十四銖除之，得一萬五千四百四十三两奇八銖
總兩 = 總銖 // 24
剩餘銖 = 總銖 % 24

# 又以十六两除之，得九百六十五斤奇三两
總斤 = 總兩 // 16
剩餘兩 = 總兩 % 16

# 以三十斤除之，得三十二鈞奇五斤
總鈞 = 總斤 // 30
剩餘斤 = 總斤 % 30

# 又以四鈞除之即得
總石 = Fraction(總鈞, 4)

a = 總石
#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
