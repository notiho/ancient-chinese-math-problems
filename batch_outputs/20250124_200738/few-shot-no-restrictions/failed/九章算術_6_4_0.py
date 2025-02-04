"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are tasked with processing it. 
One person produces roughly husked millet (糲米), another produces semi-polished millet (粺米), and the third produces fully polished millet (鑿米). 
The resulting amounts of rice must be equal for all three.

Question: how much millet does each person take to produce their rice, and how much rice does each person produce?

The procedure says:
1. Arrange the rates: 30 for roughly husked millet (糲米), 27 for semi-polished millet (粺米), and 24 for fully polished millet (鑿米). Reverse the rates to form a decreasing sequence.
2. Add the reversed rates to form the divisor (法).
3. Multiply the 7 dou of millet by the unreversed rates to form the dividends (實). Divide each dividend by the divisor to determine how much millet each person takes.
4. To ensure the rice amounts are equal, multiply the original rates by the millet each person takes, then divide by the millet rate (50) to determine the rice produced.

Answer:
- 糲米 takes *a* dou of millet.
- 粺米 takes *b* dou of millet.
- 鑿米 takes *c* dou of millet.
- Each person produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 米率
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 反衰之 (reverse the rates)
反糲米率 = 1 / 糲米率
反粺米率 = 1 / 粺米率
反鑿米率 = 1 / 鑿米率

# 副并為法 (sum the reversed rates to form the divisor)
法 = 反糲米率 + 反粺米率 + 反鑿米率

# 以七斗乘未并者 (multiply 7 dou by the unreversed rates)
糲米實 = 粟 * 反糲米率
粺米實 = 粟 * 反粺米率
鑿米實 = 粟 * 反鑿米率

# 實如法得取粟 (divide each dividend by the divisor to determine millet taken)
a = Fraction(糲米實, 法)
b = Fraction(粺米實, 法)
c = Fraction(鑿米實, 法)

# 若求米等者 (to ensure rice amounts are equal)
# 米率
粟率 = 50

# Calculate the rice produced by each person
糲米產量 = Fraction(a * 糲米率, 粟率)
粺米產量 = Fraction(b * 粺米率, 粟率)
鑿米產量 = Fraction(c * 鑿米率, 粟率)

# Since rice amounts are equal:
d = 糲米產量  # or 粺米產量 or 鑿米產量 (all are equal)

# Final answers
a, b, c, d#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
