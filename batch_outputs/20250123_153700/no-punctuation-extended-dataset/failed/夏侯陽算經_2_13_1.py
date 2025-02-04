"""
今有兵八萬人凡五兵共給醤二升問日給幾何
術曰置兵數以二因之得一十六萬以五兵除之得醤數
答曰日給 a斛
"""

"""
Suppose there are 80,000 soldiers, and there are 5 groups of soldiers sharing 2 sheng of sauce.
Question: how much sauce is given per day?

The procedure says: Place the number of soldiers and multiply it by 2, obtaining 160,000.
Divide it by the 5 groups of soldiers, obtaining the amount of sauce.

Answer: the daily amount is *a* hu.
"""

# 兵八萬人
兵數 = 80000

# 共給醤二升
醤升 = 2

# 升 to 斛 conversion (1 斛 = 10 升)
醤斛 = Fraction(醤升, 10)

# 置兵數，以二因之，得一十六萬
實 = 兵數 * 2

# 以五兵除之，得醤數
a = Fraction(實, 5) * 醤斛

"""
Variable 'a' has wrong value. Expected: 320, Actual: 6400"""
