"""
今有兵八萬人凡五兵共給醤二升問日給幾何
術曰置兵數以二因之得一十六萬以五兵除之得醤數
答曰日給 a斛
"""

#----- content starts here -----
"""
Suppose there are 80,000 soldiers, and 5 soldiers together are given 2 sheng of sauce.
Question: how much sauce is given daily?

The procedure says: Place the number of soldiers and multiply it by 2, obtaining 160,000.
Divide it by 5 soldiers, obtaining the amount of sauce.

Answer: daily, *a* hu of sauce is given.
"""

# 兵八萬人
兵數 = 80000

# 共給醤二升
醤量 = 2  # 升

# 置兵數以二因之，得一十六萬
總醤量 = 兵數 * 醤量

# 以五兵除之，得醤數
日給醤升 = Fraction(總醤量, 5)

# Convert 升 to 斛 (1 斛 = 10 升)
a = Fraction(日給醤升, 10)  # 日給醤數 in 斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320, Actual: 3200"""
