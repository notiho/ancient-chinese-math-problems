"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of the canal (渠). The formula provided in the problem is as follows:

1. Add the upper width (上廣) and lower width (下廣), then take half of the sum.
2. Multiply the result by the depth (深).
3. Multiply the result by the length (袤).
4. The result is the volume in cubic feet (積尺).

Now, let's translate this into Python code:


"""


from fractions import Fraction

# Given dimensions
upper_width = Fraction(1, 1) * 18  # 1丈8尺 = 18尺
lower_width = Fraction(3, 1) + Fraction(6, 10)  # 3尺6寸 = 3.6尺
depth = Fraction(1, 1) * 18  # 1丈8尺 = 18尺
length = Fraction(51824, 1)  # 51824尺

# Calculation
average_width = (upper_width + lower_width) / 2  # Average width
cross_section_area = average_width * depth  # Cross-sectional area
a = cross_section_area * length  # Volume in cubic feet

# Result
a  # Volume in cubic feet


"""


The variable `a` will contain the final result in cubic feet (積尺).
"""


"""
"""
