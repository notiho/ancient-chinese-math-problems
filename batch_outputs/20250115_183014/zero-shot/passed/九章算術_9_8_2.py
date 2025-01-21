"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the diameter of a circular object embedded in a wall, given the depth of the cut and the length of the chord (鐻道). Here's the Python code:


"""


from fractions import Fraction

# Given values
depth = Fraction(1, 10)  # 1寸 = 1/10尺
chord_length = Fraction(1)  # 1尺

# Calculation
half_chord = chord_length / 2  # 半鐻道
half_chord_squared = half_chord ** 2  # 半鐻道自乘
depth_squared = depth ** 2  # 深寸自乘
radius = (half_chord_squared + depth_squared) / (2 * depth)  # 半徑公式
a = radius * 2  # 材徑 = 2 * 半徑

# Output the result
a  # 材徑 in 尺


"""


The variable `a` will store the diameter of the circular object in 尺.
"""


"""
"""
