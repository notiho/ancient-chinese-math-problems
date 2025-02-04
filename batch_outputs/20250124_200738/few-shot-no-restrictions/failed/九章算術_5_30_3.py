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
- Square the base circumference, then multiply by the height, and divide by 36.
- If it leans against a wall, divide by 18.
- If it leans against an inner corner, divide by 9.

For the conversion:
- 1 dou of millet occupies 2 chi 7 cun of volume.
- 1 dou of rice occupies 1 chi 6 cun and 1/5 cun of volume.
- 1 dou of beans, da (a type of grain), hemp, or wheat occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a* chi³, and it contains *b* dou of beans.
"""

from fractions import Fraction

# 下周三丈 (base circumference is 3 zhang)
下周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高七尺 (height is 7 chi)
高 = 7

# 委粟術曰：下周自乘，以高乘之，三十六而一
積 = (下周 ** 2) * 高 / 36

# 其依垣者，十八而一
積依垣 = 積 / 18

# 其菽一斛，積二尺四寸、十分寸之三 (1 dou of beans occupies 2 chi 4 cun and 3/10 cun)
豆體積 = 2 + Fraction(4, 10) + Fraction(3, 100)  # Convert 2 chi 4 cun 3/10 cun to chi³

# 計算為菽 (calculate the number of dou of beans)
為菽 = 積依垣 / 豆體積

# Final results
a = 積依垣  # Volume in chi³
b = 為菽  # Number of dou of beans

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 350, Actual: 9.722222222222221
Variable 'b' has wrong value. Expected: 35000/243, Actual: 4.000914494741655"""
