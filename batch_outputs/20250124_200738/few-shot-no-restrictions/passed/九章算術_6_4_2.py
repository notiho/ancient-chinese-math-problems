"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people are dividing the task of pounding it into rice. 
One person produces roughly husked rice (糲米), one produces semi-polished rice (粺米), and one produces polished rice (鑿米). 
The rice amounts must be equal. 
Question: how much millet does each person take to produce their rice, and how much rice does each person produce?

The procedure says:
- Place the rates: 30 for roughly husked rice, 27 for semi-polished rice, and 24 for polished rice. Reverse these into decreasing weights.
- Add them together to form the divisor (法).
- Multiply the 7 dou of millet by the reversed rates to form the dividends (實).
- Divide the dividends by the divisor to determine how much millet each person takes.
- To determine the equal rice amounts, multiply the millet taken by each person by their respective rates (本率) to form the new dividends.
- Use the millet rate of 50 as the divisor (粟率), and divide the new dividends by this divisor to determine the rice amounts.

Answer:
- The roughly husked rice producer takes *a* dou of millet.
- The semi-polished rice producer takes *b* dou of millet.
- The polished rice producer takes *c* dou of millet.
- Each person produces *d* dou of rice.
"""

from fractions import Fraction

# 粟七斗
粟 = 7

# 糲米、粺米、鑿米的本率
糲米率 = 30
粺米率 = 27
鑿米率 = 24

# 反衰之 (逆序)
反衰率 = [Fraction(1, 糲米率), Fraction(1, 粺米率), Fraction(1, 鑿米率)]

# 副并為法
法 = sum(反衰率)

# 以七斗乘未并者，各自為取粟實
取粟實 = [粟 * rate for rate in 反衰率]

# 實如法得一斗 (每人取粟數)
a = 取粟實[0] / 法  # 糲米取粟
b = 取粟實[1] / 法  # 粺米取粟
c = 取粟實[2] / 法  # 鑿米取粟

# 若求米等者，以本率各乘定所取粟為實
糲米實 = a * 糲米率
粺米實 = b * 粺米率
鑿米實 = c * 鑿米率

# 以粟率五十為法
粟率 = 50

# 實如法得一斗 (每人產米數)
d = 糲米實 / 粟率  # 每人產米數 (米數相等)

# Output results
a, b, c, d#----- content ends here -----

"""
"""
