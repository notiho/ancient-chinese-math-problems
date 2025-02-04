"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
術曰：以今所行步數乘今籠重斤數為法，故籠重斤數乘故步，又以返數乘之，為實。實如法得一返。
荅曰： a返 。
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin, carried for 76 steps, with 50 returns.
Now, with a load weighing 1 shi, carried for 100 steps, how many returns can be made?

The procedure says: Multiply the current number of steps by the current load weight in jin to obtain the divisor.
Then, multiply the previous load weight in jin by the previous number of steps, and also multiply it by the number of returns to obtain the dividend.
Divide the dividend by the divisor to obtain the number of returns.

Answer: *a* returns.
"""

from fractions import Fraction

# Convert weights to jin (1 石 = 120 斤)
故籠重 = 1 * 120 + 17  # 1 石 17 斤
今籠重 = 1 * 120       # 1 石

# 步數 and returns
故步 = 76
故返 = 50
今步 = 100

# Calculate 法 (divisor)
法 = 今步 * 今籠重

# Calculate 實 (dividend)
實 = 故籠重 * 故步 * 故返

# Calculate the number of returns (a)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
