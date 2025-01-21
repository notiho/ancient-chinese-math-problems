"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
術曰：列一斤通作十六两，納十一两得二十七两；以二十四銖乘之、納八銖，得六百五十六銖；以乘户五百六十五，得三十七萬六百四十銖；以二十四銖除之，得一萬五千四百四十三两奇八銖；又以十六两除之，得九百六十五斤奇三两；以三十斤除之，得三十二鈞奇五斤；又以四鈞除之即得。
答曰： a(=193/24)石 b(=3) 两 c(=8)銖 。
"""

"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: 
Convert 1 jin to 16 liang, add 11 liang to get 27 liang.
Multiply this by 24 zhu, add 8 zhu, to get 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide by 24 zhu to get 15,443 liang and 8 zhu.
Divide by 16 liang to get 965 jin and 3 liang.
Divide by 30 jin to get 32 jun and 5 jin.
Finally, divide by 4 jun to get the total in shi.

Answer: *a*(=193/24) shi, *b*(=3) liang, *c*(=8) zhu.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲：1斤11两8銖
斤 = 1
两 = 11
銖 = 8

# 1斤通作16两，納11两得27两
两總 = 16 * 斤 + 两

# 以24銖乘之，納8銖，得656銖
銖總 = 24 * 两總 + 銖

# 以乘户565，得370,640銖
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

# 以4鈞除之，得石
總石 = Fraction(總鈞, 4)

# 答案
a = 總石  # 193/24 石
b = 剩餘两  # 3 两
c = 剩餘銖  # 8 銖
"""
Variable 'a' has wrong value. Expected: 193/24, Actual: 8"""
