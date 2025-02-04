"""
今有粟九百斛，斛别加二斗五升。問：加㡬何？
術曰：列九百斛以二斗五升乘之即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount added when each of the 900斛 is increased by 2斗5升. First, we need to convert 2斗5升 into a single unit (e.g., 升). Since 1斗 = 10升, 2斗5升 = 20升 + 5升 = 25升. Then, we multiply 900斛 by 25升 to find the total amount added.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Conversion factors
斗_to_升 = 10  # 1斗 = 10升

# Given values
粟 = 900  # 900斛
每斛增加 = 2 * 斗_to_升 + 5  # 2斗5升 converted to 升

# Total addition calculation
a = 粟 * 每斛增加  # Total addition in 升

# Result
a  # This is the total addition in 升
#----- content ends here -----


"""


The variable `a` will contain the total amount added in 升.
"""


"""
Variable 'a' has wrong value. Expected: 225, Actual: 22500"""
