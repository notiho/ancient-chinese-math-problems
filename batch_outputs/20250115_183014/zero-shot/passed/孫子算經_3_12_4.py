"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

"""
To solve this problem, we will compute the interest rate per unit (觔息) in terms of "兩" (a smaller unit of weight). Here's the Python code:


"""


from fractions import Fraction

# Given values
loan_silk = 57  # 貸絲五十七觔
annual_interest_silk = 16  # 限歲出息一十六觔
conversion_rate = 16  # 一觔 = 16 兩

# Convert annual interest to "兩"
annual_interest_in_liang = annual_interest_silk * conversion_rate

# Compute the interest rate per unit (觔息) in "兩"
a = Fraction(annual_interest_in_liang, loan_silk)

# The result is stored in variable 'a'


"""


The solution is stored in the variable `a` as a `Fraction` object, representing the interest rate per unit (觔息) in "兩".
"""


"""
"""
