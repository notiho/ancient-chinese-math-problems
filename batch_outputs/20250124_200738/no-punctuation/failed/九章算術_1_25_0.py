"""
又有圭田廣五步二分步之一從八步三分步之二問為田幾何
術曰半廣以乘正從
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a rectangular field with a width of 5 bu, 2/10 bu, and 1/100 bu (5 + 2/10 + 1/100 bu),
and a length of 8 bu, 3/10 bu, and 2/100 bu (8 + 3/10 + 2/100 bu).
Question: how large is the field?

The procedure says: Take half the width and multiply it by the full length.

The answer says: *a* bu.
"""

# 廣五步二分步之一
廣 = 5 + Fraction(2, 10) + Fraction(1, 100)

# 從八步三分步之二
從 = 8 + Fraction(3, 10) + Fraction(2, 100)

# 半廣以乘正從
半廣 = 廣 / 2
a = 半廣 * 從#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 143/6, Actual: 13546/625"""
