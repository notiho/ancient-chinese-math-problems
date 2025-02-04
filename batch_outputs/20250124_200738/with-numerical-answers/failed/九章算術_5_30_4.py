"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a(=350)尺 。為菽 b(=35000/243)斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many dou of beans does it contain?

The procedure for piled grain says: Multiply the base circumference by itself, then multiply by the height, and divide by 36.
For those leaning against a wall, divide by 18.
For those leaning into a corner, divide by 9.
For beans, one dou occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a*(=350) chi³, and it contains *b*(=35000/243) dou of beans.
"""

from fractions import Fraction

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高七尺
高 = 7

# 下周自乘
下周平方 = 下周 * 下周

# 以高乘之
積 = 下周平方 * 高

# 三十六而一
積 = Fraction(積, 36)

# 其依垣者，十八而一
積 = Fraction(積, 2)  # Dividing by 18 is equivalent to dividing by 2 after dividing by 36

# 程粟一斛，積二尺七寸
# 其菽一斛，皆二尺四寸、十分寸之三
菽一斛積 = 2 + Fraction(4, 10) + Fraction(3, 100)  # Convert 2 chi 4 cun 3/10 cun to chi³

# 為菽
b = Fraction(積, 菽一斛積)  # Number of dou of beans

# Final results
a = 積  # Volume in chi³
b = b  # Number of dou of beans#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 350, Actual: 175/2
Variable 'b' has wrong value. Expected: 35000/243, Actual: 8750/243"""
