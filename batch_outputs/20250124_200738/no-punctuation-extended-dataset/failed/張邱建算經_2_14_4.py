"""
今有三女各刺文一方長女七日刺訖中女八日半刺訖小女九日太半刺訖今令三女共刺一方問㡬何日刺訖
術曰置日數以㸦乘方數併為法日數相乘為實實如法而一
答曰 a日
"""

#----- content starts here -----
"""
Suppose there are three women, each embroidering a square pattern. 
The eldest completes it in 7 days, the middle one in 8.5 days, and the youngest in 9.5 days. 
Now, let the three women work together to embroider one square pattern. 
Question: how many days will it take to complete?

The procedure says: Place the number of days [for each woman] and multiply them by the square pattern count. 
Add these together to form the divisor. 
Multiply the days by each other to form the dividend. 
Divide the dividend by the divisor to obtain the result.

Answer: *a* days.
"""

from fractions import Fraction

# 長女七日刺訖
長女日數 = 7

# 中女八日半刺訖
中女日數 = Fraction(17, 2)  # 8.5 days

# 小女九日太半刺訖
小女日數 = Fraction(19, 2)  # 9.5 days

# 置日數以㸦乘方數併為法
法 = (1 / 長女日數) + (1 / 中女日數) + (1 / 小女日數)

# 日數相乘為實
實 = 1

# 實如法而一
a = Fraction(實, 法)

a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
