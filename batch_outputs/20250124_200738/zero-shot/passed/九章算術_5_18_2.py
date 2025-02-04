"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (塹堵). The dimensions provided are:

- Width (廣): 2 丈
- Length (袤): 18 丈 6 尺
- Height (高): 2 丈 5 尺

1 丈 = 10 尺, so we need to convert all dimensions to 尺 before calculating the volume.

The formula for the volume is:
\[ \text{Volume} = \text{Width} \times \text{Length} \times \text{Height} \]

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Convert dimensions to 尺
width = 2 * 10  # 2 丈 = 20 尺
length = 18 * 10 + 6  # 18 丈 6 尺 = 186 尺
height = 2 * 10 + 5  # 2 丈 5 尺 = 25 尺

# Calculate the volume
a = Fraction(width * length * height, 2)  # Divide by 2 as per the problem statement

# The answer is stored in variable 'a' in 尺³
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic 尺 (尺³).
"""


"""
"""
