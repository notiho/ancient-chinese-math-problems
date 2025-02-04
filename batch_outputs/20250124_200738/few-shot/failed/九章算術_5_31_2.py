"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall.
The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume, and how much rice does it make?

The procedure for piled grain says: Multiply the base circumference by itself, then multiply by the height, and divide by 36.
For piles leaning against a wall, divide by 18.
For piles leaning against the inner corner of a wall, divide by 9.
For rice, 1 hu occupies a volume of 1 chi 6 cun and 1/5 cun.
For millet, beans, hemp, and wheat, 1 hu occupies a volume of 2 chi 4 cun and 3/10 cun.

Answer: the volume is *a* chi³. It makes *b* hu and *c* hu of rice.
"""

from fractions import Fraction

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 其依垣內角者，九而一
內角法 = 9

# 下周自乘
下周積 = 下周 * 下周

# 以高乘之
積 = 下周積 * 高

# 九而一
積 = Fraction(積, 內角法)

# 積 a尺
a = 積

# 其米一斛，積一尺六寸、五分寸之一
米一斛積 = 1 + Fraction(6, 10) + Fraction(1, 50)

# 為米 b斛，c斛
b = 積 // 米一斛積  # 整數部分
c = 積 % 米一斛積  # 餘數部分#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 691/729, Actual: 691/450"""
