"""
今有五百六十五户户責絲一斤十一两八銖問計絲㡬何
術曰列一斤通作十六两納十一两得二十七两以二十四銖乘之納八銖得六百五十六銖以乘户五百六十五得三十七萬六百四十銖以二十四銖除之得一萬五千四百四十三两奇八銖又以十六两除之得九百六十五斤奇三两以三十斤除之得三十二鈞奇五斤又以四鈞除之即得
答曰 a石 
"""

"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang. Add 11 liang, obtaining 27 liang.
Multiply by 24 zhu, and add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide by 24 zhu, obtaining 15,443 liang and 8 zhu remaining.
Divide by 16 liang, obtaining 965 jin and 3 liang remaining.
Divide by 30 jin, obtaining 32 jun and 5 jin remaining.
Divide by 4 jun, obtaining the total in shi.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲：1斤11兩8銖
斤 = 1
兩 = 11
銖 = 8

# 一斤通作十六兩
斤為兩 = 16
總兩 = 斤 * 斤為兩 + 兩  # 納十一兩得二十七兩
總兩 = 27

# 以二十四銖乘之
兩為銖 = 24
總銖 = 總兩 * 兩為銖  # 乘二十四銖
總銖 += 銖  # 納八銖得六百五十六銖
總銖 = 656

# 以乘戶五百六十五
總銖 *= 戶數  # 得三十七萬六百四十銖
總銖 = 370640

# 以二十四銖除之
總兩 = 總銖 // 兩為銖  # 得一萬五千四百四十三兩
剩餘銖 = 總銖 % 兩為銖  # 奇八銖

# 又以十六兩除之
總斤 = 總兩 // 斤為兩  # 得九百六十五斤
剩餘兩 = 總兩 % 斤為兩  # 奇三兩

# 以三十斤除之
斤為鈞 = 30
總鈞 = 總斤 // 斤為鈞  # 得三十二鈞
剩餘斤 = 總斤 % 斤為鈞  # 奇五斤

# 又以四鈞除之
鈞為石 = 4
總石 = 總鈞 // 鈞為石  # 得石數
剩餘鈞 = 總鈞 % 鈞為石

# 答案
a = Fraction(總石)  # 答曰 a石
"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
