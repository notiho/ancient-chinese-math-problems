"""
今有委米依垣內角下周八尺高五尺問積及為米幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為米 b斛  c斛 
"""

"""
Suppose there is a pile of rice leaning against the inner corner of a wall. 
Its base circumference is 8 chi, and its height is 5 chi.
Question: what is the volume of the pile, and how much rice does it represent?

The procedure for piled grain says: 
1. For the base circumference, square it and multiply by the height.
2. Divide by 36 for a free-standing pile.
3. Divide by 18 for a pile leaning against a wall.
4. Divide by 9 for a pile leaning against the inner corner of a wall.

For rice, 1 hu occupies a volume of 2 chi 7 cun.
For millet, 1 hu occupies a volume of 1 chi 6 cun 5 fen.
For beans, hemp, and wheat, 1 hu occupies a volume of 2 chi 4 cun 3 fen.

Answer: the volume is *a* chi³, and it represents *b* hu of rice and *c* hu of millet.
"""

# 下周 8 尺
下周 = 8

# 高 5 尺
高 = 5

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 其依垣內角者，九而一
積 = Fraction(積, 9)

# 積 a 尺³
a = 積

# 程粟一斛積二尺七寸
粟一斛積 = 2 + Fraction(7, 10)

# 其米一斛積一尺六寸五分寸之一
米一斛積 = 1 + Fraction(6, 10) + Fraction(5, 100)

# 積換算為粟斛數
b = Fraction(積, 粟一斛積)

# 積換算為米斛數
c = Fraction(積, 米一斛積)
"""
Variable 'b' has wrong value. Expected: 21, Actual: 3200/243
Variable 'c' has wrong value. Expected: 691/729, Actual: 6400/297"""
