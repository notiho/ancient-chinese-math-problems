"""
今有塹堵下廣二丈，袤一十八丈六尺，高二丈五尺。問︰積幾何？
術曰：廣袤相乘，以高乘之，二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a rectangular prism (塹堵). The formula for the volume is:

\[ \text{Volume} = \text{Length} \times \text{Width} \times \text{Height} \]

The dimensions are given as:
- Width (廣) = 2 丈
- Length (袤) = 18 丈 6 尺
- Height (高) = 2 丈 5 尺

We need to convert all measurements to 尺 (since the answer is in 尺). Recall the conversion:
1 丈 = 10 尺.

Thus:
- Width = \( 2 \times 10 = 20 \) 尺
- Length = \( 18 \times 10 + 6 = 186 \) 尺
- Height = \( 2 \times 10 + 5 = 25 \) 尺

Now, calculate the volume:
\[ \text{Volume} = \text{Width} \times \text{Length} \times \text{Height} \]

Finally, divide the result by 2 (as indicated by "二而一").

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Dimensions in 尺
width = 20  # 2 丈 = 20 尺
length = 186  # 18 丈 6 尺 = 186 尺
height = 25  # 2 丈 5 尺 = 25 尺

# Calculate the volume
a = Fraction(width * length * height, 2)  # Divide by 2 as per the problem

# The answer is stored in variable 'a'
a


"""


The variable `a` will contain the volume in 尺³ as a `Fraction`.
"""


"""
"""
