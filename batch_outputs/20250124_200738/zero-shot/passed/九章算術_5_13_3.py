"""
今有圓堡壔，周四丈八尺，高一丈一尺。問︰積幾何？
術曰：周自相乘，以高乘之，十二而一。
荅曰： a尺 。
"""

"""
To solve this problem, we need to calculate the volume of a cylindrical object (圓堡壔). The formula for the volume of a cylinder is:

\[
V = \frac{\pi \cdot d^2 \cdot h}{4}
\]

However, the problem uses an ancient Chinese approximation for the volume of a cylinder:

\[
V = \frac{C^2 \cdot h}{12}
\]

Where:
- \( C \) is the circumference of the base (周),
- \( h \) is the height (高).

### Given:
- \( C = 4 \) 丈 \( 8 \) 尺 = \( 48 \) 尺 (since 1 丈 = 10 尺),
- \( h = 1 \) 丈 \( 1 \) 尺 = \( 11 \) 尺.

### Step-by-step solution:
1. Square the circumference \( C \),
2. Multiply by the height \( h \),
3. Divide the result by \( 12 \).

Here is the Python code to compute the answer:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
C = 48  # circumference in 尺
h = 11  # height in 尺

# Calculation
a = Fraction(C**2 * h, 12)

# The result is stored in variable 'a'
#----- content ends here -----


"""


The value of \( a \) will be the volume in cubic 尺.
"""


"""
"""
