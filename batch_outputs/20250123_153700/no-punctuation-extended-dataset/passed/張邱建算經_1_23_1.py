"""
今有器容九㪷中有米不知其數滿中粟舂之得米五㪷八升問滿粟㡬何
術曰置器容九㪷以米數減之餘以五之二而一得滿粟斗數
答曰 a㪷
"""

"""
Suppose there is a container with a capacity of 9 dou. It contains an unknown amount of rice. 
When filled with millet and then husked, it produces 5 dou and 8 sheng of rice.
Question: how much millet fills the container?

The procedure says: Place the container's capacity of 9 dou. Subtract the amount of rice from it. 
Take the remainder, multiply it by 5, and divide by 2. This gives the number of dou of millet that fills the container.

Answer: *a* dou.
"""

from fractions import Fraction

# 器容九㪷
器容 = 9

# 米數五㪷八升 (convert to dou, 1 dou = 10 sheng)
米數 = 5 + Fraction(8, 10)

# 以米數減之
餘 = 器容 - 米數

# 餘以五之
實 = 5 * 餘

# 二而一
a = Fraction(實, 2)
"""
"""
