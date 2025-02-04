"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (塹堵). The formula for the volume is:

\[
\text{Volume} = \text{length} \times \text{width} \times \text{height}
\]

The given dimensions are:
- Width (廣) = 2 丈
- Length (袤) = 18 丈 6 尺
- Height (高) = 2 丈 5 尺

We need to convert all dimensions to 尺 (since 1 丈 = 10 尺) and then compute the volume.

### Conversion:
- Width = \( 2 \times 10 = 20 \) 尺
- Length = \( 18 \times 10 + 6 = 186 \) 尺
- Height = \( 2 \times 10 + 5 = 25 \) 尺

### Calculation:
\[
\text{Volume} = \text{Width} \times \text{Length} \times \text{Height} = 20 \times 186 \times 25
\]

Finally, divide the result by 2 (as per the instruction "二而一").

Here is the Python code:


"""


from fractions import Fraction

# Dimensions in 尺
width = 20  # 2 丈 = 20 尺
length = 186  # 18 丈 6 尺 = 186 尺
height = 25  # 2 丈 5 尺 = 25 尺

# Volume calculation
a = Fraction(width * length * height, 2)  # Divide by 2 as per the rule

# Result
a  # Volume in 尺³


"""


The variable `a` will contain the volume in cubic 尺.
"""


"""
"""
