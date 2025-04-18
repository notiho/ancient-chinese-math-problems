"""
今有絹一疋買紫草三十斤染絹二丈五尺今有絹七疋欲減買紫草還自染餘絹問減絹買紫草各㡬何
術曰置今有絹疋數以本絹一疋尺數乗之為減絹實以紫草三十斤乗之為買紫草實以本絹尺數併染尺為法實如法得一其一術盈不足術為之亦得
答曰減絹 a疋 買草 b斤
"""

"""
Suppose there is 1 bolt of silk, which is used to buy 30 jin of purple grass to dye 2 zhang and 5 chi of silk.
Now there are 7 bolts of silk, and it is desired to reduce the amount of silk used to buy purple grass and instead use the remaining silk for dyeing.
Question: how much silk is reduced, and how much purple grass is bought?

The procedure says: Place the current number of bolts of silk.
Multiply it by the length of silk (in chi) per bolt to obtain the "reduced silk" dividend.
Multiply it by 30 jin of purple grass to obtain the "bought purple grass" dividend.
Add the length of silk per bolt and the dyed length of silk to obtain the divisor.
Divide the dividends by the divisor to obtain the results.
If there is excess or deficiency, the method of surplus and deficiency can also be used.

Answer: *a* bolts of silk are reduced, and *b* jin of purple grass are bought.
"""

# 絹一疋買紫草三十斤染絹二丈五尺
本絹疋數 = 1
紫草斤數 = 30
染絹尺數 = 2 * 10 + 5  # Convert 2 zhang 5 chi to chi

# 今有絹七疋
今絹疋數 = 7

# 置今有絹疋數，以本絹一疋尺數乘之，為減絹實
減絹實 = 今絹疋數 * 本絹疋數

# 以紫草三十斤乘之，為買紫草實
買紫草實 = 今絹疋數 * 紫草斤數

# 以本絹尺數併染尺為法
法 = 本絹疋數 + 染絹尺數

# 實如法得一
a = Fraction(減絹實, 法)
b = Fraction(買紫草實, 法)
"""
Variable 'a' has wrong value. Expected: 56/13, Actual: 7/26
Variable 'b' has wrong value. Expected: 1680/13, Actual: 105/13"""
