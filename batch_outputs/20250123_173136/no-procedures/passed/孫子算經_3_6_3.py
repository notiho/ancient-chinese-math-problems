"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
答曰： a人 奇 b 丁。
"""

"""
Suppose there are 98,766 dings (丁, adult males). For every 25 dings, one soldier (兵) is conscripted.
Question: how many soldiers are there, and how many dings are left over?

Answer: *a* soldiers and *b* dings remaining.
"""

# Total number of dings
total_dings = 98766

# Number of dings required for one soldier
dings_per_soldier = 25

# Calculate the number of soldiers (a) and the remainder dings (b)
a = total_dings // dings_per_soldier  # Integer division to find the number of soldiers
b = total_dings % dings_per_soldier   # Remainder to find leftover dings

a, b  # Output the results
"""
"""
