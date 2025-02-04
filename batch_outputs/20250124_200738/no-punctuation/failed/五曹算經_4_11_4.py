"""
今有外角聚粟下周四十八尺高六尺問粟㡬何
術曰列下周四十八尺自相乘得二千三百四尺以高六尺乘之得一萬三千八百二十四尺以二十七除之得五百一十二尺以斛法一尺六寸二分除之即得
答曰 a斛 奇 b分 
"""

#----- content starts here -----
"""
Suppose there is an external granary filled with millet. The base circumference is 48 chi, and the height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base circumference of 48 chi and multiply it by itself, obtaining 2304 chi².
Multiply this by the height of 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Using the hu-divisor of 1 chi 6 cun 2 fen (1.62 chi), divide it to obtain the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘
積 = 下周 * 下周  # 得 2304 尺²

# 以高六尺乘之
體積 = 積 * 高  # 得 13824 尺³

# 以二十七除之
體積_斛單位 = Fraction(體積, 27)  # 得 512 尺³

# 斛法一尺六寸二分 (1.62 尺)
斛法 = Fraction(162, 100)  # 1.62 尺

# 除以斛法
粟量 = 體積_斛單位 / 斛法

# 分離整數部分 (a 斛) 和小數部分 (b 分)
a = int(粟量)  # 斛數
b = (粟量 - a) * 100  # 分數部分，轉換為百分制

a = a  # 斛
b = round(b)  # 分#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 5"""
