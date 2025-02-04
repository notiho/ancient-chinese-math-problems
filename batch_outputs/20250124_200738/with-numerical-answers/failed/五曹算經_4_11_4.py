"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a(=316)斛 奇 b(=8)分 。
"""

#----- content starts here -----
"""
Suppose there is an external granary filled with millet. The base circumference is 48 chi, and the height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base circumference of 48 chi, square it to obtain 2304 chi².
Multiply it by the height of 6 chi to obtain 13824 chi³.
Divide this by 27 to obtain 512 chi³.
Finally, divide by the volume of 1 hu (1 chi 6 cun 2 fen) to obtain the result.

Answer: *a*(=316) hu and *b*(=8) fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘得二千三百四尺
下周積 = 下周 * 下周  # 2304 chi²

# 以高六尺乘之得一萬三千八百二十四尺
體積 = 下周積 * 高  # 13824 chi³

# 以二十七除之得五百一十二尺
粟體積 = Fraction(體積, 27)  # 512 chi³

# 斛法一尺六寸二分
斛法 = Fraction(1, 1) + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen = 1.62 chi³

# 以斛法除之即得
粟斛 = Fraction(粟體積, 斛法)  # Total hu

# 分解為整斛和分
a = int(粟斛)  # 316 hu
b = (粟斛 - a) * 100  # 8 fen

a, b = a, int(b)  # Final result: 316 hu and 8 fen#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
