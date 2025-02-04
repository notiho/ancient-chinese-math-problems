"""
今有圓亭，下周三丈，上周二丈，高一丈。問︰積幾何？
術曰：上、下周相乘，又各自乘，并之，以高乘之，三十六而一。
荅曰： a尺 。
"""

"""
To solve this problem, we will compute the volume of a frustum of a cone (a truncated cone). The problem provides the dimensions of the frustum: the lower circumference (下周) is 3丈, the upper circumference (上周) is 2丈, and the height (高) is 1丈. The formula for the volume of a frustum of a cone is given in the problem:

\[
V = \frac{h}{36} \times (C_1 \times C_2 + C_1^2 + C_2^2)
\]

Where:
- \(C_1\) is the lower circumference (下周),
- \(C_2\) is the upper circumference (上周),
- \(h\) is the height (高).

We will compute the volume step by step in Python, using the class `Fraction` to ensure precision.

### Python Code:

"""


from fractions import Fraction

# Given dimensions
C1 = Fraction(3)  # Lower circumference in 丈
C2 = Fraction(2)  # Upper circumference in 丈
h = Fraction(1)   # Height in 丈

# Formula for the volume of the frustum
a = (h / 36) * (C1 * C2 + C1**2 + C2**2)

# Convert the result to 尺 (1 丈 = 10 尺)
a *= 10

# The result is stored in variable 'a'
a


"""


### Explanation:
1. \(C_1 = 3\) 丈, \(C_2 = 2\) 丈, and \(h = 1\) 丈 are directly taken from the problem.
2. The formula for the volume is applied step by step:
   - Compute \(C_1 \times C_2\),
   - Compute \(C_1^2\) and \(C_2^2\),
   - Add these terms together,
   - Multiply by \(\frac{h}{36}\).
3. The result is converted from 丈 to 尺 by multiplying by 10 (since 1 丈 = 10 尺).
4. The final result is stored in the variable `a`.

### Output:
The variable `a` will contain the volume in 尺.
"""


"""
Variable 'a' has wrong value. Expected: 4750/9, Actual: 95/18"""
