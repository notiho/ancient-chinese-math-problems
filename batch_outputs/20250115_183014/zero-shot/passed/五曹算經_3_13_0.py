"""
今有凡錢五文買雉三隻，有錢一萬七千五百二十五文。問：得雉㡬何？
術曰：列錢數一萬七千五百二十五文，以雉三隻乘之得五萬二千五百七十五文，以五文除之即得。
答曰： a隻 。
"""

"""
To solve this problem, we need to compute the number of pheasants (雉) that can be bought with 17,525 coins, given that 5 coins can buy 3 pheasants. Here's the Python code:


"""


from fractions import Fraction

# Given values
total_money = 17525  # in 文
pheasants_per_5_coins = 3  # pheasants bought with 5 coins
cost_per_3_pheasants = 5  # cost in 文 for 3 pheasants

# Calculation
a = Fraction(total_money * pheasants_per_5_coins, cost_per_3_pheasants)

# The result is the number of pheasants
a  # in 隻


"""


The variable `a` will hold the number of pheasants that can be bought.
"""


"""
"""
