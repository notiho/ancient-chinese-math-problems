"""
今有句五步，股十二步。問︰句中容方幾何？
荅曰：方 a步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: how large is the square contained in the hypotenuse?

Answer: the square is *a* bu².
"""

# 句 (base) = 5 步
句 = 5

# 股 (height) = 12 步
股 = 12

# Calculate the square of the hypotenuse using the Pythagorean theorem
# Hypotenuse² = Base² + Height²
a = 句**2 + 股**2  # This gives the area of the square on the hypotenuse in bu²

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 60/17, Actual: 169"""
