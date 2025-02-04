"""
今有平地聚粟，下周三丈六尺，高四尺五寸。問：粟幾何？
術曰：置周三丈六尺，自相乘，得一千二百九十六尺，以高四尺五寸，乘之，得五千八百三十二尺，以三十六除之，得一百六十二尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of millet on flat ground. The base circumference is 3 zhang and 6 chi, and the height is 4 chi and 5 cun.
Question: how much millet is there?

The procedure says: Take the circumference of 3 zhang and 6 chi, square it, obtaining 1296 chi².
Multiply it by the height of 4 chi and 5 cun, obtaining 5832 chi³.
Divide this by 36, obtaining 162 chi³.
Finally, divide it by the volume of 1 hu (1 chi 6 cun 2 fen), obtaining the number of hu.

Answer: *a* hu.
"""

from fractions import Fraction

# 下周三丈六尺
周 = 3 * 10 + 6  # Convert zhang and chi to total chi

# 高四尺五寸
高 = 4 + Fraction(5, 10)  # Convert chi and cun to total chi

# 斛法一尺六寸二分
斛法 = 1 + Fraction(6, 10) + Fraction(2, 100)  # Convert chi, cun, and fen to total chi

# 置周三丈六尺，自相乘
周平方 = 周 ** 2

# 得一千二百九十六尺，以高四尺五寸，乘之
體積 = 周平方 * 高

# 得五千八百三十二尺，以三十六除之
體積除以三十六 = Fraction(體積, 36)

# 以斛法一尺六寸二分除之，即得
a = Fraction(體積除以三十六, 斛法)

# Output the result
a#----- content ends here -----

"""
"""
