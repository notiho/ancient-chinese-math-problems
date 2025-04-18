"""
今有田一畝，收粟六升、太半升。今有田一頃二十六畝一百五十九步，問︰收粟幾何？
術曰：以畝二百四十步為法，以六升、太半升乘今有田積步為實，實如法得粟數。
荅曰： a斛 。
"""

"""

"""


from fractions import Fraction

# 田一畝，收粟六升、太半升
粟每畝 = 6 + Fraction(1, 2)  # 六升、太半升

# 畝二百四十步為法
畝步數 = 240

# 今有田一頃二十六畝一百五十九步
田積步 = 100 * 畝步數 + 26 * 畝步數 + 159  # 一頃 = 100畝

# 以六升、太半升乘今有田積步為實
實 = 粟每畝 * 田積步

# 實如法得粟數
粟數 = Fraction(實, 畝步數)

# 轉換為斛（10升 = 1斛）
a = Fraction(粟數, 10)


"""

"""


"""
Variable 'a' has wrong value. Expected: 10133/1200, Actual: 131729/1600"""
