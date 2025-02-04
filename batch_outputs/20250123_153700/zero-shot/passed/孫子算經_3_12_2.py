"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

"""
To solve this problem, we will calculate the interest per unit weight (觔息) in terms of "兩" (a smaller unit of weight). Here's the Python code:


"""


from fractions import Fraction

# Given values
total_silk = 57  # 貸絲五十七觔
annual_interest = 16  # 限歲出息一十六觔

# Convert annual interest to "兩" (1 觔 = 16 兩)
annual_interest_in_liang = annual_interest * 16  # 以一十六兩乘之

# Calculate interest per 觔 in "兩"
a = Fraction(annual_interest_in_liang, total_silk)  # 以貸絲五十七觔除之

# The result is stored in variable 'a'


"""


The variable `a` will contain the interest per 觔 in terms of "兩".
"""


"""
"""
