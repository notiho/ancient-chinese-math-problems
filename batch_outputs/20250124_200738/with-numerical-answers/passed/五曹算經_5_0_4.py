"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
術曰：列一斤通作十六两，納十一两得二十七两；以二十四銖乘之、納八銖，得六百五十六銖；以乘户五百六十五，得三十七萬六百四十銖；以二十四銖除之，得一萬五千四百四十三两奇八銖；又以十六两除之，得九百六十五斤奇三两；以三十斤除之，得三十二鈞奇五斤；又以四鈞除之即得。
答曰： a(=4633/576)石 。
"""

#----- content starts here -----
"""
Suppose there are 565 households, and each household owes 1 jin, 11 liang, and 8 zhu of silk.
Question: how much silk is owed in total?

The procedure says: Represent 1 jin as 16 liang, add 11 liang to get 27 liang.
Multiply this by 24 zhu, add 8 zhu, obtaining 656 zhu.
Multiply this by the 565 households, obtaining 370,640 zhu.
Divide by 24 zhu, obtaining 15,443 liang and 8 zhu.
Divide this by 16 liang, obtaining 965 jin and 3 liang.
Divide this by 30 jin, obtaining 32 jun and 5 jin.
Divide this by 4 jun to obtain the final result.

Answer: *a*(=4633/576) shi.
"""

from fractions import Fraction

# 戶數
戶數 = 565

# 戶責絲一斤十一两八銖
斤 = 1
两 = 11
銖 = 8

# 列一斤通作十六两，納十一两得二十七两
斤為两 = 16
總两 = 斤 * 斤為两 + 两  # 27两

# 以二十四銖乘之、納八銖，得六百五十六銖
两為銖 = 24
總銖 = 總两 * 两為銖 + 銖  # 656銖

# 以乘户五百六十五，得三十七萬六百四十銖
總銖 *= 戶數  # 370640銖

# 以二十四銖除之，得一萬五千四百四十三两奇八銖
總两 = 總銖 // 两為銖  # 15443两
剩餘銖 = 總銖 % 两為銖  # 8銖

# 又以十六两除之，得九百六十五斤奇三两
總斤 = 總两 // 斤為两  # 965斤
剩餘两 = 總两 % 斤為两  # 3两

# 以三十斤除之，得三十二鈞奇五斤
斤為鈞 = 30
總鈞 = 總斤 // 斤為鈞  # 32鈞
剩餘斤 = 總斤 % 斤為鈞  # 5斤

# 又以四鈞除之即得
鈞為石 = 4
總石 = Fraction(總鈞, 鈞為石) + Fraction(剩餘斤, 鈞為石 * 斤為鈞) + Fraction(剩餘两, 鈞為石 * 斤為鈞 * 斤為两) + Fraction(剩餘銖, 鈞為石 * 斤為鈞 * 斤為两 * 两為銖)

a = 總石  # 4633/576石#----- content ends here -----

"""
"""
