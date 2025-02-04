"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
術曰：置鹽二斛升數，以一百里乘之為法。以四十錢乘今負鹽升數，又以八十里乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

"""
Suppose a porter carries 2 hu of salt for 100 li and is paid 40 qian.
Now, the porter carries 1 hu, 7 dou, 3 sheng, and half a sheng of salt for 80 li.
Question: how much should the porter be paid?

The procedure says: Place the number of sheng in 2 hu of salt, and multiply it by 100 li to obtain the divisor.
Multiply 40 qian by the number of sheng in the current load of salt, and also multiply it by 80 li to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of qian.

The answer says: *a* qian.
"""

# 置鹽二斛升數
# 1 hu = 10 dou, 1 dou = 10 sheng
二斛升數 = 2 * 10 * 10  # 2 hu in sheng

# 以一百里乘之為法
法 = 二斛升數 * 100

# 負鹽一斛七斗三升、少半升
# Convert 1 hu, 7 dou, 3 sheng, and 0.5 sheng into total sheng
今負鹽升數 = (1 * 10 * 10) + (7 * 10) + 3 + Fraction(1, 2)

# 以四十錢乘今負鹽升數
實1 = 40 * 今負鹽升數

# 又以八十里乘之
實 = 實1 * 80

# 實如法得一錢
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
