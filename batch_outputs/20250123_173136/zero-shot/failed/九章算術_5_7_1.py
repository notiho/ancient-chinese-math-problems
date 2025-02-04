"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism (塹). The formula provided in the problem is as follows:

1. Add the top width (上廣) and bottom width (下廣), then divide by 2 to get the average width.
2. Multiply the average width by the depth (深) to get the cross-sectional area.
3. Multiply the cross-sectional area by the length (袤) to get the total volume.

The given dimensions are:
- 上廣 = 1丈6尺3寸 = 16尺3寸 = \(16 + \frac{3}{10}\) 尺
- 下廣 = 1丈 = 10尺
- 深 = 6尺3寸 = \(6 + \frac{3}{10}\) 尺
- 袤 = 13丈2尺1寸 = 132尺1寸 = \(132 + \frac{1}{10}\) 尺

We will compute the volume step by step using Python code.


"""


from fractions import Fraction

# Given dimensions
上廣 = Fraction(16) + Fraction(3, 10)  # 16尺3寸
下廣 = Fraction(10)  # 10尺
深 = Fraction(6) + Fraction(3, 10)  # 6尺3寸
袤 = Fraction(132) + Fraction(1, 10)  # 132尺1寸

# Step 1: Compute the average width
平均廣 = (上廣 + 下廣) / 2

# Step 2: Compute the cross-sectional area
橫截面積 = 平均廣 * 深

# Step 3: Compute the total volume
a = 橫截面積 * 袤

# The result is stored in variable 'a'
a


"""


The variable `a` will contain the total volume in cubic 尺 (cubic feet).
"""


"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
