"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are tasked with processing it. 
One person produces roughly husked millet (糲米), another produces semi-polished millet (粺米), and the third produces fully polished millet (鑿米). 
The resulting rice amounts must be equal. 
Question: how much millet does each person take, and how much rice does each person produce?

The procedure says: 
List the rates for 糲米 as 30, 粺米 as 27, and 鑿米 as 24, and reverse them into a decreasing sequence. 
Add them together to get the divisor. 
Multiply the 7 dou of millet by the unreversed rates, obtaining the millet amounts for each person. 
Divide by the divisor to get the millet each person takes. 

If seeking equal rice amounts, multiply the base rates by the millet amounts each person takes, obtaining the rice amounts. 
Use the millet rate of 50 as the divisor. 
Divide the rice amounts by the divisor to get the rice each person produces.

Answer: 糲米 takes *a* dou of millet, 粺米 takes *b* dou of millet, 鑿米 takes *c* dou of millet. Each produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 糲米、粺米、鑿米的本率
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 反衰之 (反比率)
反比率 = [Fraction(1, 糲米率), Fraction(1, 粺米率), Fraction(1, 鑿米率)]

# 副并為法 (加總反比率)
法 = sum(反比率)

# 以七斗乘未并者，各自為取粟實
糲米取粟 = Fraction(粟, 法) * 反比率[0]
粺米取粟 = Fraction(粟, 法) * 反比率[1]
鑿米取粟 = Fraction(粟, 法) * 反比率[2]

# 若求米等者，以本率各乘定所取粟為實
糲米產米 = 糲米率 * 糲米取粟
粺米產米 = 粺米率 * 粺米取粟
鑿米產米 = 鑿米率 * 鑿米取粟

# 以粟率五十為法 (粟率 = 50)
粟率 = 50

# 實如法得一斗 (計算每人產米)
糲米得米 = Fraction(糲米產米, 粟率)
粺米得米 = Fraction(粺米產米, 粟率)
鑿米得米 = Fraction(鑿米產米, 粟率)

# 答案
a = 糲米取粟
b = 粺米取粟
c = 鑿米取粟
d = 糲米得米  # Since 米數等, d applies to all three

a, b, c, d#----- content ends here -----

"""
"""
