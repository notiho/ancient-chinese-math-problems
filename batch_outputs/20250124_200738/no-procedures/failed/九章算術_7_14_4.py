"""
今有漆三得油四，油四和漆五。今有漆三斗，欲令分以易油，還自和餘漆。問︰出漆、得油、和漆各幾何？
荅曰：出漆 a斗 ，得油 b斗 ，和漆 c斗 ， d升 。
"""

#----- content starts here -----
"""
Suppose 3 dou of lacquer can be exchanged for 4 dou of oil, and 4 dou of oil can be mixed with 5 dou of lacquer.
Now, there are 3 dou of lacquer, and it is desired to exchange it for oil and then mix the remaining lacquer with the oil.

Question: How much lacquer is used for exchange (*a* dou), how much oil is obtained (*b* dou), and how much lacquer is left for mixing (*c* dou and *d* sheng)?

Answer: *a* dou of lacquer is used, *b* dou of oil is obtained, and *c* dou and *d* sheng of lacquer are left for mixing.
"""

from fractions import Fraction

# Initial lacquer amount
漆 = Fraction(3)  # 3 dou

# Exchange rate: 3 dou of lacquer gets 4 dou of oil
漆_換油_比例 = Fraction(3, 4)  # 3 dou lacquer -> 4 dou oil

# Mixing ratio: 4 dou of oil mixes with 5 dou of lacquer
油_和漆_比例 = Fraction(4, 5)  # 4 dou oil -> 5 dou lacquer

# Step 1: Determine how much lacquer is used for exchange
a = 漆  # All lacquer is initially considered for exchange

# Step 2: Determine how much oil is obtained
b = a * Fraction(4, 3)  # Oil obtained from exchanging lacquer

# Step 3: Determine how much lacquer is left for mixing
# To mix with the obtained oil, we need lacquer in the ratio of 5 dou lacquer for 4 dou oil
漆_和油_所需 = b * Fraction(5, 4)  # Lacquer required for mixing with the obtained oil

# If the lacquer required for mixing is less than the total lacquer, we can mix
if 漆_和油_所需 <= 漆:
    c = 漆_和油_所需  # Lacquer used for mixing
    d = 0  # No leftover lacquer in sheng
else:
    c = 漆  # Use all lacquer for mixing
    d = 0  # No leftover lacquer in sheng

# Final results
a = 漆  # Lacquer used for exchange
b = 漆 * Fraction(4, 3)  # Oil obtained
c = 漆 -漆#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9/8, Actual: 3
Variable 'b' has wrong value. Expected: 3/2, Actual: 4
Variable 'c' has wrong value. Expected: 9/5, Actual: 0
Variable 'd' has wrong value. Expected: 3/4, Actual: 0"""
