"""
今有田廣一里，從一里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 li and a length of 1 li.
Question: how large of a field does it make?

The procedure for li fields says: Multiply the width and length in li, obtaining the area in square li.
Multiply this by 375, obtaining the number of mu.

The answer says: *a* qing.
"""

# 廣一里
廣里數 = 1

# 從一里
從里數 = 1

# 廣從里數相乘得積里
積里 = 廣里數 * 從里數

# 以三百七十五乘之，即畝數
畝數 = 375 * 積里

# 100畝為1頃
a = Fraction(畝數, 100)#----- content ends here -----

"""
"""
