"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

"""
Suppose there are 7 dou of millet, and three people are tasked with processing it into different types of rice.
One person produces roughly husked rice (糲米), one produces moderately husked rice (粺米), and one produces finely husked rice (鑿米), such that the amount of rice produced is equal for all three.

Question: how much millet does each person take, and how much rice does each produce?

The procedure says:
1. Arrange the rates: 30 for 糲米, 27 for 粺米, and 24 for 鑿米. Reverse these rates to form a decreasing sequence.
2. Add the reversed rates to form the divisor (法).
3. Multiply the 7 dou of millet by the unreversed rates to form the dividend (實) for each type.
4. Divide the dividend by the divisor to determine how much millet each person takes.
5. To ensure equal rice amounts, multiply the millet taken by each person by their respective original rates to form the dividend (實) for rice.
6. Use the millet rate of 50 as the divisor (法) to calculate the amount of rice produced.

Answer: 糲米 takes *a* dou of millet, 粺米 takes *b* dou of millet, 鑿米 takes *c* dou of millet. Each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 列置糲米三十，粺米二十七，鑿米二十四
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 反衰之
反糲米率 = Fraction(1, 糲米率)
反粺米率 = Fraction(1, 粺米率)
反鑿米率 = Fraction(1, 鑿米率)

# 副并為法
法 = 反糲米率 + 反粺米率 + 反鑿米率

# 以七斗乘未并者，各自為取粟實
糲米取粟實 = 粟 * 反糲米率
粺米取粟實 = 粟 * 反粺米率
鑿米取粟實 = 粟 * 反鑿米率

# 實如法得一斗
a = 糲米取粟實 / 法
b = 粺米取粟實 / 法
c = 鑿米取粟實 / 法

# 若求米等者，以本率各乘定所取粟為實
糲米實 = a * 糲米率
粺米實 = b * 粺米率
鑿米實 = c * 鑿米率

# 以粟率五十為法
粟率 = 50

# 實如法得一斗
d = Fraction(糲米實, 粟率)  # All rice amounts are equal, so we only calculate once.

a, b, c, d  # Output the results
"""
"""
