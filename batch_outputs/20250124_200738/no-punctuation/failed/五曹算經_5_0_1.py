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
Multiply by 24 zhu, and add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide by 24 zhu, obtaining 15,443 liang and 8 zhu remaining.
Divide by 16 liang, obtaining 965 jin and 3 liang remaining.
Divide by 30 jin, obtaining 32 jun and 5 jin remaining.
Divide by 4 jun, obtaining the result.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲：1斤11兩8銖
斤 = 1
兩 = 11
銖 = 8

# 1斤 = 16兩
斤轉兩 = 16
總兩 = 斤 * 斤轉兩 + 兩  # 轉換為兩
總兩 = 總兩 * 24 + 銖  # 1兩 = 24銖，轉換為銖

# 總銖
總銖 = 總兩 * 戶數

# 以24銖除之，得總兩
總兩 = 總銖 // 24
剩餘銖 = 總銖 % 24

# 以16兩除之，得總斤
總斤 = 總兩 // 16
剩餘兩 = 總兩 % 16

# 以30斤除之，得總鈞
總鈞 = 總斤 // 30
剩餘斤 = 總斤 % 30

# 以4鈞除之，得總石
總石 = 總鈞 // 4
剩餘鈞 = 總鈞 % 4

a = Fraction(總石)  # 答案以石為單位#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
