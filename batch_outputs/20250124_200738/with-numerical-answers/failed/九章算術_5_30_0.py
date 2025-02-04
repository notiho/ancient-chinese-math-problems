"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a(=350)尺 。為菽 b(=35000/243)斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many dou of beans does it contain?

The procedure for piled grains says: Multiply the base circumference by itself, then multiply by the height, and divide by 36.
For those leaning against a wall, divide by 18.
For those leaning against an inner corner, divide by 9.
For millet, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun of volume.
For beans, broad beans, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a*(=350) chi³, and it contains *b*(=35000/243) hu of beans.
"""

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi

# 高七尺
高 = 7

# 下周自乘
下周積 = 下周 * 下周

# 以高乘之
體積 = 下周積 * 高

# 其依垣者，十八而一
積 = Fraction(體積, 18)  # Volume leaning against a wall

# 程粟一斛，積二尺七寸
# 其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三
一斛體積 = Fraction(24, 10) + 2  # 2 chi 4 cun and 3/10 cun = 2.4 + 0.3 = 2.43 chi³

# 積及為菽各幾何
a = 積  # 350 chi³
b = Fraction(積, 一斛體積)  # 35000/243 hu#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 35000/243, Actual: 875/11"""
