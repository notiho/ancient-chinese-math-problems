"""
今有平地聚粟，下周三丈六尺，高四尺五寸。問：粟幾何？
術曰：置周三丈六尺，自相乘，得一千二百九十六尺，以高四尺五寸，乘之，得五千八百三十二尺，以三十六除之，得一百六十二尺，以斛法一尺六寸二分除之，即得。
答曰： a(=100)斛 。
"""

#----- content starts here -----
"""
Suppose there is a flat ground with a pile of millet. The base circumference is 3 zhang and 6 chi, and the height is 4 chi and 5 cun.
Question: how much millet is there?

The procedure says: Place the circumference of 3 zhang and 6 chi, square it, obtaining 1296 chi².
Multiply it by the height of 4 chi and 5 cun, obtaining 5832 chi³.
Divide it by 36, obtaining 162 chi³.
Divide it by the hu-divisor of 1 chi 6 cun 2 fen, obtaining the result.

Answer: *a*(=100) hu.
"""

from fractions import Fraction

# 下周三丈六尺
周 = 3 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # Convert cun to chi (1 chi = 10 cun)

# 置周三丈六尺，自相乘
積 = 周 * 周  # Square the circumference

# 以高四尺五寸，乘之
體積 = 積 * 高  # Multiply by height

# 以三十六除之
體積 = Fraction(體積, 36)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert to chi (1 chi = 10 cun, 1 cun = 10 fen)

# 以斛法除之，即得
a = Fraction(體積, 斛法)  # 100 hu#----- content ends here -----

"""
"""
