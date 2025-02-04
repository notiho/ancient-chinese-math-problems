"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, divided among three people for processing. 
One person produces roughly husked millet (li mi), one produces finely husked millet (pai mi), and one produces polished millet (zao mi), such that the amount of rice is equal for all.
Question: how much millet does each person take to produce their rice, and how much rice does each person produce?

The procedure says: Arrange the rates for li mi as 30, pai mi as 27, and zao mi as 24, and reverse their proportions. 
Add these reversed proportions together to form the divisor.
Multiply the 7 dou by the unreversed proportions, with each becoming its own millet-taking dividend.
Divide the dividends by the divisor to obtain the millet taken by each person.
If seeking equal rice amounts, multiply the original rates by the millet taken by each person to form dividends.
Use the millet rate of 50 as the divisor. Divide the dividends by the divisor to obtain the rice produced by each person.

Answer: The li mi producer takes *a* dou of millet, the pai mi producer takes *b* dou of millet, the zao mi producer takes *c* dou of millet, and each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 列置糲米三十，粺米二十七，鑿米二十四
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 而反衰之
反糲米率 = Fraction(1, 糲米率)
反粺米率 = Fraction(1, 粺米率)
反鑿米率 = Fraction(1, 鑿米率)

# 副并為法
法 = 反糲米率 + 反粺米率 + 反鑿米率

# 以七斗乘未并者，各自為取粟實
糲米取粟實 = Fraction(粟, 1) * 反糲米率
粺米取粟實 = Fraction(粟, 1) * 反粺米率
鑿米取粟實 = Fraction(粟, 1) * 反鑿米率

# 實如法得一斗
a = 糲米取粟實 / 法
b = 粺米取粟實 / 法
c = 鑿米取粟實 / 法

# 若求米等者，以本率各乘定所取粟為實
糲米實 = 糲米率 * a
粺米實 = 粺米率 * b
鑿米實 = 鑿米率 * c

# 以粟率五十為法
粟率 = 50

# 實如法得一斗
d = 糲米實 / 粟率  # 米數等，所有人產出相同的米數

# Final results
a, b, c, d#----- content ends here -----

"""
"""
