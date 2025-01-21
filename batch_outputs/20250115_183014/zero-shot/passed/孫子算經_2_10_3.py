"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
術曰：置廣四丈六尺，長五丈四尺，相乘得二千四百八十四尺；以深三丈五尺乘之，得八萬六千九百四十尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will calculate the volume of the rectangular pit (方窖) and then convert it into a unit of "斛" using the given conversion factor. Here's the Python code:


"""


from fractions import Fraction

# Dimensions of the pit in 尺 (1 丈 = 10 尺)
width = 4 * 10 + 6  # 4 丈 6 尺
length = 5 * 10 + 4  # 5 丈 4 尺
depth = 3 * 10 + 5  # 3 丈 5 尺

# Volume in cubic 尺
volume = width * length * depth

# Conversion factor: 1 斛 = 1 尺 6 寸 2 分 = 1 + 6/10 + 2/100 = 1.62 尺
conversion_factor = Fraction(162, 100)

# Calculate the amount in 斛
a = volume / conversion_factor

# Result
a


"""


This code calculates the value of `a` in 斛.
"""


"""
"""
