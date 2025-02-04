"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a(=316)斛 奇 b(=8)分 。
"""

#----- content starts here -----
"""
Suppose there is a granary with an external circular base circumference of 48 chi and a height of 6 chi.
Question: how much millet does it hold?

The procedure says: Place the base circumference of 48 chi, multiply it by itself, obtaining 2304 chi².
Multiply this by the height of 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen (1.62 chi), obtaining the result.

Answer: *a*(=316) hu and *b*(=8) fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘得二千三百四尺
基面積 = 下周 * 下周  # 2304

# 以高六尺乘之得一萬三千八百二十四尺
體積 = 基面積 * 高  # 13824

# 以二十七除之得五百一十二尺
體積除以27 = Fraction(體積, 27)  # 512

# 斛法一尺六寸二分 (1.62 尺)
斛法 = Fraction(162, 100)  # 1.62

# 以斛法除之即得
粟量 = Fraction(體積除以27, 斛法)

# 整數部分為斛數
a = int(粟量)  # 316

# 小數部分轉為分 (1斛 = 10分)
b = int((粟量 - a) * 10)  # 8#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 0"""
