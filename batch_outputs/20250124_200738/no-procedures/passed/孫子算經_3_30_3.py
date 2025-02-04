"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
答曰： a 。
"""

#----- content starts here -----
"""
Suppose there is a canal 9 li long, with fish heads spaced 3 cun apart, one after another.
Question: how many fish heads are there?

Answer: *a* fish heads.
"""

# Convert li to chi (1 li = 300 bu, 1 bu = 6 chi, so 1 li = 1800 chi)
canal_length_in_chi = 9 * 1800

# Convert spacing of fish heads from cun to chi (1 chi = 10 cun, so 3 cun = 0.3 chi)
spacing_in_chi = Fraction(3, 10)

# Calculate the number of fish heads
a = canal_length_in_chi // spacing_in_chi

a#----- content ends here -----

"""
"""
