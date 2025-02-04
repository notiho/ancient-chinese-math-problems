"""
今有貸與人絲五十七觔，限歲出息一十六觔。問：觔息幾何？
術曰：列限息絲一十六觔，以一十六兩乘之，得二百五十六兩，以貸絲五十七觔除之，不盡，約之，即得。
答曰： a兩 。
"""

"""
To solve this problem, we need to calculate the interest per unit of silk in terms of "兩" (liang). Here's the Python code:


"""


from fractions import Fraction

# Given values
total_silk = 57  # 貸絲 in 觔
interest_silk = 16  # 限息絲 in 觔

# Convert interest silk to 兩 (1 觔 = 16 兩)
interest_liang = interest_silk * 16

# Calculate interest per unit of silk in 兩
a = Fraction(interest_liang, total_silk)

# The result is stored in variable 'a'


"""


The solution is stored in the variable `a` as a fraction in terms of "兩".
"""


"""
"""
