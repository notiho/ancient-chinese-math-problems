"""
又有邪田，正廣六十五步，一畔從一百步，一畔從七十二步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a畝 。
"""

"""
Suppose there is an irregular (slanted) field. The straight width is 65 bu, one slanted length is 100 bu, and the other slanted length is 72 bu.
Question: how large is the field?

The procedure says: Add the two slanted lengths together and halve them. Multiply this by the straight width.
Alternatively, halve the straight width and multiply it by the sum of the slanted lengths.
In either case, divide by the mu-divisor (240) to obtain the number of mu.

Answer: *a* mu.
"""

# 正廣六十五步
正廣 = 65

# 一畔從一百步
從一 = 100

# 一畔從七十二步
從二 = 72

# 并兩邪而半之
兩邪和 = 從一 + 從二
半兩邪 = Fraction(兩邪和, 2)

# 以乘正從若廣
積步 = 半兩邪 * 正廣

# 畝法而一
畝法 = 240
a = Fraction(積步, 畝法)
"""
"""
