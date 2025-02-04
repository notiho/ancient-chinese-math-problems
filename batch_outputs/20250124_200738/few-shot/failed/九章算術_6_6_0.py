"""
今有取傭負鹽二斛，行一百里，與錢四十。今負鹽一斛七斗三升、少半升，行八十里。問︰與錢幾何？
術曰：置鹽二斛升數，以一百里乘之為法。以四十錢乘今負鹽升數，又以八十里乘之，為實。實如法得一錢。
荅曰： a錢 。
"""

#----- content starts here -----
"""
Suppose a laborer carries 2 hu of salt for 100 li and is paid 40 qian.
Now, the laborer carries 1 hu, 7 dou, 3 sheng, and half a sheng for 80 li.
Question: how much should the laborer be paid?

The procedure says: Place the number of sheng in 2 hu of salt, and multiply it by 100 li to obtain the divisor.
Multiply 40 qian by the number of sheng in the current load of salt, and also multiply it by 80 li to obtain the dividend.
Divide the dividend by the divisor to obtain the amount of qian.

Answer: *a* qian.
"""

# 置鹽二斛升數
# 1 hu = 10 dou, 1 dou = 10 sheng
二斛升數 = 2 * 10 * 10  # 2 hu in sheng

# 以一百里乘之為法
法 = 二斛升數 * 100  # divisor

# 今負鹽一斛七斗三升、少半升
# Convert 1 hu, 7 dou, 3 sheng, and 0.5 sheng to total sheng
今負鹽升數 = (1 * 10 * 10) + (7 * 10) + 3 + Fraction(1, 2)  # in sheng

# 以四十錢乘今負鹽升數
四十錢 = 40
實_1 = 四十錢 * 今負鹽升數

# 又以八十里乘之
八十里 = 80
實 = 實_1 * 八十里  # dividend

# 實如法得一錢
a = Fraction(實, 法)  # result in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
