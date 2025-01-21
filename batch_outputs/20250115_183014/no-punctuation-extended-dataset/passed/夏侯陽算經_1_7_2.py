"""
今有粟五千五百一十斛九斗欲毎斛為糲米六斗粺米五斗四升糳米四斗八升御米四斗二升問各幾何
術曰置粟退一等以六斗乗為糲米以五斗四升乗為粺米以四斗八升乗為糳米以四斗二升乗為御米返求粟法置糲米數以五因之三除之置粺米數以上十之以五斗四升除之糳米各以本米數除之皆得本粟
答曰糲米 a斛 粺米 b斛 糳米 c斛 御米 d斛
"""

"""
Suppose there are 5510 hu and 9 dou of millet. It is desired to convert each hu into:
6 dou of roughly husked millet (li mi),
5 dou and 4 sheng of finely husked millet (pai mi),
4 dou and 8 sheng of coarsely husked millet (zao mi),
and 4 dou and 2 sheng of polished millet (yu mi).
Question: how much of each type of millet is obtained?

The procedure says:
- Place the millet and reduce it by one grade (convert hu to dou).
- Multiply by 6 dou to obtain li mi.
- Multiply by 5 dou and 4 sheng to obtain pai mi.
- Multiply by 4 dou and 8 sheng to obtain zao mi.
- Multiply by 4 dou and 2 sheng to obtain yu mi.
To reverse and find the millet:
- Place the amount of li mi, multiply by 5, and divide by 3.
- Place the amount of pai mi, multiply by 10, and divide by 5 dou and 4 sheng.
- For zao mi and yu mi, divide each by its respective conversion factor to find the original millet.

Answer: li mi is *a* hu, pai mi is *b* hu, zao mi is *c* hu, yu mi is *d* hu.
"""

# 粟五千五百一十斛九斗
粟 = 5510 + Fraction(9, 10)  # Convert to hu (1 hu = 10 dou)

# 每斛為糲米六斗
糲米率 = 6

# 每斛為粺米五斗四升
粺米率 = 5 + Fraction(4, 10)  # Convert 4 sheng to dou (1 dou = 10 sheng)

# 每斛為糳米四斗八升
糳米率 = 4 + Fraction(8, 10)  # Convert 8 sheng to dou

# 每斛為御米四斗二升
御米率 = 4 + Fraction(2, 10)  # Convert 2 sheng to dou

# 置粟退一等 (convert hu to dou)
粟斗 = 10 * 粟

# 以六斗乘為糲米
糲米 = 糲米率 * 粟

# 以五斗四升乘為粺米
粺米 = 粺米率 * 粟

# 以四斗八升乘為糳米
糳米 = 糳米率 * 粟

# 以四斗二升乘為御米
御米 = 御米率 * 粟

# Convert results back to hu
a = Fraction(糲米, 10)  # Convert dou to hu
b = Fraction(粺米, 10)  # Convert dou to hu
c = Fraction(糳米, 10)  # Convert dou to hu
d = Fraction(御米, 10)  # Convert dou to hu
"""
"""
