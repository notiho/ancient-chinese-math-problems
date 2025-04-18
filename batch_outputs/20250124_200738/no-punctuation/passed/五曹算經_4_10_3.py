"""
今有半壁聚粟下周三十六尺高四尺五寸問粟㡬何
術曰列下周三十六尺自相乘得一千二百九十六尺以高四尺五寸乘之得五千八百三十二尺以十八除之得三百二十四尺以斛法一尺六寸二分除之即得
答曰 a斛 
"""

#----- content starts here -----
"""
Suppose there is a semi-cylindrical granary with a base circumference of 36 chi and a height of 4 chi and 5 cun.
Question: how much millet does it hold?

The procedure says: Take the base circumference of 36 chi, square it to get 1296 chi².
Multiply this by the height of 4 chi and 5 cun to get 5832 chi³.
Divide this by 18 to get 324 chi³.
Finally, divide this by the hu-divisor of 1 chi 6 cun 2 fen to obtain the result.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三十六尺
下周 = 36

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # Convert 5 cun to chi (1 cun = 1/10 chi)

# 列下周三十六尺，自相乘
下周平方 = 下周 * 下周

# 以高四尺五寸乘之
體積 = 下周平方 * 高

# 以十八除之
體積除以十八 = Fraction(體積, 18)

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert 6 cun and 2 fen to chi

# 以斛法除之，即得
a = Fraction(體積除以十八, 斛法)  # Final result in hu#----- content ends here -----

"""
"""
