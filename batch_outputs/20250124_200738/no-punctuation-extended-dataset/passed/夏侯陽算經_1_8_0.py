"""
今有榖一千八百四十三斛八斗三升欲依租變米毎穀三斛為米一斛四斗問合得米幾何
術曰置穀數以一斛四斗為法乗之以三斛為法除之
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 1843 hu, 8 dou, and 3 sheng of grain. It is desired to convert it into rice according to the rent ratio.
For every 3 hu of grain, it becomes 1 hu and 4 dou of rice.
Question: how much rice is obtained in total?

The procedure says: Place the amount of grain. Take 1 hu and 4 dou as the divisor. Multiply by it.
Take 3 hu as the divisor and divide by it.

Answer: *a* hu.
"""

from fractions import Fraction

# 榖一千八百四十三斛八斗三升
穀 = 1843 + Fraction(8, 10) + Fraction(3, 100)

# 每穀三斛為米一斛四斗
穀法 = 3
米法 = 1 + Fraction(4, 10)

# 置穀數，以一斛四斗為法，乘之
實 = 穀 * 米法

# 以三斛為法，除之
a = 實 / 穀法#----- content ends here -----

"""
"""
