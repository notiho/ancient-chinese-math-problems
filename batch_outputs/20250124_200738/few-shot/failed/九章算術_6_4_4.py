"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are tasked with processing it. 
One person produces roughly husked millet (li mi), another produces finely husked millet (bai mi), and the third produces polished millet (zao mi). 
The resulting rice quantities are to be equal. 
Question: how much millet does each person take, and how much rice does each person produce?

The procedure says: Arrange the rates for li mi as 30, bai mi as 27, and zao mi as 24, and reverse them into a decreasing sequence.
Add the reversed rates together to form the divisor.
Multiply the 7 dou of millet by the unreversed rates, and each becomes the millet taken by each person.
Divide by the divisor to get the millet each person takes.
If seeking equal rice quantities, multiply the original rates by the millet taken by each person to form the dividend.
Take the millet rate as 50 as the divisor.
Divide the dividend by the divisor to get the rice each person produces.

Answer: li mi takes *a* dou of millet, bai mi takes *b* dou of millet, zao mi takes *c* dou of millet. 
Each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 列置糲米三十，粺米二十七，鑿米二十四
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 而反衰之
反衰 = [Fraction(1, 糲米率), Fraction(1, 粺米率), Fraction(1, 鑿米率)]

# 副并為法
法 = sum(反衰)

# 以七斗乘未并者，各自為取粟實
糲米取粟實 = Fraction(粟, 糲米率) /法
#----- content ends here -----

"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'"""
