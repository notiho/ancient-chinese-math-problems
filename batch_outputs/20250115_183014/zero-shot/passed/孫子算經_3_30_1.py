"""
今有九里渠，三寸魚頭，頭相次。問：魚得幾何？
術曰：置九里以三百步乘之，得二千七百步；又以六尺乘之，得一萬六千二百尺，上十之，得一十六萬二千寸，以魚三寸除之，即得。
答曰： a 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
li_to_bu = 300  # 1 li = 300 bu
bu_to_chi = 6   # 1 bu = 6 chi
chi_to_cun = 10 # 1 chi = 10 cun
fish_head_length = 3  # fish head length in cun

# Step 1: Convert 9 li to bu
total_bu = 9 * li_to_bu

# Step 2: Convert bu to chi
total_chi = total_bu * bu_to_chi

# Step 3: Convert chi to cun
total_cun = total_chi * chi_to_cun

# Step 4: Divide total cun by fish head length
a = Fraction(total_cun, fish_head_length)

# Result
a


"""


The variable `a` will contain the number of fish heads.
"""


"""
"""
