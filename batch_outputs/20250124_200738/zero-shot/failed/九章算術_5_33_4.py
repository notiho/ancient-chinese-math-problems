"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

"""
To solve this problem, we need to calculate the height (`a`) of a rectangular storage space given its width (`廣`) of 3丈, length (`袤`) of 4丈5尺, and its volume (`容粟`) of 1萬斛. 

The formula for the height is derived as follows:
1. The volume is given as `實 = 廣 × 袤 × 高`.
2. Rearranging for height: `高 = 實 / (廣 × 袤)`.

In this problem:
- 1丈 = 10尺.
- The width (`廣`) is 3丈 = 30尺.
- The length (`袤`) is 4丈5尺 = 45尺.
- The volume (`實`) is 1萬斛 = 10000斛.

Let's compute the height in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
volume = 10000  # in 斛
width = 30  # in 尺 (3丈 = 30尺)
length = 45  # in 尺 (4丈5尺 = 45尺)

# Calculate height
a = Fraction(volume, width * length)  # height in 尺

# Convert height to 丈 (1丈 = 10尺)
a = a / 10  # height in 丈

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the height in 丈 as a `Fraction`.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 20/27"""
