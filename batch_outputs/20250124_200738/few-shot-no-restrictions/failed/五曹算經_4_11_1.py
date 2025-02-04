"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a granary in the shape of a circular cone, with a base circumference of 48 chi and a height of 6 chi.
Question: how much millet does it hold?

The procedure says: Take the base circumference of 48 chi, square it to get 2304 chi².
Multiply this by the height of 6 chi to get 13824 chi³.
Divide this by 27 to get 512 chi³.
Finally, divide by the volume of 1 hu (1 chi 6 cun 2 fen) to obtain the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)

# 列下周四十八尺，自相乘得二千三百四尺
底積 = 下周 ** 2

# 以高六尺乘之得一萬三千八百二十四尺
體積 = 底積 * 高

# 以二十七除之得五百一十二尺
體積 = Fraction(體積, 27)

# 以斛法一尺六寸二分除之即得
粟斛 = Fraction(體積, 斛法)

# 分解為整斛和餘分
a = 粟斛.numerator // 粟斛.denominator  # 整斛
b = 粟斛.numerator % 粟斛.denominator  # 餘分

# 答案
a斛 = a
b分 = b
#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
