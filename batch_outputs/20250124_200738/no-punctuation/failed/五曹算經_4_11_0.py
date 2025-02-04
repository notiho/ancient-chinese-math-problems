"""
今有外角聚粟下周四十八尺高六尺問粟㡬何
術曰列下周四十八尺自相乘得二千三百四尺以高六尺乘之得一萬三千八百二十四尺以二十七除之得五百一十二尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

#----- content starts here -----
"""
Suppose there is an external granary filled with millet. Its base circumference is 48 chi, and its height is 6 chi.
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
積 = 下周 * 下周

# 以高六尺乘之，得一萬三千八百二十四尺
體積 = 積 * 高

# 以二十七除之，得五百一十二尺
體積 = Fraction(體積, 27)

# 斛法一尺六寸二分 (1.62 尺)
斛法 = Fraction(162, 100)

# 以斛法除之，即得
總斛 = 體積 / 斛法

# 整數部分為斛
a = int(總斛)

# 小數部分轉為分 (1 斛 = 100 分)
b = int((總斛 - a) * 100)#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
