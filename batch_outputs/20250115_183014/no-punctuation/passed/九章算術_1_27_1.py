"""
又有邪田正廣六十五步一畔從一百步一畔從七十二步問為田幾何
術曰并兩邪而半之以乘正從若廣又可半正從若廣以乘并畝法而一
荅曰 a畝 
"""

"""
Suppose there is an irregular (trapezoidal) field. The straight width is 65 bu. 
One slanted side is 100 bu, and the other slanted side is 72 bu.
Question: how large is the field?

The procedure says: Add the two slanted sides and halve them. Multiply this by the straight width.
If the straight width is instead treated as the slanted side, halve the straight width and multiply it by the sum of the slanted sides.
Divide by the mu-divisor (240) to obtain the number of mu.

The answer says: *a* mu.
"""

# 正廣六十五步
正廣 = 65

# 一畔從一百步
畔一 = 100

# 一畔從七十二步
畔二 = 72

# 并兩邪而半之
兩邪和 = 畔一 + 畔二
半兩邪 = Fraction(兩邪和, 2)

# 以乘正從
積步 = 半兩邪 * 正廣

# 畝法二百四十步
畝法 = 240

# 而一
a = Fraction(積步, 畝法)
"""
"""
