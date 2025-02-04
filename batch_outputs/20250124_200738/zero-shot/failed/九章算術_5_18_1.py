"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we calculate the volume of a rectangular prism. The given dimensions are:

- Width (廣): 2丈 = 20尺 (1丈 = 10尺)
- Length (袤): 18丈6尺 = 186尺
- Height (高): 2丈5尺 = 25尺

The formula for the volume is:

\[
\text{Volume} = \text{Width} \times \text{Length} \times \text{Height}
\]

Finally, since the result is given in 尺 (cubic feet), we compute directly in 尺.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions in 尺
width = 20  # 2丈 = 20尺
length = 186  # 18丈6尺 = 186尺
height = 25  # 2丈5尺 = 25尺

# Calculate the volume
a = width * length * height

# The answer is stored in variable 'a'
#----- content ends here -----


"""


The variable `a` will contain the volume in cubic 尺.
"""


"""
Variable 'a' has wrong value. Expected: 46500, Actual: 93000"""
