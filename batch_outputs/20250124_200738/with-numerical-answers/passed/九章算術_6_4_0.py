"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a(=252/121)斗 。粺米取粟 b(=280/121)斗 。鑿米取粟 c(=315/121)斗 。為米各 d(=756/605)斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people divide the task of pounding it into rice.
One person produces roughly husked rice (li mi), one produces semi-polished rice (bai mi), and one produces polished rice (zao mi), such that the resulting rice quantities are equal.
Question: how much millet does each person take to produce their respective rice?

The procedure says: Arrange the rates for li mi as 30, bai mi as 27, and zao mi as 24, and invert them into a decreasing sequence.
Add these inverted rates together to form the divisor.
Multiply the 7 dou of millet by the uninverted rates, and each becomes its own millet-taking dividend.
Divide the dividends by the divisor to obtain the millet taken by each person.
If seeking equal rice quantities, multiply each millet taken by its respective rate to form the rice dividend.
Take the millet rate as 50 as the divisor, and divide the rice dividends by this divisor to obtain the rice quantities.

Answer: li mi takes *a*(=252/121) dou of millet, bai mi takes *b*(=280/121) dou of millet, zao mi takes *c*(=315/121) dou of millet.
Each produces *d*(=756/605) dou of rice.
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
糲米取粟實 = 粟 * Fraction(1, 糲米率)
粺米取粟實 = 粟 * Fraction(1, 粺米率)
鑿米取粟實 = 粟 * Fraction(1, 鑿米率)

# 實如法得一斗
a = Fraction(糲米取粟實, 法)  # 252/121
b = Fraction(粺米取粟實, 法)  # 280/121
c = Fraction(鑿米取粟實, 法)  # 315/121

# 若求米等者，以本率各乘定所取粟為實
糲米實 = a * 糲米率
粺米實 = b * 粺米率
鑿米實 = c * 鑿米率

# 以粟率五十為法
粟率 = 50

# 實如法得一斗
d = Fraction(糲米實, 粟率)  # 756/605
#----- content ends here -----

"""
"""
