"""
今有粟二斗一升，欲為粺米。問︰得幾何？
術曰：以粟求粺米，二十七之，五十而一。
荅曰：為粺米 a斗 。
"""

"""
To solve this problem, we need to calculate how much 粺米 (refined rice) can be obtained from 粟 (unrefined rice). The problem states that for every 27 units of 粟, we get 1 unit of 粺米. The given amount of 粟 is 2斗1升, and we need to convert this into 粺米.

1斗 = 10升, so 2斗1升 = 21升.

The calculation is as follows:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
粟 = 21  # in 升
conversion_ratio = Fraction(1, 27)  # 1 unit of 粺米 per 27 units of 粟

# Calculate 粺米
a = 粟 * conversion_ratio  # in 升

# Convert 粺米 from 升 to 斗 (1斗 = 10升)
a = a / 10  # in 斗

# Result
a
#----- content ends here -----


"""


The variable `a` will contain the amount of 粺米 in 斗.
"""


"""
Variable 'a' has wrong value. Expected: 567/500, Actual: 7/90"""
