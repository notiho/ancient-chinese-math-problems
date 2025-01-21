"""
今有醋三升給七兵見有四百五十七斛問給幾何
術曰置醋數再上十之為升以七因之又以三升除之即得
答曰給兵 a人
"""

"""
Suppose there are 3 sheng of vinegar allocated to 7 soldiers. 
It is observed that there are 457 hu of vinegar in total.
Question: how many soldiers can be supplied?

The procedure says: Place the vinegar amount, multiply it by 10 to convert it into sheng.
Multiply it by 7, then divide by 3 sheng to obtain the result.

Answer: it supplies *a* soldiers.
"""

# 醋三升
醋每兵 = 3

# 給七兵
兵 = 7

# 見有四百五十七斛
總醋 = 457

# 置醋數再上十之為升
總醋升 = 總醋 * 10

# 以七因之
總醋兵 = 總醋升 * 7

# 又以三升除之即得
a = Fraction(總醋兵, 醋每兵)
"""
Variable 'a' has wrong value. Expected: 319900/3, Actual: 31990/3"""
