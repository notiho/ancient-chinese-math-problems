"""
今有器中米，不知其數，前人取半，中人三分取一，後人四分取一，餘米一斗五升。問：米幾何？
術曰：置餘米一斗五升，以六乘之，得九斗；以二除之，得四斗五升；以四乘之，得一斛八斗；以三除之，即得。
答曰： a斗 。
"""

#----- content starts here -----
"""
Suppose there is a container of rice, but the total amount is unknown.
The first person takes half, the second person takes one-third, and the third person takes one-fourth.
The remaining rice is 1 dou and 5 sheng.
Question: how much rice was originally in the container?

The procedure says: Place the remaining rice, 1 dou and 5 sheng, and multiply it by 6, obtaining 9 dou.
Divide it by 2, obtaining 4 dou and 5 sheng.
Multiply it by 4, obtaining 1 hu and 8 dou.
Divide it by 3, and the result is the total amount of rice.

Answer: *a* dou.
"""

from fractions import Fraction

# 餘米一斗五升
餘米 = 1 + Fraction(5, 10)  # Convert 1 dou 5 sheng to dou (1 dou = 10 sheng)

# 以六乘之
步驟1 = 6 * 餘米  # 得九斗

# 以二除之
步驟2 = Fraction(步驟1, 2)  # 得四斗五升

# 以四乘之
步驟3 = 4 * 步驟2  # 得一斛八斗 (1 hu = 10 dou)

# 以三除之
a = Fraction(步驟3, 3)  # 即得

# Answer
a  # 米的總數 in dou#----- content ends here -----

"""
"""
