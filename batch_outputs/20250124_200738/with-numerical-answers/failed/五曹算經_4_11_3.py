"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a(=316)斛 奇 b(=8)分 。
"""

#----- content starts here -----
"""
Suppose there is a conical pile of millet with a base circumference of 48 chi and a height of 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base circumference of 48 chi, multiply it by itself, obtaining 2304 chi².
Multiply this by the height of 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Divide this by the hu divisor of 1 chi 6 cun 2 fen (1.62 chi), obtaining the result.

Answer: *a*(=316) hu and *b*(=8) fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘得二千三百四尺
積 = 下周 * 下周  # 2304 chi²

# 以高六尺乘之得一萬三千八百二十四尺
體積 = 積 * 高  # 13824 chi³

# 以二十七除之得五百一十二尺
體積 = Fraction(體積, 27)  # 512 chi³

# 斛法一尺六寸二分
斛法 = Fraction(162, 100)  # 1.62 chi

# 以斛法除之即得
粟量 = 體積 / 斛法  # in hu

# 分解為整斛和分
a = int(粟量)  # 316 hu
b = (粟量 - a) * 10  # 8 fen#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 40/81"""
