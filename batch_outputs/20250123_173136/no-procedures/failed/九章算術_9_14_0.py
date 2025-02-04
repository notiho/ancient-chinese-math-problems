"""
今有句五步，股十二步。問︰句中容方幾何？
荅曰：方 a步 。
"""

"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: how large is the square contained within the hypotenuse?

Answer: the square is *a* bu².
"""

# 句 (base) = 5 步
句 = 5

# 股 (height) = 12 步
股 = 12

# Calculate the hypotenuse (弦) squared using the Pythagorean theorem
弦平方 = 句**2 + 股**2

# The square contained within the hypotenuse is equal to the hypotenuse squared
a = 弦平方  # The square is a = 169 bu²
"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 169"""
