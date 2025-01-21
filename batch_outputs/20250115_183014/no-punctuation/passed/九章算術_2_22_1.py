"""
今有御米十四斗欲為粟問得幾何
術曰以御米求粟五十之二十一而一
荅曰為粟 a斗 
"""

"""
Suppose there are 14 dou of polished rice (御米). It is desired to turn it into unhusked millet (粟).
Question: how much unhusked millet does it make?

The procedure says: when seeking unhusked millet using polished rice, multiply by 50 and divide by 21.

The answer says: it makes *a* dou of unhusked millet.
"""

# 御米十四斗
御米 = 14

# 以御米求粟，五十之
粟 = 50 * 御米

# 二十一而一
a = Fraction(粟, 21)
"""
"""
