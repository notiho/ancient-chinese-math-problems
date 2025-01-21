"""
今有圓窖，周五丈四尺，深一丈八尺。問：受粟幾何？
術曰：先置周五丈四尺相乘，得二千九百一十六尺，以深一丈八尺乘之，得五萬二千四百八十八尺；以一十二除之，得四千三百七十四尺，以斛法一尺六寸二分除之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will calculate the volume of a cylindrical granary (圓窖) and then convert it into the number of "斛" (a unit of volume). The formula for the volume of a cylinder is:

\[
V = \pi r^2 h
\]

However, in ancient Chinese mathematics, they approximate \(\pi\) as 3, and the formula becomes:

\[
V = \text{周} \times \text{周} \times \text{深} / 12
\]

Finally, the volume is divided by the volume of one "斛" to get the number of "斛."

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
周 = Fraction(5 * 10 + 4, 10)  # 周 (circumference) = 5丈4尺 = 54尺
深 = Fraction(1 * 10 + 8, 10)  # 深 (depth) = 1丈8尺 = 18尺

# Step 1: Compute 周 * 周
周平方 = 周 * 周  # 周 squared

# Step 2: Multiply by 深
體積尺 = 周平方 * 深  # Volume in cubic 尺

# Step 3: Divide by 12 (ancient formula for cylindrical volume)
體積 = 體積尺 / 12  # Volume in cubic 尺

# Step 4: Convert to 斛
斛法 = Fraction(1, 1) + Fraction(6, 10) + Fraction(2, 100)  # 1尺6寸2分 = 1.62尺
a = 體積 / 斛法  # Volume in 斛

# Result
a  # The number of 斛


"""


This code calculates the number of "斛" (a) based on the given dimensions of the granary.
"""


"""
Variable 'a' has wrong value. Expected: 2700, Actual: 27/10"""
