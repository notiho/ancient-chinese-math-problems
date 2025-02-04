"""
今有凡錢五文買雉三隻有錢一萬七千五百二十五文問得雉㡬何
術曰列錢數一萬七千五百二十五文以雉三隻乘之得五萬二千五百七十五文以五文除之即得
答曰 a隻 
"""

#----- content starts here -----
"""
Suppose there are 5 wen (coins) used to buy 3 pheasants.
Now, with 17,525 wen, how many pheasants can be bought?

The procedure says: Arrange the amount of money, 17,525 wen.
Multiply it by 3 pheasants, obtaining 52,575 wen.
Divide it by 5 wen, and the result is the number of pheasants.

Answer: *a* pheasants.
"""

# 錢數一萬七千五百二十五文
錢數 = 17525

# 雉三隻
雉數 = 3

# 以雉三隻乘之，得五萬二千五百七十五文
總錢數 = 雉數 * 錢數

# 以五文除之，即得
a = Fraction(總錢數, 5)#----- content ends here -----

"""
"""
