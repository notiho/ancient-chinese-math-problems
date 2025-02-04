"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

"""
To solve this problem, we will calculate the volume of a trapezoidal prism (representing the ditch or trench). The formula provided in the problem can be translated into Python code as follows:

1. Add the top width (`上廣`) and bottom width (`下廣`) and divide by 2 to get the average width.
2. Multiply the average width by the depth (`深`).
3. Multiply the result by the length (`袤`).
4. The result will be the volume in cubic feet (尺³).

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
上廣 = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1 + 5/10 丈
下廣 = Fraction(1, 1)  # 1丈
深 = Fraction(5, 10)  # 5尺 = 5/10 丈
袤 = Fraction(7, 1)  # 7丈

# Calculate the volume
平均廣 = (上廣 + 下廣) / 2  # Average width
橫截面積 = 平均廣 * 深  # Cross-sectional area
a = 橫截面積 * 袤  # Volume in cubic feet

# The result is stored in variable 'a'


"""


The variable `a` will contain the volume in cubic feet (尺³).
"""


"""
Variable 'a' has wrong value. Expected: 4375, Actual: 35/8"""
