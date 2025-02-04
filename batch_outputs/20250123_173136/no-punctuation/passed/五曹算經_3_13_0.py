"""
今有凡錢五文買雉三隻有錢一萬七千五百二十五文問得雉㡬何
術曰列錢數一萬七千五百二十五文以雉三隻乘之得五萬二千五百七十五文以五文除之即得
答曰 a隻 
"""

"""
Suppose there are 5 wen (coins) used to buy 3 pheasants. 
Now, there are 17,525 wen. 
Question: how many pheasants can be bought?

The procedure says: Write down the amount of money, 17,525 wen.
Multiply it by 3 pheasants, obtaining 52,575 wen.
Divide it by 5 wen, and the result is the number of pheasants.

Answer: *a* pheasants.
"""

# 錢數一萬七千五百二十五文
錢數 = 17525

# 雉三隻
雉數 = 3

# 乘之得五萬二千五百七十五文
總錢數 = 雉數 * 錢數

# 五文
單價 = 5

# 以五文除之即得
a = Fraction(總錢數, 單價)
"""
"""
