"""
今有委米依垣內角下周八尺高五尺問積及為米幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為米 b斛  c斛 
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall.
The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume of the pile, and how much rice does it represent?

The procedure for piled grain says:
- For a pile leaning against the inner corner of a wall, multiply the base circumference by itself, then multiply by the height, and divide by 9.
- For a pile leaning against a wall, divide by 18.
- For a freestanding pile, divide by 36.

For rice:
- 1 hu of rice occupies a volume of 1 chi 6 cun 5 fen (1.65 chi³).
- For millet, beans, sesame, and wheat, 1 hu occupies 2 chi 4 cun 3 fen (2.43 chi³).

Answer: the volume is *a* chi³, and it represents *b* hu of rice and *c* hu of other grains.
"""

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 依垣內角者，九而一
積 = (下周 ** 2) * 高 / 9

# 程粟一斛積一尺六寸五分寸之一 (1.65 chi³ per hu for rice)
米體積 = Fraction(165, 100)

# 其菽答麻麥一斛皆二尺四寸十分寸之三 (2.43 chi³ per hu for other grains)
其他穀物體積 = Fraction(243, 100)

# 計算米斛數
米斛數 = 積 / 米體積

# 計算其他穀物斛數
其他穀物斛數 = 積 / 其他穀物體積

a = 積
b = 米斛數
c = 其他穀物斛數#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320/9, Actual: 35.55555555555556
Variable 'b' has wrong value. Expected: 21, Actual: 21.54882154882155
Variable 'c' has wrong value. Expected: 691/729, Actual: 14.631915866483768"""
