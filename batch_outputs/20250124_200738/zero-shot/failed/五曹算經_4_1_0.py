"""
今有官田九百畝凡一步收粟三升二合。問：計㡬何？
術曰：列田九百畝以二百四十步乘之得二十一萬六千步以三升二合乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of grain harvested from 900 畝 of land, where each step (步) yields 3 升 and 2 合. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
田 = 900  # 畝
每畝步 = 240  # 每畝有240步
每步收粟 = Fraction(3, 1) + Fraction(2, 10)  # 每步收3升2合 (2合 = 2/10升)

# Total steps
總步 = 田 * 每畝步

# Total grain harvested
總收粟 = 總步 * 每步收粟

# Convert to 斛 (1斛 = 10升)
a = 總收粟 / 10

# Result
a  # 斛
#----- content ends here -----


"""


This code calculates the total amount of grain harvested in 斛. The variable `a` contains the final answer.
"""


"""
Variable 'a' has wrong value. Expected: 6912, Actual: 69120"""
