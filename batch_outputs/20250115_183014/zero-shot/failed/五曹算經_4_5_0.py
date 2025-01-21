"""
今有方窖從一丈三尺廣六尺深一丈。問：受粟㡬何？
術曰：列從一丈三尺以廣六尺乘之得七十八尺以深一丈乘之得七百八十尺以斛法除之即得。
答曰： a斛 奇 b寸 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular pit and convert it into a unit of measurement called "斛" (hú). The dimensions of the pit are given in traditional Chinese units: 長 (length) = 1丈3尺, 廣 (width) = 6尺, and 深 (depth) = 1丈. 

1丈 = 10尺, so we first convert all dimensions into 尺 (feet). Then, we calculate the volume in cubic 尺 and convert it into 斛 using the conversion factor (1斛 = 100 cubic 尺).

Here is the Python code:


"""


from fractions import Fraction

# Dimensions of the pit
length = Fraction(1, 1) * 10 + 3  # 1丈3尺 = 10尺 + 3尺 = 13尺
width = Fraction(6, 1)  # 6尺
depth = Fraction(1, 1) * 10  # 1丈 = 10尺

# Calculate the volume in cubic 尺
volume = length * width * depth  # in cubic 尺

# Convert the volume into 斛 and 尺
a = volume // 100  # Number of 斛
b = volume % 100  # Remaining cubic 尺

# Results
a, b  # a斛 b尺


"""


### Explanation:
1. Convert all dimensions into 尺.
2. Compute the volume in cubic 尺 by multiplying length, width, and depth.
3. Divide the volume by 100 to find the number of 斛 (a) and the remainder in cubic 尺 (b).

### Solution:
The variables `a` and `b` will hold the number of 斛 and remaining cubic 尺, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 2407/5, Actual: 7
Variable 'b' has wrong value. Expected: 39/5, Actual: 80"""
