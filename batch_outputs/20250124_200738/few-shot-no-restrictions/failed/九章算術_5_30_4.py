"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many dou of beans does it contain?

The procedure for piled grain says:
- For a free-standing pile, multiply the base circumference by itself, then multiply by the height, and divide by 36.
- For a pile leaning against a wall, divide by 18.
- For a pile leaning into a corner, divide by 9.

For beans, the volume of 1 dou is 2 chi 4 cun and 3/10 of a cun.

Answer: the volume is *a* chi³, and it contains *b* dou of beans.
"""

from fractions import Fraction

# 下周三丈 (base circumference)
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高七尺 (height)
高 = 7

# 委菽依垣 (pile leaning against a wall)
# 下周自乘，以高乘之，十八而一
積 = (下周 ** 2) * 高 / 18

# 菽一斛，積二尺四寸、十分寸之三 (1 dou of beans = 2 chi 4 cun and 3/10 cun)
# Convert 2 chi 4 cun 3/10 cun to chi³
一斛體積 = 2 + Fraction(4, 10) + Fraction(3, 100)

# Calculate the number of dou of beans
為菽 = 積 / 一斛體積

# Results
a = 積  # Volume in chi³
b = 為菽  # Number of dou of beans

a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 35000/243, Actual: 144.03292181069958"""
