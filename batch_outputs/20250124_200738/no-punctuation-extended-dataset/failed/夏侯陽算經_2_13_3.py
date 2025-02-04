"""
今有兵八萬人凡五兵共給醤二升問日給幾何
術曰置兵數以二因之得一十六萬以五兵除之得醤數
答曰日給 a斛
"""

#----- content starts here -----
"""
Suppose there are 80,000 soldiers, and there are 5 units of soldiers in total.
They are collectively given 2 sheng of sauce.
Question: how much sauce is given per day?

The procedure says: Place the number of soldiers and multiply it by 2, obtaining 160,000.
Divide it by the 5 units of soldiers, obtaining the amount of sauce.

Answer: *a* hu (1 hu = 10 sheng).
"""

# 兵八萬人
兵數 = 80000

# 共給醬二升
醬 = 2

# 置兵數以二因之
總醬 = 兵數 * 醬

# 得一十六萬
assert 總醬 == 160000  # Verification step

# 以五兵除之
日給醬 = Fraction(總醬, 5)

# Convert to hu (1 hu = 10 sheng)
a = Fraction(日給醬, 10)  # Convert sheng to hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 320, Actual: 3200"""
