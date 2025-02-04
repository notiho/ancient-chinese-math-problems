"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
答曰： a 。
"""

"""
Suppose there is a canal 9 li long, with fish heads spaced 3 cun apart, one after another.
Question: how many fish heads are there?

Answer: *a* fish heads.
"""

# Define the length of the canal in li
canal_length_li = 9

# Convert li to chi (1 li = 300 chi)
canal_length_chi = canal_length_li * 300

# Convert chi to cun (1 chi = 10 cun)
canal_length_cun = canal_length_chi * 10

# Fish heads are spaced 3 cun apart
spacing_cun = 3

# Calculate the number of fish heads
a = canal_length_cun // spacing_cun

a
"""
Variable 'a' has wrong value. Expected: 54000, Actual: 9000"""
