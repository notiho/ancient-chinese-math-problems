"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
術曰：置鹽二斛升數，以一百里乘之為法。以四十錢乘今負鹽升數，又以八十里乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose a laborer carries 2 hu of salt for 100 li and is paid 40 qian.
Now, the laborer carries 1 hu, 7 dou, 3 sheng, and half a sheng of salt for 80 li.
Question: how much money should the laborer be paid?

The procedure says: Place the number of sheng in 2 hu of salt and multiply it by 100 li to obtain the divisor.
Multiply the 40 qian by the number of sheng in the current load of salt, and also multiply it by 80 li to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of qian.

Answer: *a* qian.
"""

from fractions import Fraction

# Constants
一斛 = 10  # 1 hu = 10 dou
一斗 = 10  # 1 dou = 10 sheng

# Known values
鹽_二斛 = 2 * 一斛 * 一斗  # Total sheng in 2 hu
行程_一百里 = 100  # Distance in li
報酬_四十錢 = 40  # Payment in qian

# Current load of salt
負鹽_一斛七斗三升少半升 = (
    1 * 一斛 * 一斗  # 1 hu
    + 7 * 一斗  # 7 dou
    + 3  # 3 sheng
    + Fraction(1, 2)  # half a sheng
)

行程_八十里 = 80  # Distance in li

# Procedure
# 法 = 鹽二斛升數 × 一百里
法 = 鹽_二斛 * 行程_一百里

# 實 = 四十錢 × 今負鹽升數 × 八十里
實 = 報酬_四十錢 * 負鹽_一斛七斗三升少半升 * 行程_八十里

# 實如法得一錢
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
