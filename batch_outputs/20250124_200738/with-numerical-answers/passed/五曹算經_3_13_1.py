"""
今有凡錢五文買雉三隻，有錢一萬七千五百二十五文。問：得雉㡬何？
術曰：列錢數一萬七千五百二十五文，以雉三隻乘之得五萬二千五百七十五文，以五文除之即得。
答曰： a(=10515)隻 。
"""

#----- content starts here -----
"""
Suppose there are 5 wen used to buy 3 pheasants. Now there are 17,525 wen.
Question: how many pheasants can be obtained?

The procedure says: Place the number of wen, 17,525. Multiply it by 3 pheasants, obtaining 52,575 wen.
Divide it by 5 wen, and the result is the number of pheasants.

Answer: *a*(=10,515) pheasants.
"""

# 錢五文買雉三隻
錢 = 5
雉 = 3

# 有錢一萬七千五百二十五文
總錢 = 17525

# 以雉三隻乘之得五萬二千五百七十五文
總雉錢 = 總錢 * 雉

# 以五文除之即得
a = Fraction(總雉錢, 錢) # 10515隻#----- content ends here -----

"""
"""
