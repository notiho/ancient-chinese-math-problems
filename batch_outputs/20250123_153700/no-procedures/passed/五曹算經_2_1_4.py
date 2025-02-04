"""
今有丁八千九百五十八人，凡三丁出一兵。問：出兵㡬何？
答曰： a人 。
"""

"""
Suppose there are 8,958 adult males (丁), and for every 3 males, 1 soldier is drafted.
Question: how many soldiers are drafted?

Answer: *a* soldiers.
"""

# Total number of males
丁 = 8958

# Number of males required to draft 1 soldier
每兵需丁 = 3

# Calculate the number of soldiers drafted
a = 丁 // 每兵需丁  # Use integer division since the number of soldiers must be a whole number

# Output
a
"""
"""
