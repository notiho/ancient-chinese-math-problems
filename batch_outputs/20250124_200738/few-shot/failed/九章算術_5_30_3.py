"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many dou of beans does it contain?

The procedure for piled grains says: The base circumference is squared, then multiplied by the height. Divide by 36 for a full pile. 
If leaning against a wall, divide by 18. 
If leaning against an inner corner, divide by 9.

For measuring grains: 1 hu of millet occupies 2 chi 7 cun. 
1 hu of rice occupies 1 chi 6 cun and 1/5 cun. 
1 hu of beans, peas, hemp, or wheat occupies 2 chi 4 cun and 3/10 cun.

Answer: The volume is *a* chi³. It contains *b* hu of beans.
"""

from fractions import Fraction

# 下周三丈 (convert zhang to chi: 1 zhang = 10 chi)
下周 = 3 * 10  # chi

# 高七尺
高 = 7  # chi

# 委菽依垣 (leaning against a wall, divide by 18)
# 下周自乘，以高乘之，十八而一
積 = (下周 ** 2) * 高 / 18

# 菽一斛，積二尺四寸、十分寸之三 (convert to chi³: 1 hu = 2 chi 4 cun + 3/10 cun = 2.4 + 0.3 = 2.43 chi³)
菽一斛積 = Fraction(243, 100)  # chi³

# 計算為菽
為菽 = 積 / 菽一斛積

# 答案
a = 積  # Volume in chi³
b = 為菽  # Amount of beans in hu#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 35000/243, Actual: 144.03292181069958"""
