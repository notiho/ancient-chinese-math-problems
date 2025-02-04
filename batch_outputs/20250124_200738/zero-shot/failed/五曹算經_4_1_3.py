"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain (in "斛") that can be harvested from 900 畝 of land, where each step (步) yields 3 升 and 2 合 of grain. Here's the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
田 = 900  # 畝
每畝步 = 240  # 每畝有240步
每步收粟升 = Fraction(3)  # 每步收3升
每步收粟合 = Fraction(2, 10)  # 每步收2合 (1升 = 10合)

# Total steps in 900 畝
總步 = 田 * 每畝步

# Total grain collected in 升
每步收粟 = 每步收粟升 + 每步收粟合
總粟升 = 總步 * 每步收粟

# Convert 升 to 斛 (1 斛 = 10 升)
a = 總粟升 / 10

# Result
a  # 斛
#----- content ends here -----


"""


The variable `a` will contain the total amount of grain in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
