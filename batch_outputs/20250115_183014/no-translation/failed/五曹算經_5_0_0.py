"""
今有五百六十五户，户責絲一斤十一两八銖。問：計絲㡬何？
術曰：列一斤通作十六两，納十一两得二十七两；以二十四銖乘之、納八銖，得六百五十六銖；以乘户五百六十五，得三十七萬六百四十銖；以二十四銖除之，得一萬五千四百四十三两奇八銖；又以十六两除之，得九百六十五斤奇三两；以三十斤除之，得三十二鈞奇五斤；又以四鈞除之即得。
答曰： a石 b 两 c銖 。
"""

"""

"""


from fractions import Fraction

# 戶數
戶數 = 565

# 戶責絲一斤十一兩八銖
斤 = 1
兩 = 11
銖 = 8

# 列一斤通作十六兩，納十一兩得二十七兩
一斤 = 16
總兩 = 一斤 + 兩

# 以二十四銖乘之、納八銖，得六百五十六銖
一兩銖 = 24
總銖 = 總兩 * 一兩銖 + 銖

# 以乘戶五百六十五，得三十七萬六百四十銖
總銖_總 = 總銖 * 戶數

# 以二十四銖除之，得一萬五千四百四十三兩奇八銖
總兩_總 = 總銖_總 // 一兩銖
奇銖 = 總銖_總 % 一兩銖

# 又以十六兩除之，得九百六十五斤奇三兩
總斤 = 總兩_總 // 一斤
奇兩 = 總兩_總 % 一斤

# 以三十斤除之，得三十二鈞奇五斤
一鈞 = 30
總鈞 = 總斤 // 一鈞
奇斤 = 總斤 % 一鈞

# 又以四鈞除之即得
一石 = 4
總石 = 總鈞 // 一石
奇鈞 = 總鈞 % 一石

# 答案
a = 總石  # 石
b = 奇鈞 * 一鈞 + 奇斤  # 斤
c = 奇兩 * 一兩銖 + 奇銖  # 銖


"""

"""


"""
Variable 'a' has wrong value. Expected: 193/24, Actual: 8
Variable 'b' has wrong value. Expected: 3, Actual: 5
Variable 'c' has wrong value. Expected: 8, Actual: 80"""
