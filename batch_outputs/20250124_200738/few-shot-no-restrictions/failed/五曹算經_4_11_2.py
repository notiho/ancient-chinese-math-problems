"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a granary with an external circular base circumference of 48 chi and a height of 6 chi.
Question: how much millet does it hold?

The procedure says: Take the circumference of the base, 48 chi, and square it, obtaining 2304 chi².
Multiply this by the height, 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Finally, divide this by the volume of 1 hu, which is 1 chi 6 cun 2 fen (or 1.62 chi³), to get the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)  # 1.62 as a fraction

# 列下周四十八尺，自相乘得二千三百四尺
下周平方 = 下周 ** 2

# 以高六尺乘之得一萬三千八百二十四尺
體積 = 下周平方 * 高

# 以二十七除之得五百一十二尺
體積除以27 = Fraction(體積, 27)

# 以斛法一尺六寸二分除之即得
粟斛 = 體積除以27 / 斛法

# 分解為整斛和餘分
a = int(粟斛)  # 整斛
b = (粟斛 - a) * 100  # 餘分 (轉換為百分制)

# 答案
a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 400/81"""
