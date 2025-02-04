"""
今有方堡壔方一丈六尺，高一丈五尺。問︰積幾何？
術曰：方自乘，以高乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (cuboid). The dimensions are given in Chinese units: length and width are 1丈6尺, and height is 1丈5尺. 

1丈 = 10尺, so we first convert the dimensions into 尺 (feet).  
Then, the volume is calculated as:  
Volume = length × width × height.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions in 尺 (feet)
length = Fraction(1 * 10 + 6)  # 1丈6尺 = 10尺 + 6尺
width = Fraction(1 * 10 + 6)   # Same as length since it's a square base
height = Fraction(1 * 10 + 5)  # 1丈5尺 = 10尺 + 5尺

# Volume calculation
a = length * width * height  # Volume in cubic 尺

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic 尺.
"""


"""
"""
