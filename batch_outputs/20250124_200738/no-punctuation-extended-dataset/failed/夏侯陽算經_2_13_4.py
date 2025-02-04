"""
今有兵八萬人凡五兵共給醤二升問日給幾何
術曰置兵數以二因之得一十六萬以五兵除之得醤數
答曰日給 a斛
"""

#----- content starts here -----
"""
Suppose there are 80,000 soldiers, and there are 5 groups of soldiers sharing 2 sheng of sauce.
Question: how much sauce is given daily?

The procedure says: Place the number of soldiers and multiply it by 2, obtaining 160,000.
Divide it by the 5 groups of soldiers, obtaining the amount of sauce.

Answer: daily, *a* hu of sauce is given.
"""

# 兵八萬人
兵數 = 80000

# 醤二升
醤 = 2  # in sheng

# 以二因之
醤數 = 2 * 兵數

# 得一十六萬
醤數 = 160000  # already calculated above

# 以五兵除之
醤數_per_group = Fraction(醤數, 5)

# Convert sheng to hu (10 sheng = 1 hu)
a = Fraction(醤數_per_group, 10)  # Convert to hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320, Actual: 3200"""
