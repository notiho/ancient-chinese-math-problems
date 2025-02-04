"""
今有委米依垣內角，下周八尺，高五尺。問︰積及為米幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為米 b斛 ， c斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of rice leaning against the inner corner of a wall. The base perimeter is 8 chi, and the height is 5 chi.
Question: What is the volume of the pile, and how many dou of rice does it make?

The procedure for piled grain says:
- Square the base perimeter, multiply it by the height, and divide by 36 for a full pile.
- For a pile leaning against a wall, divide by 18.
- For a pile leaning against the inner corner of a wall, divide by 9.

For rice:
- 1 hu of rice occupies a volume of 1 chi 6 cun and 1/5 cun (or 1.65 chi³).

For other grains (millet, beans, hemp, wheat):
- 1 hu occupies a volume of 2 chi 4 cun and 3/10 cun (or 2.43 chi³).

Answer: The volume is *a* chi³. It makes *b* hu of rice and *c* hu of other grains.
"""

from fractions import Fraction

# Given dimensions
下周 = 8  # chi
高 = 5  # chi

# Procedure for volume
# 下周自乘，以高乘之
積 = 下周**2 * 高

# 依垣內角者，九而一
積 = Fraction(積, 9)

# Volume in chi³
a = 積

# Rice conversion
# 1 hu of rice = 1 chi 6 cun and 1/5 cun = 1.65 chi³
米每斛積 = Fraction(165, 100)  # 1.65 chi³
b = 積 // 米每斛積  # Full hu of rice
剩餘積 = 積 % 米每斛積  # Remaining volume

# Other grains conversion
# 1 hu of other grains = 2 chi 4 cun and 3/10 cun = 2.43 chi³
其他每斛積 = Fraction(243, 100)  # 2.43 chi³
c = 剩餘積 // 其他每斛積  # Full hu of other grains

# Final results
print(f"積: {a} chi³")
print(f"為米: {b} hu (rice), {c} hu (other grains)")
#----- content ends here -----

"""
Variable 'c' has wrong value. Expected: 691/729, Actual: 0"""
