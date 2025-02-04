"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall. 
The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume and how many dou (or hu) of rice does it make?

The procedure for piled grain says: 
- Multiply the base circumference by itself, then multiply by the height, and divide by 36.
- If it leans against a wall, divide by 18.
- If it leans against the inner corner of a wall, divide by 9.

For rice:
- 1 hu of rice occupies 1 chi 6 cun and 1/5 cun (or 1.65 chi³).
- For millet, beans, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun (or 2.43 chi³).

Answer: the volume is *a* chi³. It makes *b* hu and *c* dou of rice.
"""

from fractions import Fraction

# 下周八尺
下周 = 8

# 高五尺
高 = 5

# 積計算：其依垣內角者，九而一
積 = (下周 ** 2) * 高 / 9

# 米一斛，積一尺六寸、五分寸之一 (1.65 chi³ per hu)
米一斛積 = Fraction(165, 100)

# 計算米的斛數
米斛數 = 積 / 米一斛積

# 分解為整斛和斗 (1 hu = 10 dou)
b = 米斛數.numerator // 米斛數.denominator  # 整斛數
c = (米斛數 - b) * 10  # 剩餘斗數

# 結果
a = 積
b = int(b)
c = round(float(c), 2)

a, b, c#----- content ends here -----

"""
Code error: 'float' object has no attribute 'numerator'"""
