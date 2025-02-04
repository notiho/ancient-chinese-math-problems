"""
今有城周四十八里，欲令禦賊，每三步置一兵。問：用兵㡬何？
答曰： a人 。
"""

"""
Suppose there is a city with a circumference of 48 li. It is desired to defend against invaders by placing one soldier every 3 bu.
Question: how many soldiers are needed?

Answer: *a* soldiers.
"""

# 城周四十八里 (1 里 = 300 步)
城周 = 48 * 300  # Convert li to bu

# 每三步置一兵
每兵步數 = 3

# Calculate the number of soldiers needed
a = 城周 // 每兵步數  # Use integer division since the number of soldiers must be whole

a
"""
"""
