"""
今有半壁聚粟下周三十六尺高四尺五寸。問：粟㡬何？
術曰：列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得。
答曰： a斛 。
"""

"""
Suppose there is a half-wall storage of millet with a base circumference of 36 chi and a height of 4 chi and 5 cun.
Question: how much millet does it contain?

The procedure says: Take the base circumference of 36 chi, square it to get 1296 chi².
Multiply it by the height of 4 chi and 5 cun to get 5832 chi³.
Divide it by 18 to get 324 chi³.
Finally, divide it by the hu standard of 1 chi 6 cun 2 fen to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # Convert 5 cun to chi (1 cun = 1/10 chi)

# 列下周三十六尺自相乘得一千二百九十六尺
底積 = 下周 * 下周

# 以高四尺五寸乘之得五千八百三十二尺
體積 = 底積 * 高

# 以十八除之得三百二十四尺
體積除十八 = Fraction(體積, 18)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 6 cun and 2 fen to chi

# 以斛法除之即得
a = Fraction(體積除十八, 斛法)  # Result in hu
"""
"""
