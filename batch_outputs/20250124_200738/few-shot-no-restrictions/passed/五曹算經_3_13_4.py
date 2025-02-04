"""
今有凡錢五文買雉三隻，有錢一萬七千五百二十五文。問：得雉㡬何？
術曰：列錢數一萬七千五百二十五文，以雉三隻乘之得五萬二千五百七十五文，以五文除之即得。
答曰： a隻 。
"""

#----- content starts here -----
"""
Suppose there are 5 wen (coins) used to buy 3 pheasants. 
Now, there are 17,525 wen. 
Question: how many pheasants can be obtained?

The procedure says: Write down the number of coins, 17,525 wen. 
Multiply it by 3 pheasants, obtaining 52,575. 
Divide it by 5 wen, and the result is the number of pheasants.

Answer: *a* pheasants.
"""

from fractions import Fraction

# 錢五文買雉三隻
錢 = 5
雉 = 3

# 有錢一萬七千五百二十五文
總錢 = 17525

# 以雉三隻乘之得五萬二千五百七十五文
總雉文 = 總錢 * 雉

# 以五文除之即得
a = Fraction(總雉文, 錢)

# Output the result
a#----- content ends here -----

"""
"""
