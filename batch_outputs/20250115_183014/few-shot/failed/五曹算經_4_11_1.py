"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""
Suppose there is an external corner (a square pyramid) filled with millet. The base perimeter is 48 chi, and the height is 6 chi.
Question: how much millet does it contain?

The procedure says: Take the base perimeter of 48 chi, multiply it by itself, obtaining 2304 chi².
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
體積 = Fraction(積2, 27)

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi)
斛法 = Fraction(162, 100)

# 以斛法除之即得
粟量 = 體積 / 斛法

# 分解為斛和分
a = int(粟量)  # 整數部分為斛
b = (粟量 - a) * 100  # 小數部分轉為分 (1斛 = 100分)

a = a  # 斛
b = int(b)  # 分
"""
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
