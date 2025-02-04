"""
今有凡錢五文買雉三隻，有錢一萬七千五百二十五文。問：得雉㡬何？
術曰：列錢數一萬七千五百二十五文，以雉三隻乘之得五萬二千五百七十五文，以五文除之即得。
答曰： a隻 。
"""

"""
To solve the problem, we translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
total_money = 17525  # in 文
price_per_3_pheasants = 5  # 5 文 for 3 pheasants

# Calculate the number of pheasants
a = Fraction(total_money * 3, price_per_3_pheasants)

# The result is stored in variable 'a'
a  # in 隻
#----- content ends here -----


"""


The variable `a` will contain the number of pheasants (隻).
"""


"""
"""
