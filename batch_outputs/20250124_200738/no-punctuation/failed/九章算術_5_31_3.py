"""
今有委米依垣內角下周八尺高五尺問積及為米幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為米 b斛  c斛 
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall.
The base circumference is 8 chi, and the height is 5 chi.
Question: What is the volume of the pile, and how much rice does it represent?

The procedure for piled grain says:
- For a pile leaning against the inner corner of a wall, multiply the base circumference by itself, then multiply by the height, and divide by 9.
- For a pile leaning against a wall, divide by 18.
- For a free-standing pile, divide by 36.
- For rice, 1 hu occupies 1 chi 6 cun 5 fen (1.65 chi³).
- For millet, 1 hu occupies 2 chi 7 cun (2.7 chi³).
- For beans, hemp, and wheat, 1 hu occupies 2 chi 4 cun 3 fen (2.43 chi³).

Answer: The volume is *a* chi³, and it represents *b* hu of rice, and *c* hu of millet.
"""

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 委粟術曰：下周自乘
積 = 下周 * 下周

# 以高乘之
積 *= 高

# 其依垣內角者，九而一
積 /= 9

# 積 a尺
a = Fraction(積)

# 其米一斛積一尺六寸五分寸之一 (1.65 chi³ per hu)
米體積 = Fraction(165, 100)

# 其粟一斛積二尺七寸 (2.7 chi³ per hu)
粟體積 = Fraction(27, 10)

# 為米 b斛
b = Fraction(a, 米體積)

# 為粟 c斛
c = Fraction(a, 粟體積)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320/9, Actual: 2501999792983609/70368744177664
Variable 'b' has wrong value. Expected: 21, Actual: 12509998964918045/580542139465728
Variable 'c' has wrong value. Expected: 691/729, Actual: 12509998964918045/949978046398464"""
