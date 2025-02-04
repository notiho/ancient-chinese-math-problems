"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
術曰：列五十三萬三千六百八十人，以二十三人除之即得。
答曰： a領 奇 b人 。
"""

#----- content starts here -----
"""
Suppose there is one mat (席) that can seat 23 people. There are 533,680 guests.
Question: how many mats are needed?

The procedure says: Arrange the 533,680 guests and divide by 23 people per mat. The quotient is the number of full mats, and the remainder is the number of extra people.

Answer: *a* mats and *b* extra people.
"""

# Total number of guests
總客數 = 533680

# Number of people per mat
每席人數 = 23

# Divide to find the number of full mats and the remainder
a = 總客數 // 每席人數  # Full mats
b = 總客數 % 每席人數  # Remaining people

# Output: a mats and b extra people
a, b#----- content ends here -----

"""
"""
