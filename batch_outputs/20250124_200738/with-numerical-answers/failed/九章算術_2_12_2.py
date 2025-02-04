"""
今有粟五斗、太半升，欲為麻。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為麻 a(=114/25)斗 。
"""

#----- content starts here -----
"""
Suppose there are 5 dou and half a sheng of millet. It is desired to convert it into hemp (ma).
Question: how much hemp is obtained?

The procedure says: When seeking beans (shu), da, hemp (ma), or wheat (mai) from millet, multiply by 9 and divide by 10.

Answer: it makes *a*(=114/25) dou of hemp.
"""

# 粟五斗、太半升
粟 = 5 + Fraction(1, 20)  # Convert 5 dou and half a sheng to dou (1 sheng = 1/10 dou)

# 以粟求麻，皆九之
麻 = 9 * 粟

# 十而一
a = Fraction(麻, 10)  # 114/25 dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/200"""
