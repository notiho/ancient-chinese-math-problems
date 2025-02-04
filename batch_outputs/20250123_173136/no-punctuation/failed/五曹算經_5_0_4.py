"""
今有五百六十五户户責絲一斤十一两八銖問計絲㡬何
術曰列一斤通作十六两納十一两得二十七两以二十四銖乘之納八銖得六百五十六銖以乘户五百六十五得三十七萬六百四十銖以二十四銖除之得一萬五千四百四十三两奇八銖又以十六两除之得九百六十五斤奇三两以三十斤除之得三十二鈞奇五斤又以四鈞除之即得
答曰 a石 
"""

"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang. Add 11 liang, obtaining 27 liang.
Multiply this by 24 zhu, and add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide this by 24 zhu, obtaining 15,443 liang and 8 zhu remaining.
Divide this by 16 liang, obtaining 965 jin and 3 liang remaining.
Divide this by 30 jin, obtaining 32 jun and 5 jin remaining.
Divide this by 4 jun, obtaining the total in shi.

Answer: *a* shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲 1斤11两8銖
斤 = 1
两 = 11
銖 = 8

# 1斤通作16两，納11两，得27两
总两 = 16 * 斤 + 两

# 以24銖乘之，納8銖，得656銖
总銖 = 24 * 总两 + 銖

# 以乘户565，得370640銖
總銖 = 总銖 * 戶數

# 以24銖除之，得15443两奇8銖
總兩 = 總銖 // 24
剩餘銖 = 總銖 % 24

# 以16两除之，得965斤奇3两
總斤 = 總兩 // 16
剩餘兩 = 總兩 % 16

# 以30斤除之，得32鈞奇5斤
總鈞 = 總斤 // 30
剩餘斤 = 總斤 % 30

# 以4鈞除之，即得石
總石 = 總鈞 // 4
剩餘鈞 = 總鈞 % 4

a = 總石
"""
Variable 'a' has wrong value. Expected: 4633/576, Actual: 8"""
