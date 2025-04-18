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

# 每戶責絲一斤十一兩八銖
斤 = 1
兩 = 11
銖 = 8

# 術曰：列一斤通作十六两
一斤 = 16

# 納十一两得二十七两
總兩 = 斤 * 一斤 + 兩  # 1 * 16 + 11 = 27

# 以二十四銖乘之、納八銖，得六百五十六銖
一兩 = 24
總銖 = 總兩 * 一兩 + 銖  # 27 * 24 + 8 = 656

# 以乘户五百六十五，得三十七萬六百四十銖
總銖_戶 = 總銖 * 戶數  # 656 * 565 = 370640

# 以二十四銖除之，得一萬五千四百四十三两奇八銖
總兩_戶 = divmod(總銖_戶, 一兩)  # 370640 ÷ 24 = 15443 余 8
總兩 = 總兩_戶[0]
奇銖 = 總兩_戶[1]

# 又以十六两除之，得九百六十五斤奇三两
總斤_戶 = divmod(總兩, 一斤)  # 15443 ÷ 16 = 965 余 3
總斤 = 総斤_戶[0]
奇兩 = 總斤_戶[1]

# 以三十斤除之，得三十二鈞奇五斤
一鈞 = 30
總鈞_戶 = divmod(總斤, 一鈞)  # 965 ÷ 30 = 32 余 5
總鈞 = 總鈞_戶[0]
奇斤 = 總鈞_戶[1]

# 又以四鈞除之即得
一石 = 4
總石_戶 = divmod(總鈞, 一石)  # 32 ÷ 4 = 8 余 0
總石 = 總石_戶[0]
奇鈞 = 總石_戶[1]

# 答曰：a石 b两 c銖
a = 總石
b = 奇兩
c = 奇銖


"""

"""


"""
Code error: name '総斤_戶' is not defined"""
