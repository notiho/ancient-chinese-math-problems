"""
今有米一千五百三十二斛七斗欲貸與人毎八升加息一升問本息共幾何
術曰置米數以九因八除之若求元數八因九除之
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 1532 hu and 7 dou of rice, which is to be lent to someone.
For every 8 sheng lent, an interest of 1 sheng is added.
Question: what is the total of the principal and interest?

The procedure says: Place the amount of rice and multiply it by 9. Divide it by 8.
If seeking the principal amount, multiply by 8 and divide by 9.

Answer: *a* hu.
"""

from fractions import Fraction

# 米一千五百三十二斛七斗
米 = 1532 + Fraction(7, 10)  # Convert 7 dou to hu (1 dou = 1/10 hu)

# 每八升加息一升
# 置米數，以九因八除之
a = 米 * 9 / 8#----- content ends here -----

"""
"""
