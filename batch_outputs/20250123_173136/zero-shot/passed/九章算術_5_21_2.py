"""
今有羨除，下廣六尺，上廣一丈，深三尺，末廣八尺，無深，袤七尺。問︰積幾何？
術曰：并三廣，以深乘之，又以袤乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem describes a shape with varying widths and depths, and we are tasked with calculating its volume.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
lower_width = Fraction(6)  # 下廣 (lower width) in 尺
upper_width = Fraction(10)  # 上廣 (upper width) in 尺
depth = Fraction(3)  # 深 (depth) in 尺
end_width = Fraction(8)  # 末廣 (end width) in 尺
length = Fraction(7)  # 袤 (length) in 尺

# Calculation
# Combine the three widths: lower_width, upper_width, and end_width
combined_width = lower_width + upper_width + end_width

# Multiply by the depth
volume_with_depth = combined_width * depth

# Multiply by the length
total_volume = volume_with_depth * length

# Divide by 6 (六而一)
a = total_volume / Fraction(6)

# The result is stored in variable 'a'
a  # Volume in cubic 尺


"""


The variable `a` will contain the solution to the problem, which represents the volume in cubic 尺.
"""


"""
"""
