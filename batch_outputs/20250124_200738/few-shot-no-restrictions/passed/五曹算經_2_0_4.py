"""
今有丁二萬三千六百九十二人，責兵五千九百二十三人。問：㡬何丁出一兵？
術曰：列二萬三千六百九十二人，以五千九百二十三除之即得。
答曰： a 丁出一兵。
"""

#----- content starts here -----
"""
Suppose there are 23,692 adult males (丁), and 5,923 soldiers are required.
Question: how many adult males are needed to provide one soldier?

The procedure says: Place 23,692 adult males and divide it by 5,923 soldiers. The result is the number of adult males required to provide one soldier.

Answer: *a* adult males provide one soldier.
"""

from fractions import Fraction

# Total number of adult males (丁)
丁 = 23692

# Total number of soldiers required
兵 = 5923

# Calculate how many 丁 are required to provide one 兵
a = Fraction(丁, 兵)

a#----- content ends here -----

"""
"""
