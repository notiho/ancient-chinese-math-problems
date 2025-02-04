"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
荅曰：出漆 a斗 ，得油 b斗 ，和漆 c斗 ， d升 。
"""

"""
Suppose 3 dou of lacquer can be exchanged for 4 dou of oil, and 4 dou of oil can be mixed with 5 dou of lacquer.
Now, there are 3 dou of lacquer, and it is desired to exchange it for oil and then mix the oil back with the remaining lacquer.
Question: how much lacquer is used for exchange (*a* dou), how much oil is obtained (*b* dou), and how much lacquer is left for mixing (*c* dou and *d* sheng)?
"""

from fractions import Fraction

# 漆三得油四 (3 dou of lacquer can be exchanged for 4 dou of oil)
漆_to_油_ratio = Fraction(4, 3)

# 油四和漆五 (4 dou of oil can be mixed with 5 dou of lacquer)
油_to_漆_ratio = Fraction(5, 4)

# 漆三斗 (3 dou of lacquer available)
total_漆 = 3

# Step 1: Exchange lacquer for oil
# Let "a" be the amount of lacquer used for exchange
a = total_漆  # Use all lacquer for exchange

# Calculate the amount of oil obtained
b = a * 漆_to_油_ratio

# Step 2: Mix oil with lacquer
# For every 4 dou of oil, 5 dou of lacquer is needed
# Calculate how much lacquer is needed to mix with the obtained oil
needed_漆_for_mixing = b * 油_to_漆_ratio

# Check if there is enough lacquer left for mixing
if needed_漆_for_mixing <= total_漆:
    c = needed_漆_for_mixing  # Lacquer used for mixing
    d = 0  # No leftover lacquer in sheng
else:
    c = total_漆  # Use all remaining lacquer for mixing
    d = (needed_漆_for_mixing - total_漆) * 10  # Convert leftover lacquer to sheng

# Output results
a斗 = a
b斗 = b
c斗 = c
d升 = d

# Results
a斗, b斗, c斗, d升
"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 3
Variable 'd' has wrong value. Expected: 3/4, Actual: 20"""
