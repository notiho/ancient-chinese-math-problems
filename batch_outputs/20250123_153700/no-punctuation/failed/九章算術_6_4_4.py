"""
今有粟七斗三人分舂之一人為糲米一人為粺米一人為鑿米令米數等問取粟為米各幾何
術曰列置糲米三十粺米二十七鑿米二十四而反衰之副并為法以七斗乘未并者各自為取粟實實如法得一斗若求米等者以本率各乘定所取粟為實以粟率五十為法實如法得一斗
荅曰糲米取粟 a斗 粺米取粟 b斗 鑿米取粟 c斗 為米各 d斗 
"""

"""
Suppose there are 7 dou of millet, divided among three people for processing:
One person makes roughly husked millet (li mi), one makes finely husked millet (bai mi), and one makes polished millet (zao mi).
The resulting amounts of millet are to be equal.
Question: how much millet does each person take, and how much processed millet does each person produce?

The procedure says:
List the rates: 30 for li mi, 27 for bai mi, and 24 for zao mi.
Reverse these rates into their reciprocals, and add them together to form the divisor.
Multiply the total millet (7 dou) by the unreversed rates for each type, forming the millet-taking dividends.
Divide these dividends by the divisor to obtain the millet each person takes.
If the resulting millet amounts are to be equal, multiply the original rates by the millet each person takes to form the processed millet dividends.
Use the millet rate of 50 as the divisor.
Divide these dividends by the divisor to obtain the processed millet amounts.

Answer: li mi takes *a* dou of millet, bai mi takes *b* dou of millet, zao mi takes *c* dou of millet, and each produces *d* dou of processed millet.
"""

from fractions import Fraction

# Total millet
粟 = 7

# Rates for li mi, bai mi, and zao mi
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# Reverse the rates (reciprocals) and sum them to form the divisor
法 = Fraction(1, 糲米率) + Fraction(1, 粺米率) + Fraction(1, 鑿米率)

# Multiply total millet by unreversed rates to form dividends
糲米取粟實 = 粟 * 糲米率
粺米取粟實 = 粟 * 粺米率
鑿米取粟實 = 粟 * 鑿米率

# Divide dividends by the divisor to get the millet each person takes
a = Fraction(糲米取粟實, 法.denominator * 法.numerator)
b = Fraction(粺米取粟實, 法.denominator * 法.numerator)
c = Fraction(鑿米取粟實, 法.denominator * 法.numerator)

# Multiply the original rates by the millet each person takes to form processed millet dividends
糲米實 = a * 糲米率
粺米實 = b * 粺米率
鑿米實 = c * 鑿米率

# Use the millet rate of 50 as the divisor
粟率 = 50

# Divide processed millet dividends by the divisor to get the processed millet amounts
d = Fraction(糲米實, 粟率)  # Since 米數等, all processed millet amounts are the same

# Final results
a, b, c, d
"""
Variable 'a' has wrong value. Expected: 252/121, Actual: 7/4356
Variable 'b' has wrong value. Expected: 280/121, Actual: 7/4840
Variable 'c' has wrong value. Expected: 315/121, Actual: 7/5445
Variable 'd' has wrong value. Expected: 756/605, Actual: 7/7260"""
