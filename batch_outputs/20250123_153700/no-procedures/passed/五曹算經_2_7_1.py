"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
答曰： a人 。
"""

"""
Suppose there is a city with a perimeter of 48 li. It is desired to defend against invaders by placing one soldier every 3 bu.
Question: how many soldiers are needed?

Answer: *a* soldiers.
"""

# 城周四十八里
城周 = 48  # in li

# 1 li = 300 bu
城周_in_bu = 城周 * 300

# 每三步置一兵
每兵步數 = 3

# Calculate the number of soldiers needed
a = Fraction(城周_in_bu, 每兵步數)  # Total soldiers needed
"""
"""
