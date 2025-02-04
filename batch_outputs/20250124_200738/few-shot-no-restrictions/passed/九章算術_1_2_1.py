"""
今有田廣一里，從一里。問：為田幾何？
里田術曰：廣從里數相乘得積里。以三百七十五乘之，即畝數。
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 li and a length of 1 li.
Question: how large is the field?

The procedure for li-fields says: Multiply the width and length in li to obtain the area in square li.
Multiply this by 375 to convert it into mu.
100 mu make 1 qing.

Answer: *a* qing.
"""

from fractions import Fraction

# 廣一里
廣 = 1  # in li

# 從一里
從 = 1  # in li

# 廣從里數相乘得積里
積里 = 廣 * 從  # in square li

# 以三百七十五乘之，即畝數
畝數 = 375 * 積里  # in mu

# 100 畝為 1 頃
a = Fraction(畝數, 100)  # in qing

a  # Output the result in qing#----- content ends here -----

"""
"""
