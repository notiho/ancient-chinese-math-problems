"""
今有錢一十七貫五百二十五文欲五文買雞三隻問得幾何
術曰置錢數以三因之五而一即得
答曰得雞 a隻
"""

#----- content starts here -----
"""
Suppose there is 17 guan and 525 wen of money. It is desired to buy chickens at a rate of 3 chickens for 5 wen.
Question: how many chickens can be bought?

The procedure says: Place the amount of money, multiply it by 3, and divide by 5. This gives the result.

Answer: *a* chickens.
"""

# 錢一十七貫五百二十五文
貫 = 17
文 = 525

# Convert 貫 to 文 (1 貫 = 1000 文)
總文數 = 貫 * 1000 + 文

# 以三因之
雞數 = 3 * 總文數

# 五而一
a = Fraction(雞數, 5)#----- content ends here -----

"""
"""
