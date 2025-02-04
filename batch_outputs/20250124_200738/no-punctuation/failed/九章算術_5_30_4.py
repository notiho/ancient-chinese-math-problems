"""
今有委菽依垣下周三丈高七尺問積及為菽各幾何
委粟術曰下周自乘以高乘之三十六而一其依垣者十八而一其依垣內角者九而一程粟一斛積二尺七寸其米一斛積一尺六寸五分寸之一其菽答麻麥一斛皆二尺四寸十分寸之三
荅曰積 a尺 為菽 b斛 
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many dou of beans does it represent?

The procedure for piled grain says: 
For a pile with a full base, multiply the base circumference by itself, then multiply by the height, and divide by 36.
For a pile leaning against a wall, divide by 18.
For a pile leaning against an inner corner, divide by 9.
For beans, 1 hu occupies 2 chi 7 cun of volume.
For rice, 1 hu occupies 1 chi 6 cun 5/10 cun of volume.
For beans, hemp, and wheat, 1 hu occupies 2 chi 4 cun 3/10 cun of volume.

Answer: the volume is *a* chi³, and it represents *b* hu of beans.
"""

# 下周三丈
下周 = 3 * 10  # Convert zhang to chi

# 高七尺
高 = 7

# 其依垣者，十八而一
依垣除數 = 18

# 積 = 下周自乘，以高乘之，十八而一
積 = (下周 * 下周 * 高) / 依垣除數

# 菽一斛積二尺四寸十分寸之三
菽一斛積 = 2 + Fraction(4, 10) + Fraction(3, 100)

# 為菽 = 積 / 菽一斛積
為菽 = 積 / 菽一斛積

a = 積
b = 為菽#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 35000/243, Actual: 144.03292181069958"""
