"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
術曰：方自乘，以高乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (方堡壔). The dimensions are given in terms of "丈" (zhang) and "尺" (chi), where 1 丈 = 10 尺. The formula for the volume is:

\[
\text{Volume} = \text{length} \times \text{width} \times \text{height}
\]

Here, the length and width are both 1 丈 6 尺, and the height is 1 丈 5 尺. First, we convert these dimensions into 尺, then compute the volume.


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions in 尺
length = 1 * 10 + 6  # 1 丈 6 尺 = 16 尺
width = 1 * 10 + 6   # 1 丈 6 尺 = 16 尺
height = 1 * 10 + 5  # 1 丈 5 尺 = 15 尺

# Volume calculation
a = Fraction(length) * Fraction(width) * Fraction(height)  # Volume in 尺³

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic 尺 (尺³).
"""


"""
"""
