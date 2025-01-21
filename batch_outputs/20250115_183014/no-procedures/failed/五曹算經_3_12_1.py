"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
答曰： a人 。
"""

"""
Suppose there are 2 sheng of sauce to feed 5 people. Now there are 320 hu of sauce.
Question: how many people can be fed?

Answer: *a* people.
"""

# 醬二升飼五人
醬_per_人 = Fraction(2, 5)  # Each person consumes 2/5 sheng of sauce.

# 醬三百二十斛
醬_total = 320 * 10  # Convert hu to sheng (1 hu = 10 dou, 1 dou = 10 sheng, so 1 hu = 100 sheng).

# Calculate the number of people
a = Fraction(醬_total, 醬_per_人)  # Total sauce divided by sauce per person.
"""
Variable 'a' has wrong value. Expected: 80000, Actual: 8000"""
