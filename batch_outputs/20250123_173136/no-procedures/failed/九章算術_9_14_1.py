"""
今有句五步，股十二步。問︰句中容方幾何？
荅曰：方 a步 。
"""

"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: how many square bu can fit inside the square on the hypotenuse?

Answer: *a* square bu.
"""

# 句 (base) = 5 bu
句 = 5

# 股 (height) = 12 bu
股 = 12

# Hypotenuse (弦) is calculated using the Pythagorean theorem: 弦^2 = 句^2 + 股^2
弦平方 = 句**2 + 股**2

# The area of the square on the hypotenuse is equal to 弦平方
a = 弦平方  # This is the area in square bu

# Final result
a
"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 169"""
