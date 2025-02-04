"""
今有句五步，股十二步。問︰句中容方幾何？
荅曰：方 a步 。
"""

"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: how large is the square contained within the hypotenuse?

Answer: it is *a* square bu.
"""

# 句 (base) = 5 步
句 = 5

# 股 (height) = 12 步
股 = 12

# Hypotenuse square (方) = 句^2 + 股^2
a = 句**2 + 股**2  # This is the square of the hypotenuse in square bu.
"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 169"""
