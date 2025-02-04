"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is an external granary (a circular cone) filled with millet. Its base circumference is 48 chi, and its height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base circumference of 48 chi, square it to get 2304 chi².
Multiply it by the height of 6 chi to get 13824 chi³.
Divide it by 27 to get 512 chi³.
Finally, divide it by the volume of 1 hu, which is 1 chi 6 cun 2 fen (or 1.62 chi³), to get the result.

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
體積 = Fraction(體積, 27)

# 以斛法一尺六寸二分除之即得
斛數 = 體積 // 斛法  # Integer part (a hu)
餘數 = 體積 % 斛法  # Remainder (b fen)

# Convert the remainder to fen (1 hu = 1.62 chi³, so 1 fen = 1/100 of 1.62 chi³)
餘數分 = (餘數 / 斛法) * 100

# Final result
a = int(斛數)  # Number of hu
b = int(餘數分)  # Number of fen

a, b  # Output the result as a斛 奇 b分#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
