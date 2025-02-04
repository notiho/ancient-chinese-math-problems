"""
今有粟七斗三人分舂之一人為糲米一人為粺米一人為鑿米令米數等問取粟為米各幾何
術曰列置糲米三十粺米二十七鑿米二十四而反衰之副并為法以七斗乘未并者各自為取粟實實如法得一斗若求米等者以本率各乘定所取粟為實以粟率五十為法實如法得一斗
荅曰糲米取粟 a斗 粺米取粟 b斗 鑿米取粟 c斗 為米各 d斗 
"""

"""
Suppose there are 7 dou of millet to be divided among three people for milling.
One person produces roughly husked millet (li mi), one produces semi-polished millet (bai mi), and one produces polished millet (zao mi).
The milled rice quantities are to be equal.
Question: how much millet does each person take, and how much rice does each person produce?

The procedure says:
List the rates: 30 for li mi, 27 for bai mi, and 24 for zao mi.
Reverse these rates to form a decreasing sequence.
Add them together to form the divisor.
Multiply the 7 dou of millet by the unreversed rates to form the millet-taking dividends.
Divide these dividends by the divisor to find the millet each person takes.
If the milled rice quantities are to be equal, multiply the millet taken by the original rates to form the rice-producing dividends.
Divide these dividends by the millet rate (50) to find the rice each person produces.

Answer: li mi takes *a* dou of millet, bai mi takes *b* dou of millet, zao mi takes *c* dou of millet.
Each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 糲米三十, 粺米二十七, 鑿米二十四
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 列置糲米三十, 粺米二十七, 鑿米二十四而反衰之
反衰率 = [Fraction(1, 糲米率), Fraction(1, 粺米率), Fraction(1, 鑿米率)]

# 副并為法
法 = sum(反衰率)

# 以七斗乘未并者各自為取粟實
糲米取粟實 = Fraction(粟, 1) * Fraction(1, 糲米率) / 法
粺米取粟實 = Fraction(粟, 1)
"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
