"""
今有米一千五百三十二斛七斗欲貸與人毎八升加息一升問本息共幾何
術曰置米數以九因八除之若求元數八因九除之
答曰 a斛
"""

#----- content starts here -----
"""
Suppose there are 1532 hu and 7 dou of rice, which are to be lent to someone.
For every 8 sheng lent, 1 sheng is added as interest.
Question: what is the total amount of principal and interest?

The procedure says: Place the amount of rice.
Multiply it by 9 and divide by 8 to find the total (principal + interest).
If seeking the original amount (principal) from the total, multiply by 8 and divide by 9.

Answer: *a* hu.
"""

from fractions import Fraction

# 米一千五百三十二斛七斗
米 = 1532 + Fraction(7, 10)  # Convert 7 dou to hu (1 dou = 1/10 hu)

# 每八升加息一升
# 置米數，以九因八除之
總數 = 米 * 9 / 8

a = 總數#----- content ends here -----

"""
"""
