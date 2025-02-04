"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
術曰：置九里以三百步乘之，得二千七百步；又以六尺乘之，得一萬六千二百尺，上十之，得一十六萬二千寸，以魚三寸除之，即得。
答曰： a 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
li_to_bu = 300  # 1 li = 300 bu (步)
bu_to_chi = 6   # 1 bu = 6 chi (尺)
chi_to_cun = 10 # 1 chi = 10 cun (寸)
length_of_channel_in_li = 9  # 9 li
length_of_fish_head_in_cun = 3  # 3 cun

# Step 1: Convert li to bu
length_in_bu = length_of_channel_in_li * li_to_bu

# Step 2: Convert bu to chi
length_in_chi = length_in_bu * bu_to_chi

# Step 3: Convert chi to cun
length_in_cun = length_in_chi * chi_to_cun

# Step 4: Divide by the length of the fish head to find the number of fish
a = Fraction(length_in_cun, length_of_fish_head_in_cun)

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the number of fish as a `Fraction`.
"""


"""
"""
