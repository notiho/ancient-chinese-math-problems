"""
今有三女各刺文一方長女七日刺訖中女八日半刺訖小女九日太半刺訖今令三女共刺一方問㡬何日刺訖
術曰置日數以㸦乘方數併為法日數相乘為實實如法而一
答曰 a日
"""

"""
Suppose there are three women, each embroidering one square. 
The eldest finishes in 7 days, the middle one in 8.5 days, and the youngest in 9.5 days. 
Now let the three women work together to embroider one square.
Question: how many days will it take to finish?

The procedure says: Place the days for each woman. 
Multiply the total square (1 square) by the days for each woman, and sum them to form the divisor.
Multiply the days for each woman with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

# 長女七日刺訖
長女日數 = 7

# 中女八日半刺訖
中女日數 = 8 + Fraction(1, 2)

# 小女九日太半刺訖
小女日數 = 9 + Fraction(1, 2)

# 置日數以㸦乘方數併為法
法 = (1 * 長女日數) + (1 * 中女日數) + (1 * 小女日數)

# 日數相乘為實
實 = 長女日數 * 中女日數 * 小女日數

# 實如法而一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 3451/1256, Actual: 2261/100"""
