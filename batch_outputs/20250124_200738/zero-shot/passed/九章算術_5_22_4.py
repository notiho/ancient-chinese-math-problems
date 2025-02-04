"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
術曰：倍下袤，上袤從之，以廣乘之，又以高乘之，六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to compute the volume of a frustum-like structure (trapezoidal prism) based on the given dimensions. The formula provided in the problem states that we should:

1. Double the bottom length (下袤).
2. Add the top length (上袤) to it.
3. Multiply the result by the width (廣).
4. Multiply the result by the height (高).
5. Divide the entire product by 6.

The dimensions provided are:
- Bottom length (下袤) = 4 丈
- Top length (上袤) = 2 丈
- Width (廣) = 3 丈
- Height (高) = 1 丈

We will compute the volume in terms of 尺 (1 丈 = 10 尺). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions in 丈
bottom_length = 4  # 下袤
top_length = 2     # 上袤
width = 3          # 廣
height = 1         # 高

# Convert dimensions to 尺 (1 丈 = 10 尺)
bottom_length = bottom_length * 10
top_length = top_length * 10
width = width * 10
height = height * 10

# Compute the volume
a = Fraction((2 * bottom_length + top_length) * width * height, 6)

# The result is stored in variable 'a' in 尺
a
#----- content ends here -----


"""


The variable `a` will contain the volume in 尺.
"""


"""
"""
