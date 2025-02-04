"""
今有兵八萬人凡五兵共給醤二升問日給幾何
術曰置兵數以二因之得一十六萬以五兵除之得醤數
答曰日給 a斛
"""

#----- content starts here -----
"""
Suppose there are 80,000 soldiers, and in total, 5 soldiers are given 2 sheng of sauce.
Question: how much sauce is given per day?

The procedure says: Place the number of soldiers, multiply it by 2, obtaining 160,000.
Divide it by 5 soldiers, obtaining the amount of sauce.

Answer: the daily amount is *a* hu.
"""

# 兵八萬人
兵數 = 80000

# 醤二升
醤 = 2  # in sheng

# 置兵數以二因之
實 = 兵數 * 醤

# 得一十六萬
實 = 160000  # Confirmed from the procedure

# 以五兵除之
醤數 = Fraction(實, 5)

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(醤數, 10)  # Convert to hu

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320, Actual: 3200"""
