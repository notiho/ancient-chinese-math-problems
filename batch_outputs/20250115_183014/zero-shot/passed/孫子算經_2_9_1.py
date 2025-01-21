"""
今有圓窖，下周二百八十六尺，深三丈六尺。問：受粟幾何？
術曰：置周二百八十六尺，自相乘得八萬一千七百九十六尺，以深三丈六尺乘之，得二百九十四萬四千六百五十六；以一十二除之，得二十四萬五千三百八十八尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the volume of a cylindrical granary (圓窖) and determine how many "斛" it can hold. The formula for the volume of a cylinder is:

\[
V = \pi r^2 h
\]

However, in ancient Chinese mathematics, the formula for the volume of a cylinder was simplified as:

\[
V = \frac{周^2 \times 深}{12}
\]

where:
- \( 周 \) is the circumference of the base of the cylinder,
- \( 深 \) is the depth (height) of the cylinder,
- The division by 12 accounts for the approximation of \(\pi\).

Finally, the result is divided by the volume of one "斛" (1斛 = 1尺6寸2分 = 1.62尺³) to find the number of "斛" the granary can hold.

Here is the Python code to compute the answer:


"""


from fractions import Fraction

# Given values
周 = 286  # circumference in 尺
深 = 3 * 10 + 6  # depth in 尺 (3丈6尺 = 36尺)
一斛 = Fraction(162, 100)  # 1斛 = 1.62尺³

# Step 1: Compute 周^2
周_squared = 周 * 周

# Step 2: Compute 周^2 * 深
volume_raw = 周_squared * 深

# Step 3: Divide by 12 to get the volume in 尺³
volume_in_cubic_chi = Fraction(volume_raw, 12)

# Step 4: Divide by the volume of one 斛 to get the number of 斛
a = volume_in_cubic_chi / 一斛

# Result
a


"""


The variable `a` will contain the number of "斛" the granary can hold, represented as a fraction.
"""


"""
"""
