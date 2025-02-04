"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a canal 9 li long, with fish heads spaced 3 cun apart, one after another.
Question: how many fish are there?

Answer: *a* fish.
"""

# Define the length of the canal in li
canal_length_li = 9

# Convert li to chi (1 li = 300 chi)
canal_length_chi = canal_length_li * 300

# Convert chi to cun (1 chi = 10 cun)
canal_length_cun = canal_length_chi * 10

# Spacing between fish heads in cun
spacing_cun = 3

# Calculate the number of fish
a = canal_length_cun // spacing_cun  # Integer division since we can't have partial fish

a  # Output the result#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 54000, Actual: 9000"""
