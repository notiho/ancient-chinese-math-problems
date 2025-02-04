"""
今有粟一斗。問：為糲米幾何？
答曰： a升 。
"""

#----- content starts here -----
"""
Suppose there is 1 dou of unhusked millet. It is desired to turn it into roughly husked millet.
Question: how much does one obtain?

Answer: it makes *a* sheng of husked millet.
"""

from fractions import Fraction

# 粟一斗 (1 dou of unhusked millet)
粟 = 1  # 1 dou

# 1 dou = 10 sheng
粟_in_sheng = 10 * 粟

# Husked millet is obtained by multiplying by 3/5
a = Fraction(3 * 粟_in_sheng, 5)

# Output the result
a#----- content ends here -----

"""
"""
