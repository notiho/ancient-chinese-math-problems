"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

"""
To solve this problem, we will calculate the number of square units ("方") that can be made using the given dimensions of the embankment. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
lower_width = Fraction(5)  # 下廣 (5丈)
upper_width = Fraction(3)  # 上廣 (3丈)
height = Fraction(2)       # 高 (2丈)
length = Fraction(60)      # 長 (60尺)
unit_area = Fraction(1000) # 一千尺作一方

# Calculation
combined_width = lower_width + upper_width  # 并之
average_width = combined_width / 2          # 半之
cross_section_area = average_width * height # 以二丈乘之
volume = cross_section_area * length        # 以長六十尺乘之
a = volume / unit_area                      # 以一千尺除之，即得

# Result
a  # This is the answer in 方
#----- content ends here -----


"""


The variable `a` will hold the solution in terms of "方".
"""


"""
Variable 'a' has wrong value. Expected: 48, Actual: 12/25"""
