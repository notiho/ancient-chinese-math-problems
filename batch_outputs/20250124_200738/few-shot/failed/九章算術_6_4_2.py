"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, divided among three people for processing.
One person makes roughly husked millet (li mi), one makes semi-polished millet (bai mi), and one makes polished millet (zao mi), such that the resulting amounts of rice are equal.
Question: how much millet does each person take, and how much rice does each produce?

The procedure says: Arrange the rates for li mi as 30, bai mi as 27, and zao mi as 24, and reverse them into a decreasing sequence.
Add them together to form the divisor.
Multiply the 7 dou of millet by the unreversed rates, each separately, to form the millet amounts.
Divide by the divisor to obtain the millet taken by each person.
If the rice amounts are to be equal, multiply the original rates by the millet amounts taken to form the rice amounts.
Use the millet rate of 50 as the divisor.
Divide the rice amounts by this divisor to obtain the rice amounts.

Answer: li mi takes *a* dou of millet, bai mi takes *b* dou of millet, zao mi takes *c* dou of millet, and each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 列置糲米三十，粺米二十七，鑿米二十四
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 而反衰之
反衰率 = [Fraction(1, 糲米率), Fraction(1, 粺米率), Fraction(1, 鑿米率)]

# 副并為法
法 = sum(反衰率)

# 以七斗乘未并者，各自為取粟實
糲米取粟實 = Fraction(粟, 反衰率[0])
粺米取粟實 =粟#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
