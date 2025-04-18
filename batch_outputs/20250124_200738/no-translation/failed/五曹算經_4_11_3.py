"""
今有外角聚粟下周四十八尺高六尺。問：粟㡬何？
術曰：列下周四十八尺，自相乘得二千三百四尺；以高六尺乘之得一萬三千八百二十四尺，以二十七除之得五百一十二尺。以斛法一尺六寸二分除之即得。
答曰： a斛 奇 b分 。
"""

"""

"""

#----- content starts here -----

from fractions import Fraction

# 列下周四十八尺
下周 = 48

# 自相乘得二千三百四尺
積 = 下周 * 下周

# 以高六尺乘之
高 = 6
體積 = 積 * 高

# 以二十七除之
體積 = Fraction(體積, 27)

# 斛法一尺六寸二分
斛法 = Fraction(1) + Fraction(6, 10) + Fraction(2, 100)

# 以斛法除之即得
粟 = Fraction(體積, 斛法)

# 分解為斛和分
a = int(粟)  # 整數部分為斛
b = (粟 - a) * 100  # 小數部分轉為分
b = int(b)  # 取整數部分

# 答案
a斛 = a
b分 = b
#----- content ends here -----


"""

"""


"""
Variable 'b' has wrong value. Expected: 8, Actual: 4"""
