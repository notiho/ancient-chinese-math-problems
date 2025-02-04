"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

"""
To solve this problem, we need to calculate the interest rate per unit of silk (觔息) in terms of "兩" (a smaller unit of weight). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
loan_silk = 57  # 貸絲五十七觔
annual_interest_silk = 16  # 限歲出息一十六觔

# Convert annual interest to "兩" (1 觔 = 16 兩)
annual_interest_liang = annual_interest_silk * 16  # 以一十六兩乘之

# Calculate the interest rate per 觔 in "兩"
a = Fraction(annual_interest_liang, loan_silk)  # 以貸絲五十七觔除之

# Output the result
a  # 答曰：a兩
#----- content ends here -----


"""


The variable `a` will contain the interest rate per 觔 in terms of "兩".
"""


"""
"""
