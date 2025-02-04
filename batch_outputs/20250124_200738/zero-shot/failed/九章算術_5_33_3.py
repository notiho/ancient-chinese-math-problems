"""
今有倉廣三丈，袤四丈五尺，容粟一萬斛。問︰高幾何？
術曰：置粟一萬斛積尺為實。廣袤相乘為法。實如法而一，得高尺。
荅曰： a丈 。
"""

"""
To solve this problem, we need to calculate the height ("高") of a storage space given its dimensions and volume. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
volume = 10000  # in 斛
width = Fraction(3)  # in 丈
length = Fraction(4) + Fraction(5, 10)  # 4丈5尺 = 4 + 5/10 丈

# Formula: height = volume / (width * length)
height = Fraction(volume) / (width * length)

# Convert height to 丈 (1丈 = 10尺)
a = height / 10  # height in 丈

# The answer is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the height in 丈.
"""


"""
Variable 'a' has wrong value. Expected: 2, Actual: 2000/27"""
