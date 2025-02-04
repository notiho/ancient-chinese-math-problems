"""
今有田廣一里，從一里。問：為田幾何？
荅曰： a頃 。
"""

#----- content starts here -----
"""
Suppose there is a field with a width of 1 li and a length of 1 li.
Question: how large of a field does it make?

The answer says: *a* qing.
"""

# 廣一里 (1 li = 300 bu)
廣 = 300

# 從一里 (1 li = 300 bu)
從 = 300

# Multiply width and length to get the area in square bu
area_in_bu = 廣 * 從

# Convert square bu to qing (1 qing = 100,000 square bu)
a = Fraction(area_in_bu, 100000)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 9/10"""
