"""
今有平地聚粟下周三丈六尺高四尺五寸問粟幾何
術曰置周三丈六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以三十六除之得一百六十二尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

"""
Suppose there is a pile of millet on flat ground. Its base circumference is 3 zhang and 6 chi, and its height is 4 chi and 5 cun.
Question: how much millet is there?

The procedure says: Take the circumference of 3 zhang and 6 chi, square it, obtaining 1296 chi².
Multiply it by the height of 4 chi and 5 cun, obtaining 5832 chi³.
Divide it by 36, obtaining 162 chi³.
Divide it by the dou-measure of 1 chi 6 cun 2 fen, and the result is obtained.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三丈六尺
周 = 3 * 10 + 6  # Convert zhang to chi (1 zhang = 10 chi)

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # Convert cun to chi (1 chi = 10 cun)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert cun and fen to chi

# 置周三丈六尺，自相乘得一千二百九十六尺
積 = 周 * 周

# 以高四尺五寸乘之，得五千八百三十二尺
體積 = 積 * 高

# 以三十六除之，得一百六十二尺
體積 = Fraction(體積, 36)

# 以斛法一尺六寸二分除之，即得
a = Fraction(體積, 斛法)  # Result in hu
"""
"""
