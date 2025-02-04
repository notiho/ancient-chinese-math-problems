"""
今有外角聚粟下周四十八尺高六尺問粟㡬何
術曰列下周四十八尺自相乘得二千三百四尺以高六尺乘之得一萬三千八百二十四尺以二十七除之得五百一十二尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

#----- content starts here -----
"""
Suppose there is an external granary filled with millet. The base circumference is 48 chi, and the height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base circumference of 48 chi, multiply it by itself, obtaining 2304 chi².
Multiply this by the height of 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Using the hu-divisor of 1 chi 6 cun 2 fen (1.62 chi), divide it, and the result is obtained.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘，得二千三百四尺
底積 = 下周 * 下周

# 以高六尺乘之，得一萬三千八百二十四尺
體積 = 底積 * 高

# 以二十七除之，得五百一十二尺
體積_簡化 = Fraction(體積, 27)

# 斛法一尺六寸二分 (1.62 尺)
斛法 = Fraction(162, 100)

# 以斛法除之，即得
總斛數 = Fraction(體積_簡化, 斛法)

# 分解為整斛和分
a = int(總斛數)  # 整斛
b = (總斛數 - a) * 100  # 分 (轉換為百分制)

a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 400/81"""
