"""
今有邪田一頭廣三十步一頭廣四十二步正從六十四步問為田幾何
術曰并兩邪而半之以乘正從若廣又可半正從若廣以乘并畝法而一
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is an irregular field with one side having a width of 30 bu, the other side having a width of 42 bu, and a length of 64 bu.
Question: how large is the field?

The procedure says: Add the two irregular widths and halve them. Multiply this by the regular length.
If the width can also be halved, multiply the halved width by the length.
Divide by the mu-divisor (240) to obtain the number of mu.

Answer: *a* mu.
"""

# 一頭廣三十步
廣1 = 30

# 一頭廣四十二步
廣2 = 42

# 正從六十四步
正從 = 64

# 并兩邪而半之
平均廣 = (廣1 + 廣2) / 2

# 以乘正從
積步 = 平均廣 * 正從

# 畝法二百四十步
畝法 = 240

# 以畝法而一
a = Fraction(積步, 畝法)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
