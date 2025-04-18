"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 米三千二百四十六斛八斗七升
米 = 3246 + Fraction(8, 10) + Fraction(7, 100)

# 每斛直錢四百八十二文
每斛價 = 482

# 以四百八十二文乘之即得
總價 = 米 * 每斛價

# 換算為貫（1貫 = 1000文）
a = Fraction(總價, 1000)
#----- content ends here -----


"""

"""


"""
"""
