"""
今有粟五千五百一十斛九斗欲毎斛為糲米六斗粺米五斗四升糳米四斗八升御米四斗二升問各幾何
術曰置粟退一等以六斗乗為糲米以五斗四升乗為粺米以四斗八升乗為糳米以四斗二升乗為御米返求粟法置糲米數以五因之三除之置粺米數以上十之以五斗四升除之糳米各以本米數除之皆得本粟
答曰糲米 a斛 粺米 b斛 糳米 c斛 御米 d斛
"""

"""
Suppose there are 5510 hu and 9 dou of millet. It is desired to convert each hu into:
6 dou of roughly husked millet (li mi),
5 dou and 4 sheng of finely husked millet (pai mi),
4 dou and 8 sheng of coarse rice (zao mi),
and 4 dou and 2 sheng of polished rice (yu mi).
Question: how much of each type is obtained?

The procedure says:
Place the millet and reduce it by one rank (convert hu to dou).
Multiply it by 6 to obtain li mi.
Multiply it by 5 dou and 4 sheng to obtain pai mi.
Multiply it by 4 dou and 8 sheng to obtain zao mi.
Multiply it by 4 dou and 2 sheng to obtain yu mi.

To reverse and find the millet:
Place the amount of li mi, multiply it by 5, and divide it by 3.
Place the amount of pai mi, multiply it by 10, and divide it by 5 dou and 4 sheng.
For zao mi and yu mi, divide each by its respective conversion factor to obtain the original millet.

Answer: li mi is *a* hu, pai mi is *b* hu, zao mi is *c* hu, yu mi is *d* hu.
"""

# 粟五千五百一十斛九斗
粟_斛 = 5510
粟_斗 = 9

# Convert 粟 to total dou (退一等)
粟 = 粟_斛 * 10 + 粟_斗

# 每斛為糲米六斗
糲米率 = 6

# 每斛為粺米五斗四升 (convert to dou)
粺米率 = 5 + Fraction(4, 10)

# 每斛為糳米四斗八升 (convert to dou)
糳米率 = 4 + Fraction(8, 10)

# 每斛為御米四斗二升 (convert to dou)
御米率 = 4 + Fraction(2, 10)

# 以六斗乘為糲米
糲米 = 粟 * 糲米率

# 以五斗四升乘為粺米
粺米 = 粟 * 粺米率

# 以四斗八升乘為糳米
糳米 = 粟 * 糳米率

# 以四斗二升乘為御米
御米 = 粟 * 御米率

# Convert results back to hu (divide by 10)
a = Fraction(糲米, 10)
b = Fraction(粺米, 10)
c = Fraction(糳米, 10)
d = Fraction(御米, 10)
"""
Variable 'a' has wrong value. Expected: 165327/50, Actual: 165327/5
Variable 'b' has wrong value. Expected: 1487943/500, Actual: 1487943/50
Variable 'c' has wrong value. Expected: 330654/125, Actual: 661308/25
Variable 'd' has wrong value. Expected: 1157289/500, Actual: 1157289/50"""
