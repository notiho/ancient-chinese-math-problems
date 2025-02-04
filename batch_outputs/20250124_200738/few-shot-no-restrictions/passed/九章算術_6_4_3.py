"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are tasked with processing it. 
One person produces roughly husked millet (糲米), another produces semi-polished millet (粺米), and the third produces polished millet (鑿米). 
The resulting amounts of millet must be equal. 
Question: how much millet does each person take to process, and how much rice does each person produce?

The procedure says:
- Place the rates for roughly husked millet (30), semi-polished millet (27), and polished millet (24) in a line, and reverse them into a decreasing sequence.
- Add them together to form the divisor (法).
- Multiply the 7 dou of millet by the reversed rates to form the dividends (實).
- Divide the dividends by the divisor to determine how much millet each person takes.
- To ensure the resulting rice amounts are equal, multiply the millet taken by each person by their respective rates, and divide by the millet rate (50).

Answer:
- 糲米 takes *a* dou of millet, 粺米 takes *b* dou of millet, 鑿米 takes *c* dou of millet.
- Each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 米率
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 粟率
粟率 = 50

# 反衰之 (reverse the rates)
反糲米率 = Fraction(1, 糲米率)
反粺米率 = Fraction(1, 粺米率)
反鑿米率 = Fraction(1, 鑿米率)

# 副并為法 (sum the reversed rates to form the divisor)
法 = 反糲米率 + 反粺米率 + 反鑿米率

# 以七斗乘未并者，各自為取粟實 (calculate the millet each person takes)
糲米取粟 = Fraction(粟, 1) * 反糲米率 / 法
粺米取粟 = Fraction(粟, 1) * 反粺米率 / 法
鑿米取粟 = Fraction(粟, 1) * 反鑿米率 / 法

# 若求米等者，以本率各乘定所取粟為實 (calculate the rice produced by each person)
糲米產米 = 糲米取粟 * 糲米率 / 粟率
粺米產米 = 粺米取粟 * 粺米率 / 粟率
鑿米產米 = 鑿米取粟 * 鑿米率 / 粟率

# Results
a = 糲米取粟
b = 粺米取粟
c = 鑿米取粟
d = 糲米產米  # All rice amounts are equal, so we can use any one of them

# Output
a, b, c, d#----- content ends here -----

"""
"""
