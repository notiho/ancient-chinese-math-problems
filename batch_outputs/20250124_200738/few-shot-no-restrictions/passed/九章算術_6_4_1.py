"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

#----- content starts here -----
"""
Suppose there are 7 dou of millet, and three people divide the task of pounding it into rice. 
One person produces roughly husked rice (糲米), another produces semi-polished rice (粺米), and the third produces fully polished rice (鑿米), such that the resulting rice quantities are equal.
Question: how much millet should each person take to produce their respective rice, and how much rice does each person produce?

The procedure says:
- Place the rates for 糲米 (30), 粺米 (27), and 鑿米 (24), and reverse them into a decreasing sequence.
- Add them together to form the divisor.
- Multiply the 7 dou of millet by the reversed rates to form the dividends.
- Divide the dividends by the divisor to get the amount of millet each person takes.
- To find the equal rice quantities, multiply the millet each person takes by their respective rates, and divide by the millet rate (50).

Answer:
- 糲米 takes *a* dou of millet.
- 粺米 takes *b* dou of millet.
- 鑿米 takes *c* dou of millet.
- Each produces *d* dou of rice.
"""

from fractions import Fraction

# Initial data
總粟 = 7  # Total millet in dou
糲米率 = 30  # Rate for 糲米
粺米率 = 27  # Rate for 粺米
鑿米率 = 24  # Rate for 鑿米
粟率 = 50  # Millet rate for rice production

# Step 1: Reverse the rates (反衰之)
反糲米率 = Fraction(1, 糲米率)
反粺米率 = Fraction(1, 粺米率)
反鑿米率 = Fraction(1, 鑿米率)

# Step 2: Add the reversed rates to form the divisor (副并為法)
法 = 反糲米率 + 反粺米率 + 反鑿米率

# Step 3: Multiply the total millet by the reversed rates to form the dividends (以七斗乘未并者)
糲米取粟實 = 總粟 * 反糲米率
粺米取粟實 = 總粟 * 反粺米率
鑿米取粟實 = 總粟 * 反鑿米率

# Step 4: Divide the dividends by the divisor to get the millet each person takes (實如法得一斗)
a = 糲米取粟實 / 法  # Millet taken for 糲米
b = 粺米取粟實 / 法  # Millet taken for 粺米
c = 鑿米取粟實 / 法  # Millet taken for 鑿米

# Step 5: Calculate the equal rice quantities
糲米產米 = (a * 糲米率) / 粟率
粺米產米 = (b * 粺米率) / 粟率
鑿米產米 = (c * 鑿米率) / 粟率

# Since the rice quantities are equal:
d = 糲米產米  # Equal rice quantity for all

# Final results
print(f"糲米取粟 {a} 斗")
print(f"粺米取粟 {b} 斗")
print(f"鑿米取粟 {c} 斗")
print(f"為米各 {d} 斗")#----- content ends here -----

"""
"""
