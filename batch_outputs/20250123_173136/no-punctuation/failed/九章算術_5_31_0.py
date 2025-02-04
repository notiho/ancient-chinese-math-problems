"""
今有委米依垣內角下周八尺高五尺問積及為米幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為米 b斛  c斛 
"""

"""
Suppose there is a pile of rice leaning against the inner corner of a wall.
The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume of the pile, and how much rice does it represent?

The procedure for piled grain says: 
For the base circumference, square it, then multiply by the height.
Divide by 36 to obtain the volume.
If it leans against a wall, divide by 18.
If it leans against the inner corner of a wall, divide by 9.
For rice, 1 hu occupies 2 chi 7 cun of volume.
For rice grains, 1 hu occupies 1 chi 6 cun 5 fen of volume.
For beans, sesame, and wheat, 1 hu occupies 2 chi 4 cun 3 fen of volume.

Answer: the volume is *a* chi³, and it represents *b* hu of rice and *c* hu of rice grains.
"""

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
體積 = 下周平方 * 高

# 其依垣內角者九而一
積 = Fraction(體積, 9)

# 程粟一斛積二尺七寸
粟每斛積 = 2 + Fraction(7, 10)

# 其米一斛積一尺六寸五分寸之一
米每斛積 = 1 + Fraction(6, 10) + Fraction(5, 100)

# 積為米
b = Fraction(積, 粟每斛積)  # 粟
c = Fraction(積, 米每斛積)  # 米

a = 積
"""
Variable 'b' has wrong value. Expected: 21, Actual: 3200/243
Variable 'c' has wrong value. Expected: 691/729, Actual: 6400/297"""
