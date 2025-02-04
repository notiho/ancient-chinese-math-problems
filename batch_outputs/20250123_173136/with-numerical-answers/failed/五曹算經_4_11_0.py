"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a(=316)斛 奇 b(=8)分 。
"""

"""
Suppose there is an external corner (a square-based pyramid) filled with millet. 
Its base perimeter is 48 chi, and its height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base perimeter of 48 chi, multiply it by itself, obtaining 2304 chi².
Multiply this by the height of 6 chi, obtaining 13824 chi³.
Divide this by 27, obtaining 512 chi³.
Divide this by the hu-divisor of 1 chi 6 cun 2 fen (1.62 chi), and the result is obtained.

Answer: *a*(=316) hu and *b*(=8) fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘得二千三百四尺
基面積 = 下周 * 下周

# 以高六尺乘之得一萬三千八百二十四尺
體積 = 基面積 * 高

# 以二十七除之得五百一十二尺
體積簡化 = Fraction(體積, 27)

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)

# 以斛法除之即得
粟量 = Fraction(體積簡化, 斛法)

# 分離整數部分和分數部分
a =粟量.numerator // 粟量.denominator  # 316斛
b =粟量 -a
"""
Variable 'b' has wrong value. Expected: 8, Actual: 4/81"""
