"""
今有簫田從四十八步一頭廣二十五步一頭廣三十五步。問：為田㡬何？
答曰： a畝
"""

#----- content starts here -----
"""
Suppose there is a field in the shape of a trapezoid. One side of the field is 48 bu long, one side is 25 bu wide, and the other side is 35 bu wide.
Question: how large is the field?

Answer: *a* mu.
"""

# Define the dimensions of the trapezoid
從 = 48  # Length of the field (base)
廣1 = 25  # Width of one end
廣2 = 35  # Width of the other end

# Calculate the area of the trapezoid in square bu
area_in_bu = Fraction(從 * (廣1 + 廣2), 2)

# Convert the area into mu (1 mu = 240 square bu)
a = Fraction(area_in_bu, 240)#----- content ends here -----

"""
"""
