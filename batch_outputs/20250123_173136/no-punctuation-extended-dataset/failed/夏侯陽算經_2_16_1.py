"""
今有醋三升給七兵見有四百五十七斛問給幾何
術曰置醋數再上十之為升以七因之又以三升除之即得
答曰給兵 a人
"""

"""
Suppose there are 3 sheng of vinegar to supply 7 soldiers. 
It is observed that there are 457 hu of vinegar.
Question: how many soldiers can be supplied?

The procedure says: Place the vinegar amount, multiply it by 10 to convert to sheng.
Multiply it by 7, then divide by 3 sheng. This gives the result.

Answer: it supplies *a* soldiers.
"""

# 醋三升
醋升 = 3

# 給七兵
兵數 = 7

# 見有四百五十七斛
醋斛 = 457

# 置醋數再上十之為升
醋升總數 = 10 * 醋斛

# 以七因之
供應總數 = 醋升總數 * 兵數

# 又以三升除之即得
a = Fraction(供應總數, 醋升)
"""
Variable 'a' has wrong value. Expected: 319900/3, Actual: 31990/3"""
