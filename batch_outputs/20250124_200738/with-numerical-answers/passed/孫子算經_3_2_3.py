"""
今有平地聚粟，下周三丈六尺，高四尺五寸。問：粟幾何？
術曰：置周三丈六尺，自相乘，得一千二百九十六尺，以高四尺五寸，乘之，得五千八百三十二尺，以三十六除之，得一百六十二尺，以斛法一尺六寸二分除之，即得。
答曰： a(=100)斛 。
"""

#----- content starts here -----
"""
Suppose there is a flat ground with a pile of millet. The base circumference is 3 zhang 6 chi, and the height is 4 chi 5 cun.
Question: how much millet is there?

The procedure says: Place the circumference of 3 zhang 6 chi, square it, obtaining 1296 chi.
Multiply it by the height of 4 chi 5 cun, obtaining 5832 chi.
Divide it by 36, obtaining 162 chi.
Divide it by the hu-divisor of 1 chi 6 cun 2 fen, and the result is obtained.

Answer: *a*(=100) hu.
"""

# 下周三丈六尺
周 = 3 * 10 + 6  # Convert zhang and chi to chi

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # Convert chi and cun to chi

# 置周三丈六尺，自相乘
積 = 周 * 周  # Square the circumference

# 得一千二百九十六尺
assert 積 == 1296  # Verify the intermediate result

# 以高四尺五寸，乘之
體積 = 積 * 高  # Multiply by the height

# 得五千八百三十二尺
assert 體積 == 5832  # Verify the intermediate result

# 以三十六除之
體積 = Fraction(體積, 36)  # Divide by 36

# 得一百六十二尺
assert 體積 == 162  # Verify the intermediate result

# 以斛法一尺六寸二分除之
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert chi, cun, and fen to chi
a = Fraction(體積, 斛法)  # Divide by the hu-divisor

# 答曰：100斛
assert a == 100  # Verify the final result#----- content ends here -----

"""
"""
