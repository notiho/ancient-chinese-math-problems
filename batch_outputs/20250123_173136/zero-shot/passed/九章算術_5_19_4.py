"""
今有陽馬，廣五尺，袤七尺，高八尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，三而一。
荅曰： a尺 。
"""

"""
This problem is asking for the volume of a rectangular prism (陽馬) with given dimensions: width (廣) = 5 尺, length (袤) = 7 尺, and height (高) = 8 尺. The formula provided suggests multiplying the width, length, and height, then dividing the result by 3.

Here is the Python code to compute the answer:


"""


from fractions import Fraction

# Dimensions of the rectangular prism
width = 5  # 尺
length = 7  # 尺
height = 8  # 尺

# Compute the volume
a = Fraction(width * length * height, 3)  # Volume in 尺

# The result is stored in variable 'a'


"""


The variable `a` will contain the volume of the rectangular prism in 尺.
"""


"""
"""
