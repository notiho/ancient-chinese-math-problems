"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

"""
Suppose there is a pile of rice leaning against the inner corner of a wall. The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume, and how much rice does it make?

The procedure for piled grain says: Multiply the base circumference by itself, then multiply by the height, and divide by 36. 
If it leans against a wall, divide by 18. 
If it leans against the inner corner of a wall, divide by 9.

For rice, 1 hu occupies a volume of 1 chi 6 cun and 1/5 cun (or 1.65 chi³). 
For millet, 1 hu occupies a volume of 2 chi 7 cun (or 2.7 chi³). 
For beans, da, hemp, and wheat, 1 hu occupies a volume of 2 chi 4 cun and 3/10 cun (or 2.43 chi³).

Answer: the volume is *a* chi³. It makes *b* hu of rice and *c* hu of millet.
"""

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 下周自乘
下周積 = 下周 * 下周

# 以高乘之
體積 = 下周積 * 高

# 其依垣內角者，九而一
a = Fraction(體積, 9)

# 米一斛，積一尺六寸、五分寸之一 (1.65 chi³ per hu)
米每斛積 = Fraction(165, 100)

# 積為米幾何
b = a / 米每斛積

# 粟一斛，積二尺七寸 (2.7 chi³ per hu)
粟每斛積 = Fraction(27, 10)

# 積為粟幾何
c = a / 粟每斛積
"""
Variable 'b' has wrong value. Expected: 21, Actual: 6400/297
Variable 'c' has wrong value. Expected: 691/729, Actual: 3200/243"""
