"""
今有粟七斗三人分舂之一人為糲米一人為粺米一人為鑿米令米數等問取粟為米各幾何
術曰列置糲米三十粺米二十七鑿米二十四而反衰之副并為法以七斗乘未并者各自為取粟實實如法得一斗若求米等者以本率各乘定所取粟為實以粟率五十為法實如法得一斗
荅曰糲米取粟 a斗 粺米取粟 b斗 鑿米取粟 c斗 為米各 d斗 
"""

"""
Suppose there are 7 dou of millet to be divided among three people for processing.
One person makes roughly husked millet (li mi), one makes finely husked millet (pai mi), and one makes polished millet (zao mi).
The resulting amounts of millet must be equal.
Question: how much millet does each person take, and how much processed millet does each produce?

The procedure says:
List the rates: 30 for li mi, 27 for pai mi, and 24 for zao mi.
Reverse the rates to form a decreasing sequence.
Add them together to form the divisor.
Multiply the 7 dou by the reversed rates to form the millet-taking dividends.
Divide the dividends by the divisor to find the millet taken by each person.
If the resulting millet amounts are equal, multiply the millet taken by each person by their respective rates to form the processed millet dividends.
Divide these dividends by the millet rate (50) to find the processed millet amounts.

Answer: li mi takes *a* dou of millet, pai mi takes *b* dou of millet, zao mi takes *c* dou of millet, and each produces *d* dou of processed millet.
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
取粟實 = [粟 * rate for rate in 反衰率]

# 實如法得一斗 (取粟)
取粟 = [實 / 法 for 実 in 取粟實]
a, b, c = 取粟

# 若求米等者以本率各乘定所取粟為實
米實 = [取粟[i] * rate for i, rate in enumerate([糲米率, 粺米率, 鑿米率])]

# 以粟率五十為法
粟率 = 50

# 實如法得一斗 (為米)
為米 = [實 / 粟率 for 実 in 米實]
d = 為米[0]  # All 米 amounts are equal

# Final results
a, b, c, d
"""
Code error: name '實' is not defined"""
