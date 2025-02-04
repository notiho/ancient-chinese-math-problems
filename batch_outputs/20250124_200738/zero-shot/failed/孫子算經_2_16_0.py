"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the number of square units ("方") that can be formed using a given volume of soil from a trapezoidal prism-shaped embankment.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the embankment
lower_width = Fraction(5)  # in 丈
upper_width = Fraction(3)  # in 丈
height = Fraction(2)       # in 丈
length = Fraction(60, 10)  # converting 尺 to 丈 (1 丈 = 10 尺)
volume_per_square_unit = Fraction(1000, 10)  # converting 尺 to 丈³ (1 丈³ = 1000 尺³)

# Calculate the average width of the trapezoid
average_width = (lower_width + upper_width) / 2  # in 丈

# Calculate the volume of the embankment
embankment_volume = average_width * height * length  # in 丈³

# Calculate the number of square units
a = embankment_volume / volume_per_square_unit  # in 方

# The result is stored in variable 'a'
#----- content ends here -----


"""


Now, the variable `a` contains the number of square units ("方") that can be formed.
"""


"""
Variable 'a' has wrong value. Expected: 48, Actual: 12/25"""
