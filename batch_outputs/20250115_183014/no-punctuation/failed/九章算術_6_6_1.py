"""
今有取傭負鹽二斛行一百里與錢四十今負鹽一斛七斗三升少半升行八十里問與錢幾何
術曰置鹽二斛升數以一百里乘之為法以四十錢乘今負鹽升數又以八十里乘之為實實如法得一錢
荅曰 a錢 
"""

"""
Suppose a laborer carries 2 hu of salt for 100 li and is paid 40 qian.
Now, the laborer carries 1 hu, 7 dou, 3 sheng, and half a sheng for 80 li.
Question: how much money is paid?

The procedure says: Place the number of sheng in 2 hu of salt and multiply it by 100 li, obtaining the divisor.
Multiply 40 qian by the current number of sheng of salt, and also multiply it by 80 li, obtaining the dividend.
Divide the dividend by the divisor, obtaining the amount of qian.

The answer says: *a* qian.
"""

# 置鹽二斛升數
# 1 hu = 10 dou, 1 dou = 10 sheng
鹽二斛升數 = 2 * 10 * 10  # 2 hu in sheng

# 以一百里乘之，為法
法 = 鹽二斛升數 * 100  # Divisor

# 以四十錢乘
錢 = 40

# 今負鹽升數
# 1 hu = 10 dou, 1 dou = 10 sheng
今負鹽升數 = 1 * 10 * 10 + 7 * 10 + 3 + Fraction(1, 2)  # Convert to sheng

# 又以八十里乘之，為實
實 = 錢 * 今負鹽升數 * 80  # Dividend

# 實如法得一錢
a = Fraction(實, 法)  # Result in qian
"""
Variable 'a' has wrong value. Expected: 416/15, Actual: 694/25"""
