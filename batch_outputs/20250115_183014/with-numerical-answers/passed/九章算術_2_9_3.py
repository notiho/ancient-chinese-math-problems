"""
今有粟九斗八升，欲為御飯。問︰得幾何？
術曰：以粟求御飯，二十一之，二十五而一。
荅曰：為御飯 a(=1029/125)斗 。
"""

"""
Suppose there are 9 dou and 8 sheng of millet. It is desired to turn it into prepared rice.
Question: how much prepared rice is obtained?

The procedure says: when seeking prepared rice from millet, multiply by 21 and divide by 25.

The answer says: *a*(=1029/125) dou of prepared rice.
"""

from fractions import Fraction

# 粟九斗八升
粟斗 = 9
粟升 = 8

# Convert to dou (1 dou = 10 sheng)
粟 =粟斗 + Fraction(粟升, 10)

# 以粟求御飯，二十一之
御飯 = 21 * 粟

# 二十五而一
a = Fraction(御飯, 25) # 1029/125
"""
"""
