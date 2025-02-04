"""
今有圓材，埋在壁中，不知大小。以鐻鐻之，深一寸，鐻道長一尺。問︰徑幾何？
術曰：半鐻道自乘，如深寸而一，以深寸增之，即材徑。
荅曰：材徑 a尺 。
"""

"""
To solve this problem, we need to compute the diameter (材徑) of a circular object (圓材) based on the given measurements. Here's the Python code:


"""


from fractions import Fraction

# Given values
depth = Fraction(1, 10)  # 深一寸 = 1/10 尺
arc_length = Fraction(1)  # 鐻道長一尺 = 1 尺

# Calculation
half_arc_squared = (arc_length / 2) ** 2  # 半鐻道自乘
depth_squared = depth ** 2  # 深寸而一
diameter = half_arc_squared / depth + depth  # 以深寸增之，即材徑

# Result
a = diameter  # 材徑 a 尺


"""


The result is stored in the variable `a`, which represents the diameter of the circular object in 尺.
"""


"""
"""
