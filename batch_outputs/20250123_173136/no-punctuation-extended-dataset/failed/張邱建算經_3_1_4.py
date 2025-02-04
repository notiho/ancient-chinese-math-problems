"""
今有鹿直西走馬獵追之未及三十六步鹿囘直北走馬俱斜逐之走五十步未及一十步斜直射之得鹿若鹿不迴馬獵追之問幾何里而及之
術曰置斜逐步數以射步數增之自相乘以追之未及步數自相乘減之餘以開方除之所得以減斜逐步數餘為法以斜逐步數乘未及步數為實實如法而一
答曰 a里
"""

"""
Suppose a deer runs straight west, and a horseman hunts and chases it but does not catch up within 36 bu. 
The deer then turns and runs straight north, and the horseman chases it diagonally for 50 bu but still does not catch up by 10 bu. 
The horseman shoots diagonally and catches the deer.
If the deer had not turned, how many li would the horseman need to chase it to catch up?

The procedure says: Place the diagonal chasing steps and add the shooting steps to them. Square the result. 
Subtract the square of the steps by which the horseman did not catch up. 
Take the square root of the remainder and divide it by the diagonal chasing steps. Subtract this from the diagonal chasing steps. 
The remainder is the divisor. Multiply the diagonal chasing steps by the steps by which the horseman did not catch up to get the dividend. 
Divide the dividend by the divisor to get the result.

Answer: *a* li.
"""

from fractions import Fraction
from math import sqrt

# 斜逐步數
斜逐步數 = 50

# 射步數
射步數 = 10

# 追之未及步數
未及步數 = 36

# 置斜逐步數，以射步數增之，自相乘
增後步數平方 = (斜逐步數 + 射步數) ** 2

# 以追之未及步數自相乘減之
減後平方 = 增後步數平方 - 未及步數 ** 2

# 餘以開方除之
開方結果 = sqrt(減後平方)

# 所得以減斜逐步數，餘為法
法 = 斜逐步數 - 開方結果

# 以斜逐步數乘未及步數，為實
實 = 斜逐步數 * 未及步數

# 實如法而一
a = Fraction(實, 法) / 300  # Convert to li (1 li = 300 bu)
"""
Code error: both arguments should be Rational instances"""
