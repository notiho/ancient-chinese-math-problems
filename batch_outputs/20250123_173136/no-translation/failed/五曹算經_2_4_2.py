"""
今有兵三千一百四十八人，人給布一丈二尺三寸。問：計㡬何？
術曰：列兵三千一百四十八人，以布一十二尺三寸乘之，得三萬八千七百二十尺四寸，以五十尺除之即得。
答曰： a端 。
"""

"""

"""


from fractions import Fraction

# 兵三千一百四十八人
兵 = 3148

# 布一丈二尺三寸 (1丈 = 10尺, 1尺 = 10寸)
布 = 10 + 2 + Fraction(3, 10)  # Convert to 尺

# 以布一十二尺三寸乘之
總布 = 兵 * 布

# 得三萬八千七百二十尺四寸
# 總布 = 38720 + Fraction(4, 10)  # Confirmed from the problem statement

# 以五十尺除之即得 (1端 = 50尺)
端法 = 50
a = Fraction(總布, 端法)  # Calculate the number of 端


"""

"""


"""
Variable 'a' has wrong value. Expected: 9675051/12500, Actual: 96801/125"""
