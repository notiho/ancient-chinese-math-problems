"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
術曰：并兩邪而半之，以乘正從若廣。又可半正從若廣，以乘并。畝法而一。
荅曰： a(=48/5)畝 。
"""

#----- content starts here -----
"""
Suppose there is an irregular (trapezoidal) field. One end has a width of 30 bu, and the other end has a width of 42 bu. The length (正從) is 64 bu.
Question: how large is the field?

The procedure says: Add the two irregular widths and halve them. Multiply this by the length (or the average width).
Alternatively, halve the length (or the average width) and multiply it by the sum of the widths.
Divide by the mu-divisor (240 bu² per mu) to obtain the number of mu.

Answer: *a*(=48/5) mu.
"""

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

# 畝法而一 (畝法 = 240)
畝法 = 240
a = Fraction(積步, 畝法)  # 48/5#----- content ends here -----

"""
"""
