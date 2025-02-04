"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a(=320/9)尺 。為米 b(=21)斛 ， c(=691/729)斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall. 
The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume and how many hu of rice does it make?

The procedure for piled grain says: 
The base circumference is squared, then multiplied by the height, and divided by 36.
If it leans against a wall, divide by 18.
If it leans against the inner corner of a wall, divide by 9.
For rice, 1 hu occupies a volume of 1 chi 6 cun and 1/5 cun.
For millet, beans, hemp, and wheat, 1 hu occupies a volume of 2 chi 4 cun and 3/10 cun.

Answer: the volume is *a*(=320/9) chi³. 
It makes *b*(=21) hu and *c*(=691/729) hu of rice.
"""

from fractions import Fraction

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 其依垣內角者，九而一
積 = Fraction(積, 9)  # a = 320/9

# 程粟一斛，積一尺六寸、五分寸之一
一斛積 = Fraction(16, 10) + Fraction(1, 50)  # 1 chi 6 cun and 1/5 cun = 1.65 chi³

# 積及為米幾何
b = 積 // 一斛積  # Whole hu of rice = 21
c = 積 % 一斛積 / 一斛積  # Fractional part of hu = 691/729#----- content ends here -----

"""
Missing variable in output: 'a'"""
