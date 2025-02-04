"""
今有鹿直西走馬獵追之未及三十六步鹿囘直北走馬俱斜逐之走五十步未及一十步斜直射之得鹿若鹿不迴馬獵追之問幾何里而及之
術曰置斜逐步數以射步數增之自相乘以追之未及步數自相乘減之餘以開方除之所得以減斜逐步數餘為法以斜逐步數乘未及步數為實實如法而一
答曰 a里
"""

#----- content starts here -----
"""
Suppose a deer runs straight west, and a horse hunter chases it but does not catch it within 36 bu. 
The deer then turns and runs straight north, while the horse chases it diagonally for 50 bu but still does not catch it, being 10 bu away. 
The horse then shoots diagonally and catches the deer. 
If the deer had not turned, how many li would the horse have chased it before catching it?

The procedure says: Place the number of diagonal chasing steps and add the number of shooting steps. 
Square the sum, then subtract the square of the steps the horse was short of catching the deer. 
Take the square root of the remainder and divide it by the square root of the diagonal chasing steps. 
Subtract the result from the diagonal chasing steps. 
The remainder is the divisor. 
Multiply the diagonal chasing steps by the steps the horse was short of catching the deer to get the dividend. 
Divide the dividend by the divisor to get the result.

Answer: *a* li.
"""

from fractions import Fraction
import math

# 斜逐步數
斜逐步數 = 50

# 射步數
射步數 = 10

# 追之未及步數
未及步數 = 36

# 置斜逐步數，以射步數增之，自相乘
增步數 = 斜逐步數 + 射步數
增步數平方 = 增步數 ** 2

# 以追之未及步數自相乘減之
未及步數平方 = 未及步數 ** 2
餘 = 增步數平方 - 未及步數平方

# 餘以開方除之所得
開方結果 = math.sqrt(餘)

# 以減斜逐步數，餘為法
法 = 斜逐步數 - 開方結果

# 以斜逐步數乘未及步數為實
實 = 斜逐步數 * 未及步數

# 實如法而一
a = Fraction(實, 法) / 300  # Convert to li (1 li = 300 bu)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
