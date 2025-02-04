"""
今有鹿直西走馬獵追之未及三十六步鹿囘直北走馬俱斜逐之走五十步未及一十步斜直射之得鹿若鹿不迴馬獵追之問幾何里而及之
術曰置斜逐步數以射步數增之自相乘以追之未及步數自相乘減之餘以開方除之所得以減斜逐步數餘為法以斜逐步數乘未及步數為實實如法而一
答曰 a里
"""

#----- content starts here -----
"""
Suppose a deer runs straight west, and a horse hunter chases it but does not catch it after 36 bu. 
The deer then turns and runs straight north, while the horse chases it diagonally for 50 bu, still 10 bu short of catching it.
The horse shoots the deer diagonally and catches it.
If the deer had not turned and the horse continued chasing it, how many li would the horse need to run to catch the deer?

The procedure says: Place the diagonal chase steps (斜逐步數) and add the shooting steps (射步數) to it. 
Square the result. Subtract the square of the steps the horse was short of catching (未及步數).
Take the square root of the remainder and divide it by the diagonal chase steps (斜逐步數). 
Subtract this result from the diagonal chase steps (斜逐步數). 
The remainder becomes the divisor (法). 
Multiply the diagonal chase steps (斜逐步數) by the steps the horse was short of catching (未及步數) to get the dividend (實). 
Divide the dividend by the divisor to get the result.

Answer: *a* li.
"""

from fractions import Fraction
import math

# 斜逐步數 (diagonal chase steps)
斜逐步數 = 50

# 射步數 (shooting steps)
射步數 = 10

# 未及步數 (steps short of catching)
未及步數 = 36

# 置斜逐步數以射步數增之，自相乘
增後平方 = (斜逐步數 + 射步數) ** 2

# 以追之未及步數自相乘減之
減後平方 = 增後平方 - 未及步數 ** 2

# 餘以開方除之
開方結果 = math.sqrt(減後平方)

# 所得以減斜逐步數，餘為法
法 = 斜逐步數 - 開方結果

# 以斜逐步數乘未及步數為實
實 = 斜逐步數 * 未及步數

# 實如法而一
a = Fraction(實, 法) / 300  # Convert to li (1 li = 300 bu)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
