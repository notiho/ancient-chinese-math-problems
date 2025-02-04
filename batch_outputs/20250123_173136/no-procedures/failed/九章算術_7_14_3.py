"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
荅曰：出漆 a斗 ，得油 b斗 ，和漆 c斗 ， d升 。
"""

"""
Suppose 3 dou of lacquer can be exchanged for 4 dou of oil, and 4 dou of oil can be mixed with 5 dou of lacquer.
Now, there are 3 dou of lacquer, and it is desired to exchange it for oil, then mix the oil back with the remaining lacquer.
Question: how much lacquer is used for exchange, how much oil is obtained, and how much lacquer is left for mixing?

Answer: *a* dou of lacquer is used for exchange, *b* dou of oil is obtained, and *c* dou and *d* sheng of lacquer are left for mixing.
"""

from fractions import Fraction

# 漆三斗
漆 = 3

# 漆三得油四 (3 dou of lacquer can be exchanged for 4 dou of oil)
漆_to_油_ratio = Fraction(4, 3)

# 油四和漆五 (4 dou of oil can be mixed with 5 dou of lacquer)
油_to_漆_ratio = Fraction(5, 4)

# Step 1: Exchange all lacquer for oil
a = 漆  # All lacquer is used for exchange
b = 漆 * 漆_to_油_ratio  # Oil obtained from the exchange

# Step 2: Mix the obtained oil back with lacquer
# For every 4 dou of oil, 5 dou of lacquer is needed
# Calculate how much lacquer is needed to mix with the obtained oil
漆_needed_for_mixing = b * 油_to_漆_ratio

# Remaining lacquer after mixing
remaining_漆 = 漆 - 漆_needed_for_mixing

# Convert remaining lacquer into dou and sheng
c = int(remaining_漆)  # Whole dou
d = (remaining_漆 - c) * 10  # Convert fractional part to sheng (1 dou = 10 sheng)

# Final results
a = Fraction(a)  # Lacquer used for exchange
b = Fraction(b)  # Oil obtained
c = Fraction(c)  # Whole dou of lacquer left
d = Fraction(d)  # Sheng of lacquer left

a, b, c, d  # Output results
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: -2
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
