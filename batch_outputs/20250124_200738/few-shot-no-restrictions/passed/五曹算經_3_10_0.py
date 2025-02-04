"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

#----- content starts here -----
"""
Suppose there is one mat, which can seat 23 people. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange 533,680 people, divide by 23 people, and the result is obtained.

Answer: *a* mats and *b* remaining people.
"""

from fractions import Fraction

# Total guests
總客人數 = 533680

# Number of people per mat
每席人數 = 23

# Calculate the number of full mats
a = 總客人數 // 每席人數

# Calculate the remaining people
b = 總客人數 % 每席人數

# Output the results
a, b#----- content ends here -----

"""
"""
