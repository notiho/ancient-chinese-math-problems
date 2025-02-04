"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is an external corner (a square pyramid) filled with millet. Its base perimeter is 48 chi, and its height is 6 chi.
Question: how much millet does it contain?

The procedure says:
- Take the base perimeter of 48 chi and square it, obtaining 2304 chi².
- Multiply this by the height of 6 chi, obtaining 13824 chi³.
- Divide this by 27, obtaining 512 chi³.
- Finally, divide this by the volume of 1 hu, which is 1 chi³ 6 cun 2 fen (or 1.62 chi³), to obtain the result.

The answer says: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
下周 = 48

# 高六尺
高 = 6

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)

# 列下周四十八尺，自相乘得二千三百四尺
基面積 = 下周 ** 2

# 以高六尺乘之得一萬三千八百二十四尺
體積 = 基面積 * 高

# 以二十七除之得五百一十二尺
體積 = Fraction(體積, 27)

# 以斛法一尺六寸二分除之即得
斛數 = 體積 / 斛法

# 分解為整斛和餘分
a = int(斛數)  # 整斛數
b = (斛數 - a) * 100  # 餘分 (轉換為百分制)

# 答案
a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 400/81"""
