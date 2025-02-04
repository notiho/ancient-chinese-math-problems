"""
今有御米十四斗，欲為粟。問︰得幾何？
術曰：以御米求粟，五十之，二十一而一。
荅曰：為粟 a(=100/3)斗 。
"""

#----- content starts here -----
"""
Suppose there are 14 dou of polished rice. It is desired to convert it back into unhusked millet.
Question: how much unhusked millet does it make?

The procedure says: When seeking unhusked millet using polished rice, multiply by 50 and divide by 21.

Answer: it makes *a*(=100/3) dou of unhusked millet.
"""

# 御米十四斗
御米 = 14

# 以御米求粟，五十之
粟 = 50 * 御米

# 二十一而一
a = Fraction(粟, 21) # 100/3#----- content ends here -----

"""
"""
