"""
今有軍糧米三千二百四十六斛八斗七升，每斛直錢四百八十二文。問：計㡬何？
術曰：列米三千二百四十六斛八斗七升，以四百八十二文乘之即得。
答曰： a貫 。
"""

#----- content starts here -----
"""
Suppose there is military grain rice amounting to 3246 hu, 8 dou, and 7 sheng. 
Each hu is worth 482 wen. 
Question: what is the total value?

The procedure says: Place the rice amount of 3246 hu, 8 dou, and 7 sheng. 
Multiply it by 482 wen to obtain the total.

The answer says: *a* guan.
"""

from fractions import Fraction

# 米三千二百四十六斛八斗七升
米 = 3246 + Fraction(8, 10) + Fraction(7, 100)

# 每斛直錢四百八十二文
每斛價 = 482

# 以四百八十二文乘之即得
總價文 = 米 * 每斛價

# 1貫 = 1000文
a = Fraction(總價文, 1000)  # Convert to 貫
#----- content ends here -----

"""
"""
