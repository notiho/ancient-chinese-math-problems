"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
術曰：列一斤通作十六两，納十一两得二十七两；以二十四銖乘之、納八銖，得六百五十六銖；以乘户五百六十五，得三十七萬六百四十銖；以二十四銖除之，得一萬五千四百四十三两奇八銖；又以十六两除之，得九百六十五斤奇三两；以三十斤除之，得三十二鈞奇五斤；又以四鈞除之即得。
答曰： a(=4633/576)石 。
"""

"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang, and add 11 liang to obtain 27 liang.
Multiply this by 24 zhu and add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 376,640 zhu.
Divide this by 24 zhu to obtain 15,443 liang and 8 zhu.
Divide this by 16 liang to obtain 965 jin and 3 liang.
Divide this by 30 jin to obtain 32 jun and 5 jin.
Finally, divide this by 4 jun to obtain the total in shi.

Answer: *a*(=4633/576) shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 每戶責絲：1斤11兩8銖
斤 = 1
兩 = 11
銖 = 8

# 列一斤通作十六两，納十一两得二十七两
兩 = 16 * 斤 + 兩  # 27兩

# 以二十四銖乘之、納八銖，得六百五十六銖
銖 = 24 * 兩 + 銖  # 656銖

# 以乘户五百六十五，得三十七萬六百四十銖
總銖 = 戶數 * 銖  # 376640銖

# 以二十四銖除之，得一萬五千四百四十三两奇八銖
總兩 = Fraction(總銖, 24)  # 15443兩 and 8銖

# 又以十六两除之，得九百六十五斤奇三两
總斤 = Fraction(總兩, 16)  # 965斤 and 3兩

# 以三十斤除之，得三十二鈞奇五斤
總鈞 = Fraction(總斤, 30)  # 32鈞 and 5斤

# 又以四鈞除之即得
總石 = Fraction(總鈞, 4)  # 4633/576石

a = 總石  # 4633/576石
"""
"""
