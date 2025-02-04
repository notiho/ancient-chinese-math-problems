"""
今有器中米不知其數前人取半中人三分取一後人四分取一餘米一斗五升問米幾何
術曰置餘米一斗五升以六乘之得九斗以二除之得四斗五升以四乘之得一斛八斗以三除之即得
答曰 a斗 
"""

#----- content starts here -----
"""
Suppose there is a container with an unknown amount of rice.
The first person takes half, the second person takes one-third, and the last person takes one-fourth.
Afterward, 1 dou and 5 sheng of rice remain.
Question: how much rice was originally in the container?

The procedure says: Place the remaining rice, 1 dou and 5 sheng.
Multiply it by 6, obtaining 9 dou.
Divide it by 2, obtaining 4 dou and 5 sheng.
Multiply it by 4, obtaining 1 hu and 8 dou.
Divide it by 3, and the result is the original amount of rice.

Answer: *a* dou.
"""

# 餘米一斗五升
餘米 = 1 + Fraction(5, 10)  # Convert 1 dou 5 sheng to dou

# 以六乘之，得九斗
九斗 = 6 * 餘米

# 以二除之，得四斗五升
四斗五升 = 九斗 / 2

# 以四乘之，得一斛八斗
一斛八斗 = 4 * 四斗五升

# 以三除之，即得
a = 一斛八斗 / 3#----- content ends here -----

"""
"""
