"""
今有三女各刺文一方長女七日刺訖中女八日半刺訖小女九日太半刺訖今令三女共刺一方問㡬何日刺訖
術曰置日數以㸦乘方數併為法日數相乘為實實如法而一
答曰 a日
"""

"""
Suppose there are three women, each embroidering one square of fabric.
The eldest finishes in 7 days, the middle one in 8.5 days, and the youngest in 9.5 days.
Now, let the three women embroider one square of fabric together.
Question: how many days will it take to finish?

The procedure says: Place the days [required by each woman].
Multiply them together with the fabric square count, and sum them to obtain the divisor.
Multiply the days by each other to obtain the dividend.
Divide the dividend by the divisor to obtain the number of days.

Answer: *a* days.
"""

from fractions import Fraction

# 長女七日刺訖
長女日數 = 7

# 中女八日半刺訖
中女日數 = Fraction(17, 2)  # 8.5 days as a fraction

# 小女九日太半刺訖
小女日數 = Fraction(19, 2)  # 9.5 days as a fraction

# 置日數以㸦乘方數併為法
法 = (長女日數 * 中女日數) + (長女日數 * 小女日數) + (中女日數 * 小女日數)

# 日數相乘為實
實 = 長女日數 * 中女日數 * 小女日數

# 實如法而一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 3451/1256, Actual: 2261/827"""
