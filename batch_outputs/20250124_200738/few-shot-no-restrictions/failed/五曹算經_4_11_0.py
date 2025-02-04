"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

#----- content starts here -----
"""
Suppose there is a granary with an external circular base circumference of 48 chi and a height of 6 chi.
Question: how much millet does it hold?

The procedure says:
1. Take the circumference of the base (48 chi) and square it, obtaining 2304 chi².
2. Multiply this by the height (6 chi), obtaining 13824 chi³.
3. Divide this by 27 to account for the volume of a cylinder, obtaining 512 chi³.
4. Divide this by the volume of 1 hu, which is 1 chi 6 cun 2 fen (or 1.62 chi³), to get the number of hu.

Answer: *a* hu and *b* fen.
"""

from fractions import Fraction

# 下周四十八尺
周 = 48

# 高六尺
高 = 6

# 斛法一尺六寸二分 (1 chi 6 cun 2 fen = 1.62 chi³)
斛法 = Fraction(162, 100)

# Step 1: 自相乘得二千三百四尺
底積 = 周 ** 2

# Step 2: 以高六尺乘之得一萬三千八百二十四尺
體積 = 底積 * 高

# Step 3: 以二十七除之得五百一十二尺
有效體積 = Fraction(體積, 27)

# Step 4: 以斛法除之即得
斛數 = 有效體積 / 斛法

# Separate into hu and fractional fen
a = int(斛數)  # Whole hu
b = (斛數 - a) * 100  # Remaining fen (as a fraction of 100)

# Convert b to a fraction for exact representation
b = Fraction(b).limit_denominator()

a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 8, Actual: 400/81"""
