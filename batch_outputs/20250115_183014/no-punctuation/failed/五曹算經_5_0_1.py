"""
今有五百六十五户户責絲一斤十一两八銖問計絲㡬何
術曰列一斤通作十六两納十一两得二十七两以二十四銖乘之納八銖得六百五十六銖以乘户五百六十五得三十七萬六百四十銖以二十四銖除之得一萬五千四百四十三两奇八銖又以十六两除之得九百六十五斤奇三两以三十斤除之得三十二鈞奇五斤又以四鈞除之即得
答曰 a石 b 两 c銖 
"""

"""
Suppose there are 565 households, each owing 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang. Add 11 liang to get 27 liang.
Multiply by 24 zhu and add 8 zhu to get 656 zhu.
Multiply by the 565 households to get 370,640 zhu.
Divide by 24 zhu to get 15,443 liang and 8 zhu remaining.
Divide by 16 liang to get 965 jin and 3 liang remaining.
Divide by 30 jin to get 32 jun and 5 jin remaining.
Divide by 4 jun to get the final result.

Answer: *a* shi, *b* liang, *c* zhu.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲 1斤11两8銖
斤 = 1
两 = 11
銖 = 8

# 1斤通作16两，納11两得27两
两總 = 16 * 斤 + 两

# 以24銖乘之，納8銖得656銖
銖總 = 24 * 两總 + 銖

# 以乘戶565，得370,640銖
總銖 = 銖總 * 戶數

# 以24銖除之，得15,443两奇8銖
總两 = 總銖 // 24
剩餘銖 = 總銖 % 24

# 以16两除之，得965斤奇3两
總斤 = 總两 // 16
剩餘两 = 總两 % 16

# 以30斤除之，得32鈞奇5斤
總鈞 = 總斤 // 30
剩餘斤 = 總斤 % 30

# 以4鈞除之，得石數
總石 = 總鈞 // 4
剩餘鈞 = 總鈞 % 4

# 答案
a = 總石
b = 剩餘两
c = 剩餘銖
"""
Variable 'a' has wrong value. Expected: 193/24, Actual: 8"""
