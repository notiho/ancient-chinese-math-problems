"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
術曰：置堤，上廣三丈，下廣五丈。并之，得八丈；半之，得四丈。以二丈乘之，得八百尺；以長六十尺乘之，得四萬八千；以一千尺除之，即得。
答曰： a 方。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the number of cubic units ("方") that can be formed using a given volume of material. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
top_width = Fraction(3)  # 上廣 (in 丈)
bottom_width = Fraction(5)  # 下廣 (in 丈)
height = Fraction(2)  # 高 (in 丈)
length = Fraction(60, 10)  # 長 (in 丈, converted from 尺 to 丈)
material_volume = Fraction(1000, 10)  # 一千尺 (converted to 丈^3)

# Calculate the average width of the trapezoidal cross-section
average_width = (top_width + bottom_width) / 2  # 并之，半之

# Calculate the volume of the堤
堤_volume = average_width * height * length  # 以二丈乘之，以長六十尺乘之

# Calculate the number of cubic units ("方") that can be formed
a = 堤_volume / material_volume  # 以一千尺除之

# The result
a
#----- content ends here -----


"""


The variable `a` will contain the solution to the problem, expressed as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 48, Actual: 12/25"""
