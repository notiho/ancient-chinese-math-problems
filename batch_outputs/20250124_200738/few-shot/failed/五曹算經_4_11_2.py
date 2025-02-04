"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a granary with an outer circular base circumference of 48 chi and a height of 6 chi.
Question: how much millet does it hold?

The procedure says: Take the base circumference of 48 chi, multiply it by itself, obtaining 2304 chi².
Multiply this by the height of 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen (1.62 chi), obtaining the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘得二千三百四尺
積1 = 下周 * 下周

# 以高六尺乘之得一萬三千八百二十四尺
積2 = 積1 * 高

# 以二十七除之得五百一十二尺
積3 = Fraction(積2, 27)

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)

# 以斛法除之即得
總斛 = 積3 / 斛法

# 整數部分為斛數
a = int(總斛)

# 小數部分轉換為分 (1 hu = 100 fen)
b = int((總斛 - a) * 100)

a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
