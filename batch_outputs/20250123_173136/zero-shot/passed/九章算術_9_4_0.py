"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the length of a vine (葛) that wraps around a cylindrical tree seven times. The tree's height is 2丈 (20尺), and its circumference is 3尺. The vine forms a helical path, and we need to calculate its total length using the Pythagorean theorem.

Here is the Python code:


"""


from fractions import Fraction
import math

# Given values
tree_height = Fraction(20)  # 木長 (2丈 = 20尺)
circumference = Fraction(3)  # 圍之 (3尺)
wraps = 7  # 葛纏木七周

# Calculate the total horizontal distance (股)
horizontal_distance = wraps * circumference

# Calculate the vine length (弦) using the Pythagorean theorem
vine_length = math.sqrt(float(tree_height**2 + horizontal_distance**2))

# Convert the result to 丈 (1丈 = 10尺)
a = Fraction(vine_length) / 10

# Output the result
a


"""


The variable `a` will contain the length of the vine in 丈.
"""


"""
"""
