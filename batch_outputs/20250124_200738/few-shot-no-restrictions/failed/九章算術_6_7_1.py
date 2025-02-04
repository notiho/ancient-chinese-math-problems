"""
今有負籠重一石一十七斤，行七十六步，五十返。今負籠重一石，行百步，問︰返幾何？
術曰：以今所行步數乘今籠重斤數為法，故籠重斤數乘故步，又以返數乘之，為實。實如法得一返。
荅曰： a返 。
"""

#----- content starts here -----
"""
Suppose there is a load weighing 1 shi and 17 jin, carried for 76 steps, with 50 returns.
Now, with a load weighing 1 shi, carried for 100 steps, how many returns are there?

The procedure says: Multiply the current number of steps by the current load weight in jin to obtain the divisor.
Then, multiply the previous load weight in jin by the previous number of steps, and also multiply by the number of returns to obtain the dividend.
Divide the dividend by the divisor to obtain the number of returns.

Answer: *a* returns.
"""

from fractions import Fraction

# Conversion constants
石_to_斤 = 120  # 1 石 = 120 斤

# Previous load weight: 1 石 17 斤
previous_load_weight = 1 * 石_to_斤 + 17  # Convert to 斤

# Previous steps and returns
previous_steps = 76
previous_returns = 50

# Current load weight: 1 石
current_load_weight = 1 * 石_to_斤  # Convert to 斤

# Current steps
current_steps = 100

# Calculate the divisor (法): current steps × current load weight
divisor = current_steps * current_load_weight

# Calculate the dividend (實): previous load weight × previous steps × previous returns
dividend = previous_load_weight * previous_steps * previous_returns

# Calculate the number of returns (a)
a = Fraction(dividend, divisor)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 150000/2603, Actual: 2603/60"""
