"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is an irregular (trapezoidal) field. The width is 65 bu. 
One side of the length is 100 bu, and the other side of the length is 72 bu.
Question: how large is the field?

The procedure says: Add the two irregular sides together and halve them. 
Then multiply by the regular width. Alternatively, halve the regular width and multiply by the sum of the irregular sides.
Finally, divide by the mu-divisor (240) to get the result in mu.

The answer says: *a* mu.
"""

from fractions import Fraction

# 正廣 (width) 65步
正廣 = 65

# 一畔從 (one side length) 100步
從一 = 100

# 一畔從 (other side length) 72步
從二 = 72

# 畝法 (mu divisor) 240
畝法 = 240

# 并兩邪而半之
平均從 = Fraction(從一 + 從二, 2)

# 以乘正廣
積步 = 平均從 * 正廣

# 畝法而一
a = Fraction(積步, 畝法)

a  # Output the result in mu#----- content ends here -----

"""
"""
