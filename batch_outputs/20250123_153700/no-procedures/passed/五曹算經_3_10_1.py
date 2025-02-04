"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
答曰： a領 奇 b人 。
"""

"""
Suppose there is a mat, one mat can seat 23 people. There are 533,680 guests.
Question: how many mats are needed, and how many people will be left without a seat?

Answer: *a* mats and *b* people.
"""

# Number of guests
guests = 533680

# Number of people per mat
people_per_mat = 23

# Calculate the number of mats needed (integer division)
a = guests // people_per_mat

# Calculate the remaining people (modulus)
b = guests % people_per_mat
"""
"""
