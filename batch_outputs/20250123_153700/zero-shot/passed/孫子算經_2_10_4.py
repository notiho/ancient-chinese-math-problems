"""
今有方窖，廣四丈六尺，長五丈四尺，深三丈五尺。問：受粟幾何？
術曰：置廣四丈六尺，長五丈四尺，相乘得二千四百八十四尺；以深三丈五尺乘之，得八萬六千九百四十尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular pit and then convert it into a unit called "斛" using the given conversion factor. Here's the Python code:


"""


from fractions import Fraction

# Dimensions of the pit
width = Fraction(4 * 10 + 6)  # 4丈6尺 converted to 尺
length = Fraction(5 * 10 + 4)  # 5丈4尺 converted to 尺
depth = Fraction(3 * 10 + 5)  # 3丈5尺 converted to 尺

# Volume in cubic 尺
volume_in_cubic_chi = width * length * depth

# Conversion factor: 1斛 = 1尺6寸2分 = 1 + 6/10 + 2/100 = 1.62尺
conversion_factor = Fraction(162, 100)

# Calculate the volume in 斛
a = volume_in_cubic_chi / conversion_factor

# The answer is stored in variable 'a'


"""


This code calculates the volume of the pit in cubic 尺 and then divides it by the conversion factor to get the volume in 斛. The result is stored in the variable `a`.
"""


"""
"""
