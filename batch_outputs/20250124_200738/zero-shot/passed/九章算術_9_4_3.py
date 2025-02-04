"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a tree with a height of 2丈 (20尺, since 1丈 = 10尺) and a circumference of 3尺. A vine wraps around the tree 7 times and reaches the top of the tree. We are tasked to find the length of the vine (葛).

The solution involves using the Pythagorean theorem, where:
- The height of the tree (木長) is the "句" (one leg of the right triangle).
- The total horizontal distance covered by the vine (7周 × 3尺) is the "股" (the other leg of the right triangle).
- The hypotenuse (弦) is the length of the vine (葛).

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
tree_height = Fraction(20)  # 木長, 2丈 = 20尺
circumference = Fraction(3)  # 圍之, 3尺
wraps = Fraction(7)  # 葛纏木七周

# Calculate the horizontal distance (股)
horizontal_distance = wraps * circumference

# Use the Pythagorean theorem to calculate the vine length (弦)
a = (tree_height**2 + horizontal_distance**2)**0.5  # 葛長

# Convert the result to 丈 (1丈 = 10尺)
a = Fraction(a) / 10

# The length of the vine in 丈
a
#----- content ends here -----


"""


The variable `a` will contain the length of the vine in 丈.
"""


"""
"""
