"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為菽 b斛 。
"""

"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the total volume, and how many dou of beans does it make?

The procedure for piled grain says: Take the base circumference and square it, then multiply it by the height. Divide by 36 for a free-standing pile. For a pile leaning against a wall, divide by 18. For a pile leaning into a corner, divide by 9.
For beans, 1 hu occupies 2 chi 4 cun and 3/10 of a cun in volume.

Answer: the volume is *a* chi³, and it makes *b* hu of beans.
"""

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi

# 高七尺
高 = 7

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 其依垣者，十八而一
積依垣 = Fraction(積, 18)

# 程粟一斛，積二尺四寸、十分寸之三
一斛積 = 2 + Fraction(4, 10) + Fraction(3, 100)

# 計算為菽
為菽 = Fraction(積依垣, 一斛積)

# 答案
a = 積依垣  # 積 in chi³
b = 為菽  # 為菽 in hu
"""
"""
