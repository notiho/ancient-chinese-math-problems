"""
今有席，一領坐客二十三人，有客五十三萬三千六百八十人。問：席㡬何？
答曰： a領 奇 b人 。
"""

"""
Suppose there is a mat, and one mat can seat 23 people. There are 533,680 guests.
Question: how many mats are needed, and how many people will remain without a mat?

Answer: *a* mats and *b* people.
"""

# One mat can seat 23 people
mat_capacity = 23

# Total number of guests
total_guests = 533680

# Calculate the number of full mats needed
a = total_guests // mat_capacity

# Calculate the remaining people without a mat
b = total_guests % mat_capacity

a, b
"""
"""
