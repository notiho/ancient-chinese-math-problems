"""
今有粟七斗三人分舂之一人為糲米一人為粺米一人為鑿米令米數等問取粟為米各幾何
術曰列置糲米三十粺米二十七鑿米二十四而反衰之副并為法以七斗乘未并者各自為取粟實實如法得一斗若求米等者以本率各乘定所取粟為實以粟率五十為法實如法得一斗
荅曰糲米取粟 a斗 粺米取粟 b斗 鑿米取粟 c斗 為米各 d斗 
"""

"""
Suppose there are 7 dou of millet to be divided among three people for milling.
One person makes roughly husked millet (li mi), one makes finely husked millet (bai mi), and one makes polished millet (zao mi).
The milled rice quantities are to be equal.
Question: how much millet does each person take, and how much rice does each person produce?

The procedure says:
1. Place the rates: 30 for li mi, 27 for bai mi, and 24 for zao mi, and reverse them into a decreasing sequence.
2. Add these reversed rates together to form the divisor.
3. Multiply the 7 dou by the unreversed rates, each becoming its own millet-taking dividend.
4. Divide each dividend by the divisor to obtain the millet taken by each person.
5. If seeking equal rice quantities:
   - Multiply the millet taken by the original rates to form the rice-producing dividends.
   - Use the millet rate of 50 as the divisor.
   - Divide each dividend by the divisor to obtain the rice produced by each person.

Answer: li mi takes *a* dou of millet, bai mi takes *b* dou of millet, zao mi takes *c* dou of millet, and each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
總粟 = 7

# 糲米三十, 粺米二十七, 鑿米二十四
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 反衰之 (reverse the rates)
反衰率 = [Fraction(1, 糲米率), Fraction(1, 粺米率), Fraction(1, 鑿米率)]

# 副并為法 (sum the reversed rates to form the divisor)
法 = sum(反衰率)

# 以七斗乘未并者 (multiply the total millet by the original rates)
糲米取粟實 = 總粟 * Fraction(1, 糲米率) / 法
粺米取粟實 = 總
"""
Code error: name '總' is not defined"""
