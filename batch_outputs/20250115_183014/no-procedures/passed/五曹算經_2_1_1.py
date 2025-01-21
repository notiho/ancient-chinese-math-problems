"""
今有丁八千九百五十八人，凡三丁出一兵。問：出兵㡬何？
答曰： a人 。
"""

"""
Suppose there are 8,958 adult males (丁). For every 3 males, 1 soldier is conscripted.
Question: how many soldiers are conscripted?

Answer: *a* soldiers.
"""

# Total number of males
丁 = 8958

# Number of males required to conscript 1 soldier
每兵所需丁 = 3

# Calculate the number of soldiers
a = 丁 // 每兵所需丁  # Use integer division since soldiers must be whole numbers

# Output the result
a
"""
"""
