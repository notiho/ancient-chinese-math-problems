"""
今有委米依垣內角下周八尺高五尺問積及為米幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為米 b斛  c斛 
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall.
The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume, and how much rice does it make?

The procedure for piled grain says:
- For the base circumference, square it, then multiply by the height.
- Divide by 36 for a full pile.
- For a pile leaning against a wall, divide by 18.
- For a pile leaning against the inner corner of a wall, divide by 9.

For rice:
- 1 dou of rice occupies a volume of 2 chi 7 cun (2.7 chi).
- 1 dou of millet occupies a volume of 1 chi 6 cun 5 fen (1.65 chi).
- 1 dou of beans, hemp, or wheat occupies a volume of 2 chi 4 cun 3 fen (2.43 chi).

Answer: the volume is *a* chi³, and it makes *b* dou of rice and *c* dou of millet.
"""

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 其依垣內角者九而一
分母 = 9

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 九而一
積 = Fraction(積, 分母)

# 積 a 尺³
a = 積

# 程粟一斛積二尺七寸 (2.7 chi)
粟體積 = Fraction(27, 10)

# 其米一斛積一尺六寸五分寸之一 (1.65 chi)
米體積 = Fraction(165, 100)

# 為米 b 斛
b = 積 / 粟體積

# 為米 c 斛
c = 積 / 米體積#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 21, Actual: 3200/243
Variable 'c' has wrong value. Expected: 691/729, Actual: 6400/297"""
