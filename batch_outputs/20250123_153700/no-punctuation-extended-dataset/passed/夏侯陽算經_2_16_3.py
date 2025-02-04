"""
今有醋三升給七兵見有四百五十七斛問給幾何
術曰置醋數再上十之為升以七因之又以三升除之即得
答曰給兵 a人
"""

"""
Suppose there are 3 sheng of vinegar allocated to 7 soldiers. 
It is observed that there are 457 hu of vinegar in total.
Question: how many soldiers can be supplied?

The procedure says: Place the vinegar amount, multiply it by 10 to convert it to sheng.
Multiply it by 7, then divide it by 3 sheng, obtaining the number of soldiers.

Answer: it supplies *a* soldiers.
"""

# 醋三升
醋每兵 = 3

# 七兵
兵數 = 7

# 四百五十七斛
總醋 = 457

# 置醋數再上十之為升 (convert hu to sheng, 1 hu = 10 dou = 100 sheng)
總醋升 = 總醋 * 100

# 以七因之 (multiply by 7 soldiers)
總醋兵 = 總醋升 * 7

# 又以三升除之 (divide by 3 sheng per soldier)
a = Fraction(總醋兵, 醋每兵)
"""
"""
