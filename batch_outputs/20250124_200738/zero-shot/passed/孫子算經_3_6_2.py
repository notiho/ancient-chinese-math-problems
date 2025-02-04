"""
今有丁九萬八千七百六十六，凡二十五丁出一兵。問：兵幾何？
術曰：置丁九萬八千七百六十六為實，以二十五為法。實如法，即得。
答曰： a人 奇 b 丁。
"""

"""
To solve this problem, we need to divide the total number of 丁 (98,766) by 25 to determine how many full 兵 can be formed, and the remainder will be the leftover 丁. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_ding = 98766  # Total 丁
conversion_rate = 25  # 25 丁 form 1 兵

# Calculate the number of 兵 and the leftover 丁
a = total_ding // conversion_rate  # Full 兵
b = total_ding % conversion_rate  # Remaining 丁

# Results
# a represents the number of 兵
# b represents the leftover 丁
#----- content ends here -----


"""


After running this code:
- `a` will hold the number of 兵.
- `b` will hold the leftover 丁.
"""


"""
"""
