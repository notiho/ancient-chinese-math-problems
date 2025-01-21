"""
今有圭田廣十二步，正從二十一步。問：為田幾何？
術曰：半廣以乘正從。
荅曰： a步 。
"""

"""
To solve this problem, we need to calculate the area of the field (田). The formula provided in the problem is:

**Area = (1/2 × 廣) × 正從**

Here:
- 廣 (width) = 12 steps
- 正從 (length) = 21 steps

The solution will be written into the variable `a`.


"""


from fractions import Fraction

# Given values
廣 = 12  # width in steps
正從 = 21  # length in steps

# Calculate the area
a = Fraction(1, 2) * 廣 * 正從

# a is the area in steps²
a


"""

"""


"""
"""
