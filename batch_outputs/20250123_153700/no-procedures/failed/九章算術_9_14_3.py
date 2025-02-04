"""
今有句五步，股十二步。問︰句中容方幾何？
荅曰：方 a步 。
"""

"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: how large is the square contained within the hypotenuse?

Answer: the square is *a* bu².
"""

# 句 (base) = 5步
句 = 5

# 股 (height) = 12步
股 = 12

# Hypotenuse squared (using the Pythagorean theorem)
a = 句**2 + 股**2  # Hypotenuse squared is the sum of the squares of the two legs

# a is the area of the square contained within the hypotenuse
a
"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 169"""
