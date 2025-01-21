"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
答曰： a人 奇 b 丁。
"""

"""
Suppose there are 98,766 dings (adult males). For every 25 dings, one soldier is conscripted.
Question: how many soldiers are there, and how many dings are left over?

Answer: *a* soldiers, with *b* dings left over.
"""

# Total dings
total_dings = 98766

# Number of dings required for one soldier
dings_per_soldier = 25

# Calculate the number of soldiers
a = total_dings // dings_per_soldier

# Calculate the leftover dings
b = total_dings % dings_per_soldier

# Results
a, b
"""
"""
