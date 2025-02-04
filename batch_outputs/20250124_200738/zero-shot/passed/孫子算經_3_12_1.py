"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

"""
To solve this problem, we will compute the interest rate per unit of silk (觔息). The problem states that 57 觔 of silk is loaned, and the annual interest is 16 觔. We need to calculate the interest rate in terms of "兩" (1 觔 = 16 兩).

Here is the Python code to compute the value of `a`:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
loan_silk = 57  # in 觔
annual_interest = 16  # in 觔

# Convert annual interest to 兩 (1 觔 = 16 兩)
annual_interest_in_liang = annual_interest * 16  # in 兩

# Calculate interest rate per 觔 in 兩
a = Fraction(annual_interest_in_liang, loan_silk)

# The result is stored in variable `a`
#----- content ends here -----


"""


The value of `a` will represent the interest rate per 觔 in 兩.
"""


"""
"""
