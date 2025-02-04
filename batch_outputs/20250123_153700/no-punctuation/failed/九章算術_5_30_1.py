"""
今有委菽依垣下周三丈高七尺問積及為菽各幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為菽 b斛 
"""

"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many dou of beans does it make?

The procedure for piles of grain says: 
For a pile leaning against a wall, take the base circumference, square it, and multiply by the height. Divide by 18.
For a pile leaning against an inner corner, divide by 9.
For a freestanding pile, divide by 36.
For beans, 1 hu occupies 2 chi 7 cun of volume.

Answer: the volume is *a* chi³, and it makes *b* hu of beans.
"""

# 下周三丈 (convert zhang to chi: 1 zhang = 10 chi)
下周 = 3 * 10  # chi

# 高七尺
高 = 7  # chi

# 委粟術：其依垣者十八而一
依垣法 = 18

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 其依垣者，十八而一
積依垣 = Fraction(積, 依垣法)

# 程粟一斛積二尺七寸 (convert to chi³: 2 chi 7 cun = 2 + 7/10 chi³)
一斛積 = 2 + Fraction(7, 10)

# 計算為菽
為菽 = Fraction(積依垣, 一斛積)

# 答案
a = 積依垣  # Volume in chi³
b = 為菽  # Amount of beans in hu
"""
Variable 'b' has wrong value. Expected: 35000/243, Actual: 3500/27"""
