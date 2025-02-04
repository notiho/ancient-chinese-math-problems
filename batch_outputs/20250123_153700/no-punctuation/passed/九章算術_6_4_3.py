"""
今有粟七斗三人分舂之一人為糲米一人為粺米一人為鑿米令米數等問取粟為米各幾何
術曰列置糲米三十粺米二十七鑿米二十四而反衰之副并為法以七斗乘未并者各自為取粟實實如法得一斗若求米等者以本率各乘定所取粟為實以粟率五十為法實如法得一斗
荅曰糲米取粟 a斗 粺米取粟 b斗 鑿米取粟 c斗 為米各 d斗 
"""

"""
Suppose there are 7 dou of millet to be divided among three people for milling.
One person mills roughly husked millet (糲米), one mills semi-polished millet (粺米), and one mills polished millet (鑿米), such that the resulting amounts of rice are equal.
Question: how much millet does each person take, and how much rice does each person produce?

The procedure says:
- Place the rates: 30 for roughly husked millet (糲米), 27 for semi-polished millet (粺米), and 24 for polished millet (鑿米).
- Reverse these rates to form a decreasing sequence.
- Add them together to form the divisor (法).
- Multiply the 7 dou of millet by the reversed rates, each becoming its own dividend (取粟實).
- Divide each dividend by the divisor to determine the millet taken by each person.
- To ensure the rice amounts are equal, multiply the millet taken by each person by their respective original rates (本率) to form the rice dividend (實).
- Use the millet rate of 50 as the divisor (粟率) to determine the rice produced by each person.

Answer: 糲米 takes *a* dou of millet, 粺米 takes *b* dou of millet, 鑿米 takes *c* dou of millet, and each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 列置糲米三十、粺米二十七、鑿米二十四
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
d = 糲米實 / 粟率  # 米數等，所有人產出的米數相同

a, b, c, d  # 糲米取粟 a斗, 粺米取粟 b斗, 鑿米取粟 c斗, 為米各 d斗
"""
"""
