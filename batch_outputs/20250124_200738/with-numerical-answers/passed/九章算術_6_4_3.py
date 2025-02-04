"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a(=252/121)斗 。粺米取粟 b(=280/121)斗 。鑿米取粟 c(=315/121)斗 。為米各 d(=756/605)斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, divided among three people for processing:
One person produces roughly husked millet (li mi), one produces semi-polished millet (bai mi), and one produces polished millet (zao mi), such that the resulting amounts of millet are equal.
Question: how much millet does each person take to process into their respective type of rice?

The procedure says:
List the rates: 30 for li mi, 27 for bai mi, and 24 for zao mi, and reverse them into a decreasing sequence.
Add them together to form the divisor.
Multiply the 7 dou of millet by the unreversed rates, each becoming its own dividend.
Divide the dividends by the divisor to obtain the millet each person takes.
If seeking equal amounts of rice, multiply the original rates by the millet each person takes to form the dividend.
Use the millet rate of 50 as the divisor.
Divide the dividends by the divisor to obtain the equal amounts of rice.

Answer:
Li mi takes *a*(=252/121) dou of millet.
Bai mi takes *b*(=280/121) dou of millet.
Zao mi takes *c*(=315/121) dou of millet.
Each produces *d*(=756/605) dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 列置糲米三十，粺米二十七，鑿米二十四
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 而反衰之 (reverse the rates)
反糲米率 = Fraction(1, 糲米率)
反粺米率 = Fraction(1, 粺米率)
反鑿米率 = Fraction(1, 鑿米率)

# 副并為法 (sum the reversed rates to form the divisor)
法 = 反糲米率 + 反粺米率 + 反鑿米率

# 以七斗乘未并者，各自為取粟實 (multiply 7 dou by unreversed rates to form dividends)
糲米取粟實 = 粟 * 反糲米率
粺米取粟實 = 粟 * 反粺米率
鑿米取粟實 = 粟 * 反鑿米率

# 實如法得一斗 (divide the dividends by the divisor to get the millet each person takes)
a = Fraction(糲米取粟實, 法)  # 252/121
b = Fraction(粺米取粟實, 法)  # 280/121
c = Fraction(鑿米取粟實, 法)  # 315/121

# 若求米等者，以本率各乘定所取粟為實 (multiply original rates by millet taken to form rice dividends)
糲米實 = 糲米率 * a
粺米實 = 粺米率 * b
鑿米實 = 鑿米率 * c

# 以粟率五十為法 (use millet rate of 50 as divisor)
粟率 = 50

# 實如法得一斗 (divide rice dividends by the divisor to get equal amounts of rice)
d = Fraction(糲米實, 粟率)  # 756/605

# Final results:
# a = 252/121
# b = 280/121
# c = 315/121
# d = 756/605#----- content ends here -----

"""
"""
