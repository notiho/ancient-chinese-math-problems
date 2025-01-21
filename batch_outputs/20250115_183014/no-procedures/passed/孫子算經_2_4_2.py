"""
今有粟一斗。問：為糲米幾何？
答曰： a升 。
"""

"""
Suppose there is 1 dou of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much does one obtain?

Answer: it makes *a* sheng of roughly husked millet.
"""

from fractions import Fraction

# 粟一斗 (1 dou = 10 sheng)
粟 = 10  # in sheng

# The conversion rate from unhusked millet to husked millet is 3/5
conversion_rate = Fraction(3, 5)

# Calculate the amount of husked millet
a = 粟 * conversion_rate

# Output the result
a  # a is the amount of husked millet in sheng
"""
"""
