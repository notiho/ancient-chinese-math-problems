"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the height ("高") of a storage space given its width ("廣"), length ("袤"), and volume ("容粟"). The formula provided in the problem is:

1. Multiply the width and length to get the base area.
2. Divide the volume by the base area to get the height.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
width = Fraction(3)  # 廣 = 3丈
length = Fraction(4) + Fraction(5, 10)  # 袤 = 4丈5尺 = 4.5丈
volume = Fraction(10000)  # 容粟 = 1萬斛

# Calculate the base area
base_area = width * length  # 廣袤相乘

# Calculate the height
a = volume / base_area  # 高 = 容粟 / 廣袤

# The answer is stored in variable 'a'
#----- content ends here -----


"""


Explanation:
- The width is 3丈.
- The length is 4丈5尺, which is converted to 4.5丈 (1丈 = 10尺).
- The volume is 1萬斛, which is 10000斛.
- The base area is calculated by multiplying the width and length.
- The height is calculated by dividing the volume by the base area.

The result is stored in the variable `a`.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 20000/27"""
