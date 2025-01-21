"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (塹堵). The dimensions are given as follows:

- Width (廣): 2 丈
- Length (袤): 18 丈 6 尺
- Height (高): 2 丈 5 尺

The formula for the volume is:

\[
\text{Volume} = \text{Width} \times \text{Length} \times \text{Height}
\]

Since the answer is requested in 尺 (feet), we need to convert all dimensions to 尺 before performing the calculation. Note that 1 丈 = 10 尺.

### Conversion:
- Width: \( 2 \, 丈 = 20 \, 尺 \)
- Length: \( 18 \, 丈 \, 6 \, 尺 = 186 \, 尺 \)
- Height: \( 2 \, 丈 \, 5 \, 尺 = 25 \, 尺 \)

### Calculation:
\[
\text{Volume} = 20 \times 186 \times 25
\]

Now, let's write this in Python code:


"""


from fractions import Fraction

# Dimensions in 尺
width = 20  # 2 丈 = 20 尺
length = 186  # 18 丈 6 尺 = 186 尺
height = 25  # 2 丈 5 尺 = 25 尺

# Volume calculation
a = width * length * height  # Volume in 尺³

# Result
a


"""


The variable `a` will hold the volume in 尺³.
"""


"""
Variable 'a' has wrong value. Expected: 46500, Actual: 93000"""
