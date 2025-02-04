"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against an inner corner of a wall. 
The base circumference is 8 chi, and the height is 5 chi.
Question: what is the volume of the pile, and how many hu of rice does it make?

The procedure for piled grain says:
- Square the base circumference, multiply by the height, and divide by 36 for a free-standing pile.
- For a pile leaning against a wall, divide by 18.
- For a pile leaning against an inner corner, divide by 9.

Additionally:
- For rice, 1 hu occupies 1 chi 6 cun and 1/5 cun of volume.
- For millet, beans, hemp, and wheat, 1 hu occupies 2 chi 4 cun and 3/10 cun of volume.

Answer: the volume is *a* chi³. It makes *b* hu and *c* hu of rice.
"""

from fractions import Fraction

# 下周八尺
下周 = 8  # chi

# 高五尺
高 = 5  # chi

# 積計算：其依垣內角者，九而一
積 = (下周**2 * 高) / 9  # chi³

# 米一斛，積一尺六寸、五分寸之一
米一斛體積 = 1 + Fraction(6, 10) + Fraction(1, 50)  # chi³

# 計算為米幾斛
米總斛 = 積 / 米一斛體積

# 分離整斛和餘數
整斛 = int(米總斛)
餘斛 = 米總斛 - 整斛

# 答案
a = 積  # 總體積
b = 整斛  # 整斛數
c = 餘斛  # 餘斛數

# Print results
a, b, c#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320/9, Actual: 35.55555555555556
Variable 'c' has wrong value. Expected: 691/729, Actual: 0.9478737997256523"""
