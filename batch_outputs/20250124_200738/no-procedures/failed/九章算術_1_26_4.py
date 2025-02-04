"""
今有邪田，一頭廣三十步，一頭廣四十二步，正從六十四步。問：為田幾何？
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is an irregular (trapezoidal) field. One end is 30 bu wide, the other end is 42 bu wide, and the length (正從) is 64 bu.
Question: how large is the field?

Answer: it is *a* mu.
"""

# 一頭廣三十步
廣1 = 30

# 一頭廣四十二步
廣2 = 42

# 正從六十四步
正從 = 64

# Calculate the area in square bu (using the formula for the area of a trapezoid: (base1 + base2) * height / 2)
area_in_bu = (廣1 + 廣2) * 正從 / 2

# Convert the area from square bu to mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
