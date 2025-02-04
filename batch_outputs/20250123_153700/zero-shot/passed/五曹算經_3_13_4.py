"""
今有凡錢五文買雉三隻，有錢一萬七千五百二十五文。問：得雉㡬何？
術曰：列錢數一萬七千五百二十五文，以雉三隻乘之得五萬二千五百七十五文，以五文除之即得。
答曰： a隻 。
"""

"""
To solve the problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
total_money = 17525  # in 文
money_per_pheasant = 5  # in 文
pheasants_for_5_wen = 3  # pheasants

# Calculation
a = Fraction(total_money * pheasants_for_5_wen, money_per_pheasant)

# Result
a  # in 隻


"""


The variable `a` will hold the number of pheasants (隻).
"""


"""
"""
