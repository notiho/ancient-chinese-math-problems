"""
今有鹿直西走馬獵追之未及三十六步鹿囘直北走馬俱斜逐之走五十步未及一十步斜直射之得鹿若鹿不迴馬獵追之問幾何里而及之
術曰置斜逐步數以射步數增之自相乘以追之未及步數自相乘減之餘以開方除之所得以減斜逐步數餘為法以斜逐步數乘未及步數為實實如法而一
答曰 a里
"""

#----- content starts here -----
"""
Suppose a deer runs straight west, and a horseman hunts it, chasing it but not catching it after 36 bu. 
The deer then turns and runs straight north, while the horseman chases it diagonally for 50 bu, still 10 bu short of catching it. 
The horseman then shoots the deer diagonally and catches it. 
If the deer had not turned, and the horseman continued chasing it straight west, how many li would it take for the horseman to catch the deer?

The procedure says: Place the number of diagonal chasing steps. Add the number of shooting steps to it. Multiply the sum by itself. 
Subtract the square of the number of steps by which the horseman had not caught the deer. 
Take the square root of the remainder and divide it by the diagonal chasing steps. Subtract the result from the diagonal chasing steps. 
The remainder becomes the divisor. Multiply the diagonal chasing steps by the number of steps by which the horseman had not caught the deer. 
This becomes the dividend. Divide the dividend by the divisor to find the result.

Answer: *a* li.
"""

from fractions import Fraction
from math import sqrt

# 鹿直西走，馬追未及三十六步
未及步數 = 36

# 鹿囘直北走，馬斜逐五十步，未及一十步
斜逐步數 = 50
射步數 = 10

# 置斜逐步數，以射步數增之，自相乘
增步數 = 斜逐步數 + 射步數
增步平方 = 增步數 * 增步數

# 以追之未及步數自相乘減之
未及平方 = 未及步數 * 未及步數
餘數 = 增步平方 - 未及平方

# 餘以開方除之
開方結果 = sqrt(Fraction(餘數))

# 所得以減斜逐步數，餘為法
法 = Fraction(斜逐步數) - Fraction(開方結果)

# 以斜逐步數乘未及步數，為實
實 = Fraction(斜逐步數) * Fraction(未及步數)

# 實如法而一
a = Fraction(實, 法) / 300  # Convert bu to li (1 li = 300 bu)#----- content ends here -----

"""
"""
