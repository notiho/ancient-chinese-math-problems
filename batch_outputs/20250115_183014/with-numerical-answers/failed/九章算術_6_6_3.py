"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
術曰：置鹽二斛升數，以一百里乘之為法。以四十錢乘今負鹽升數，又以八十里乘之，為實。實如法得一錢。
荅曰： a(=416/15)錢 。
"""

"""
Suppose a porter carries 2 hu of salt for 100 li and is paid 40 qian.
Now, the porter carries 1 hu, 7 dou, 3 sheng, and half a sheng of salt for 80 li.
Question: how much money should be paid?

The procedure says: Place the number of sheng in 2 hu of salt, and multiply it by 100 li to get the divisor.
Multiply 40 qian by the number of sheng in the current load of salt, and also multiply it by 80 li to get the dividend.
Divide the dividend by the divisor to get the amount of qian.

Answer: *a*(=416/15) qian.
"""

# 置鹽二斛升數
# Convert 2 hu to sheng (1 hu = 10 dou, 1 dou = 10 sheng)
鹽二斛升數 = 2 * 10 * 10

# 以一百里乘之為法
法 = 100 * 鹽二斛升數

# 今負鹽一斛七斗三升、少半升
# Convert 1 hu, 7 dou, 3 sheng, and 1/2 sheng to total sheng
今負鹽升數 = (1 * 10 * 10) + (7 * 10) + 3 + Fraction(1, 2)

# 以四十錢乘今負鹽升數
實1 = 40 * 今負鹽升數

# 又以八十里乘之
實 = 80 * 實1

# 實如法得一錢
a = Fraction(實, 法) # 416/15 qian
"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
