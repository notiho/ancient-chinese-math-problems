"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a(=559/24)畝 。
"""

#----- content starts here -----
"""
Suppose there is an irregular (trapezoidal) field. Its straight width is 65 bu.
One side length is 100 bu, and the other side length is 72 bu.
Question: how large is the field?

The procedure says: Add the two slanted sides together and halve them.
Multiply this by the straight length or width.
Alternatively, halve the straight length or width and multiply it by the sum of the slanted sides.
Divide by the mu-divisor to obtain the result.

Answer: *a*(=559/24) mu.
"""

from fractions import Fraction

# 正廣六十五步
正廣 = 65

# 一畔從一百步
從一 = 100

# 一畔從七十二步
從二 = 72

# 并兩邪而半之
兩邪和 = 從一 + 從二
兩邪半 = Fraction(兩邪和, 2)

# 以乘正從若廣
積步 = 兩邪半 * 正廣

# 畝法而一
畝法 = 240
a = Fraction(積步, 畝法)  # 559/24#----- content ends here -----

"""
"""
