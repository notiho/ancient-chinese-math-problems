"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall. 
The base circumference is 8 chi, and the height is 5 chi.
Question: What is the volume of the pile, and how many dou of rice does it contain?

The procedure for piled grain says:
- Multiply the base circumference by itself, then multiply by the height, and divide by 36.
- If the pile leans against a wall, divide by 18.
- If the pile leans against the inner corner of a wall, divide by 9.

For rice:
- 1 dou of rice occupies a volume of 1 chi 6 cun and 1/5 of a cun (or 1.65 chi³).
- For other grains like beans, millet, hemp, and wheat, 1 dou occupies 2 chi 4 cun and 3/10 of a cun (or 2.43 chi³).

Answer: The volume is *a* chi³. It contains *b* dou of rice and *c* dou of other grains.
"""

from fractions import Fraction

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 積計算 (依垣內角者，九而一)
積 = (下周 ** 2) * 高 / 9

# 米一斛，積一尺六寸五分寸之一 (1.65 尺³)
米一斛 = Fraction(165, 100)

# 菽、答、麻、麥一斛，積二尺四寸十分寸之三 (2.43 尺³)
其他一斛 = Fraction(243, 100)

# 計算米斛數
米斛數 = 積 / 米一斛

# 計算其他穀物斛數
其他斛數 = 積 / 其他一斛

# 結果
a = 積
b = 米斛數
c = 其他斛數

a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320/9, Actual: 35.55555555555556
Variable 'b' has wrong value. Expected: 21, Actual: 21.54882154882155
Variable 'c' has wrong value. Expected: 691/729, Actual: 14.631915866483768"""
