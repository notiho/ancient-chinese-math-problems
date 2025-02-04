"""
今有凡錢五文買雉三隻，有錢一萬七千五百二十五文。問：得雉㡬何？
術曰：列錢數一萬七千五百二十五文，以雉三隻乘之得五萬二千五百七十五文，以五文除之即得。
答曰： a隻 。
"""

#----- content starts here -----
"""
Suppose there are 5 wen (coins) used to buy 3 pheasants. Now there are 17,525 wen.
Question: how many pheasants can be obtained?

The procedure says: Take the amount of money, 17,525 wen, and multiply it by 3 pheasants, obtaining 52,575. 
Divide this by 5 wen to get the answer.

Answer: *a* pheasants.
"""

from fractions import Fraction

# 錢數
錢數 = 17525

# 雉數
雉數 = 3

# 每五文買三隻
每五文 = 5

# 以雉三隻乘之
總文數 = 雉數 * 錢數

# 以五文除之即得
a = Fraction(總文數, 每五文)

a#----- content ends here -----

"""
"""
