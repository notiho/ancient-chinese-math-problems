"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
術曰：列一斤通作十六两，納十一两得二十七两；以二十四銖乘之、納八銖，得六百五十六銖；以乘户五百六十五，得三十七萬六百四十銖；以二十四銖除之，得一萬五千四百四十三两奇八銖；又以十六两除之，得九百六十五斤奇三两；以三十斤除之，得三十二鈞奇五斤；又以四鈞除之即得。
答曰： a(=4633/576)石 。
"""

"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says:
Convert 1 jin into 16 liang, add 11 liang to get 27 liang.
Multiply this by 24 zhu, add 8 zhu to get 656 zhu.
Multiply this by the 565 households to get 370,640 zhu.
Divide by 24 zhu to get 15,443 liang and 8 zhu.
Divide by 16 liang to get 965 jin and 3 liang.
Divide by 30 jin to get 32 jun and 5 jin.
Finally, divide by 4 jun to get the total in shi.

Answer: *a*(=4633/576) shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲：1斤11两8銖
斤 = 1
两 = 11
銖 = 8

# 列一斤通作十六两，納十一两得二十七两
两總 = 16 * 斤 + 两  # 27两

# 以二十四銖乘之、納八銖，得六百五十六銖
銖總 = 24 * 两總 + 銖  # 656銖

# 以乘户五百六十五，得三十七萬六百四十銖
總銖 = 銖總 * 戶數  # 370,640銖

# 以二十四銖除之，得一萬五千四百四十三两奇八銖
總两 = 總銖 // 24  # 15,443两
餘銖 = 總銖 % 24  # 8銖

# 又以十六两除之，得九百六十五斤奇三两
總斤 = 總两 // 16  # 965斤
餘两 = 總两 % 16  # 3两

# 以三十斤除之，得三十二鈞奇五斤
總鈞 = 總斤 // 30  # 32鈞
餘斤 = 總斤 % 30  # 5斤

# 又以四鈞除之即得
總石 = Fraction(總鈞, 4) + Fraction(餘斤, 120) + Fraction(餘两, 1920) + Fraction(餘銖, 46080)

a = 總石  # 4633/576石
"""
"""
