"""
今有鹿直西走馬獵追之未及三十六步鹿囘直北走馬俱斜逐之走五十步未及一十步斜直射之得鹿若鹿不迴馬獵追之問幾何里而及之
術曰置斜逐步數以射步數增之自相乘以追之未及步數自相乘減之餘以開方除之所得以減斜逐步數餘為法以斜逐步數乘未及步數為實實如法而一
答曰 a里
"""

"""
Suppose a deer runs straight west, and a horseman hunts it, chasing after it but not catching it within 36 bu. 
The deer then turns and runs straight north, while the horseman chases it diagonally for 50 bu, still not catching it, being 10 bu short.
The horseman shoots diagonally and catches the deer.
If the deer had not turned north and the horseman continued chasing it west, how many li would it take for the horseman to catch the deer?

The procedure says: Place the diagonal chase distance and add the shooting distance to it. Square this sum.
Subtract the square of the distance by which the horseman was short of catching the deer.
Take the square root of the remainder and divide it by the diagonal chase distance.
Subtract this result from the diagonal chase distance. The remainder is the divisor.
Multiply the diagonal chase distance by the distance by which the horseman was short of catching the deer. This is the dividend.
Divide the dividend by the divisor to obtain the result.

The answer says: *a* li.
"""

from fractions import Fraction
import math

# 斜逐步數
斜逐步數 = 50

# 射步數
射步數 = 10

# 追之未及步數
未及步數 = 36

# 置斜逐步數以射步數增之，自相乘
增之 = 斜逐步數 + 射步數
增之平方 = 增之 ** 2

# 以追之未及步數自相乘減之
未及平方 = 未及步數 ** 2
餘 = 增之平方 - 未及平方

# 餘以開方除之
開方 = math.sqrt(餘)

# 所得以減斜逐步數，餘為法
法 = 斜逐步數 - 開方

# 以斜逐步數乘未及步數，為實
實 = 斜逐步數 * 未及步數

# 實如法而一
a = Fraction(實, 法) / 300  # Convert bu to li (1 li = 300 bu)
"""
Code error: both arguments should be Rational instances"""
