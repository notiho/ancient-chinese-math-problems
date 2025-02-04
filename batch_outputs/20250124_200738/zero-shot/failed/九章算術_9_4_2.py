"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the length of a vine (葛) that wraps around a tree seven times and reaches the top of the tree. The tree's height is given as 2丈 (20尺), and its circumference is 3尺. The vine's length can be calculated using the Pythagorean theorem, where the height of the tree is one leg of a right triangle, and the total horizontal distance (7 wraps × 3尺) is the other leg. The hypotenuse of the triangle will be the length of the vine.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
tree_height = Fraction(20)  # 木長 (height of the tree) in 尺
circumference = Fraction(3)  # 圍之 (circumference of the tree) in 尺
wraps = 7  # 葛纏木七周 (number of wraps)

# Calculate the total horizontal distance (股)
horizontal_distance = wraps * circumference

# Use the Pythagorean theorem to calculate the length of the vine (弦)
vine_length = (tree_height**2 + horizontal_distance**2)**0.5

# Convert the result to 丈 (1丈 = 10尺)
a = vine_length / 10

# The solution
a
#----- content ends here -----


"""


This code calculates the length of the vine in 丈 and stores the result in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 29/10, Actual: 2.9"""
