"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
lower_width = 5  # in 丈
upper_width = 3  # in 丈
height = 2       # in 丈
length = 60      # in 尺
unit_conversion = 1000  # 尺 per 方

# Calculations
combined_width = lower_width + upper_width  # 丈
average_width = Fraction(combined_width, 2)  # 丈
cross_section_area = average_width * height  # 丈^2
cross_section_area_in_chi = cross_section_area * 100  # convert 丈^2 to 尺^2
volume_in_chi = cross_section_area_in_chi * length  # 尺^3
a = Fraction(volume_in_chi, unit_conversion)  # 方

# Result
a  # in 方


"""


The variable `a` will contain the solution in terms of 方.
"""


"""
"""
