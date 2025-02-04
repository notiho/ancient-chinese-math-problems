"""
今有器中米，不知其數，前人取半，中人三分取一，後人四分取一，餘米一斗五升。問：米幾何？
術曰：置餘米一斗五升，以六乘之，得九斗；以二除之，得四斗五升；以四乘之，得一斛八斗；以三除之，即得。
答曰： a(=6)斗 。
"""

"""
Suppose there is rice in a container, but the amount is unknown.
The first person takes half, the second person takes one-third, and the last person takes one-fourth, leaving 1 dou and 5 sheng of rice.
Question: how much rice was there originally?

The procedure says: Place the remaining rice, 1 dou and 5 sheng.
Multiply it by 6, obtaining 9 dou.
Divide it by 2, obtaining 4 dou and 5 sheng.
Multiply it by 4, obtaining 1 hu and 8 dou.
Divide it by 3, obtaining the original amount.

Answer: *a*(=6) dou.
"""

from fractions import Fraction

# 餘米一斗五升
餘米 = 1 + Fraction(5, 10)  # 1 dou 5 sheng = 1.5 dou

# 以六乘之，得九斗
步驟1 = 6 * 餘米  # 9 dou

# 以二除之，得四斗五升
步驟2 = Fraction(步驟1, 2)  # 4.5 dou

# 以四乘之，得一斛八斗
步驟3 = 4 * 步驟2  # 18 dou = 1 hu 8 dou

# 以三除之，即得
a = Fraction(步驟3, 3)  # 6 dou
"""
"""
