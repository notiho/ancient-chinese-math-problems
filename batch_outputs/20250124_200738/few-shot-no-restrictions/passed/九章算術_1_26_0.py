"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is an irregular (trapezoidal) field, with one end having a width of 30 bu, the other end having a width of 42 bu, and the length being 64 bu.
Question: how large is the field?

The procedure says: Add the two irregular widths together and halve them. Multiply this by the length to get the area.
Alternatively, halve the length and multiply it by the sum of the widths to get the area.
Finally, divide the area by the mu-divisor (240) to get the number of mu.

Answer: *a* mu.
"""

from fractions import Fraction

# 一頭廣三十步
廣1 = 30

# 一頭廣四十二步
廣2 = 42

# 正從六十四步
正從 = 64

# 并兩邪而半之
平均廣 = Fraction(廣1 + 廣2, 2)

# 以乘正從若廣
積步 = 平均廣 * 正從

# 畝法二百四十步
畝法 = 240

# 畝法而一
a = Fraction(積步, 畝法)

a#----- content ends here -----

"""
"""
