"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
術曰：以七周乘三尺為股，木長為句，為之求弦。弦者，葛之長。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a tree and a vine, where the vine wraps around the tree seven times and reaches the top of the tree. The length of the vine is the hypotenuse of a right triangle formed by the height of the tree and the total horizontal distance covered by the vine's wrapping.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given data
tree_height = Fraction(2)  # 木長二丈 (tree height is 2丈)
circumference = Fraction(3, 10)  # 圍之三尺 (circumference is 3尺, which is 3/10丈)
wraps = 7  # 葛纏木七周 (the vine wraps around the tree 7 times)

# Compute the total horizontal distance (股)
horizontal_distance = wraps * circumference

# Compute the hypotenuse (弦), which is the length of the vine
a = math.sqrt(float(tree_height**2 + horizontal_distance**2))

# Convert the result back to a Fraction for exact representation
a = Fraction(a).limit_denominator()

# The length of the vine in 丈
print(f"The length of the vine is {a}丈.")
#----- content ends here -----


"""


The solution is stored in the variable `a`, which represents the length of the vine in 丈.
"""


"""
"""
