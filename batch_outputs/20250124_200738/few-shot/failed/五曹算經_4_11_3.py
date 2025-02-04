"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is an external corner (a square pyramid) filled with millet. The base perimeter is 48 chi, and the height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base perimeter of 48 chi, multiply it by itself to get 2304 chi².
Multiply this by the height of 6 chi to get 13824 chi³.
Divide this by 27 to get 512 chi³.
Finally, divide this by the volume of 1 hu (1 chi 6 cun 2 fen) to get the result.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 列下周四十八尺，自相乘得二千三百四尺
積1 = 下周 * 下周  # 48 * 48 = 2304

# 以高六尺乘之得一萬三千八百二十四尺
積2 = 積1 * 高  # 2304 * 6 = 13824

# 以二十七除之得五百一十二尺
體積 = Fraction(積2, 27)  # 13824 / 27 = 512

# 斛法一尺六寸二分
斛法 = Fraction(1, 1) + Fraction(6, 10) + Fraction(2, 100)  # 1 chi 6 cun 2 fen = 1.62 chi³

# 以斛法除之即得
總斛 = 體積 / 斛法  # 512 / 1.62

# 分解成斛和分
a = int(總斛)  # 整數部分為斛
b = (總斛 - a) * 100  # 小數部分轉換為分 (1斛 = 100分)

a = a  # 斛
b = round(b)  # 分#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 5"""
