"""
今有御米十四斗，欲為粟。問︰得幾何？
荅曰：為粟 a斗 。
"""

#----- content starts here -----
"""
Suppose there are 14 dou of polished rice (御米). It is desired to convert it back into unhusked millet (粟).
Question: how much unhusked millet does it make?

Answer: it makes *a* dou of unhusked millet.
"""

# 御米十四斗
御米 = 14

# To convert polished rice to unhusked millet, multiply by 2 and divide by 3
a = Fraction(2 * 御米, 3)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 100/3, Actual: 28/3"""
