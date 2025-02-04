"""
今有醋三升給七兵見有四百五十七斛問給幾何
術曰置醋數再上十之為升以七因之又以三升除之即得
答曰給兵 a人
"""

#----- content starts here -----
"""
Suppose there are 3 sheng of vinegar to supply 7 soldiers. 
It is observed that there are 457 hu of vinegar.
Question: how many soldiers can be supplied?

The procedure says: Place the amount of vinegar, multiply it by 10 to convert it to sheng.
Multiply it by 7 soldiers, then divide by 3 sheng. The result is obtained.

Answer: it supplies *a* soldiers.
"""

# 醋三升
醋升 = 3

# 給七兵
兵 = 7

# 見有四百五十七斛
醋斛 = 457

# 置醋數再上十之為升
醋升總 = 10 * 醋斛

# 以七因之
總兵需求 = 醋升總 * 兵

# 又以三升除之即得
a = Fraction(總兵需求, 醋升)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 319900/3, Actual: 31990/3"""
