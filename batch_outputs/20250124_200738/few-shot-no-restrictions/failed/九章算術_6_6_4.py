"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
術曰：置鹽二斛升數，以一百里乘之為法。以四十錢乘今負鹽升數，又以八十里乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose a laborer carries 2 hu of salt for 100 li and is paid 40 qian.
Now, the laborer carries 1 hu, 7 dou, 3 sheng, and half a sheng of salt for 80 li.
Question: how much should the laborer be paid?

The procedure says: Place the number of sheng in 2 hu of salt, and multiply it by 100 li to obtain the divisor.
Multiply 40 qian by the number of sheng in the current load of salt, and also multiply it by 80 li to obtain the dividend.
Divide the dividend by the divisor to obtain the payment in qian.

Answer: *a* qian.
"""

from fractions import Fraction

# Constants for unit conversions
HU_TO_SHENG = 100  # 1 hu = 100 sheng
DOU_TO_SHENG = 10  # 1 dou = 10 sheng

# Known values
鹽二斛 = 2 * HU_TO_SHENG  # Convert 2 hu to sheng
行一百里 = 100
與錢四十 = 40

# Current load of salt: 1 hu, 7 dou, 3 sheng, and half a sheng
負鹽 = 1 * HU_TO_SHENG + 7 * DOU_TO_SHENG + 3 + Fraction(1, 2)  # Convert to sheng
行八十里 = 80

# Procedure
# 法 = 鹽二斛升數 × 行一百里
法 = 鹽二斛 * 行一百里

# 實 = 與錢四十 × 負鹽升數 × 行八十里
實 = 與錢四十 * 負鹽 * 行八十里

# 實如法得一錢
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
