"""
今有箕田，舌廣二十步，踵廣五步，正從三十步。問：為田幾何？
術曰：并踵、舌而半之，以乘正從。畝法而一。
荅曰： a畝 。
"""

#----- content starts here -----
"""
Suppose there is a trapezoidal field (箕田) with the following dimensions:
- The width of the "tongue" (舌廣) is 20 bu.
- The width of the "heel" (踵廣) is 5 bu.
- The length (正從) is 30 bu.

Question: how large is the field in mu?

The procedure says:
Add the widths of the tongue and heel, then halve the result. Multiply this by the length.
Finally, divide by the mu-divisor (240 bu² per mu) to obtain the area in mu.

Answer: *a* mu.
"""

from fractions import Fraction

# 舌廣二十步
舌廣 = 20

# 踵廣五步
踵廣 = 5

# 正從三十步
正從 = 30

# 畝法 (240步² per 畝)
畝法 = 240

# 并踵、舌而半之
平均廣 = Fraction(舌廣 + 踵廣, 2)

# 以乘正從
積步 = 平均廣 * 正從

# 畝法而一
a = Fraction(積步, 畝法)

a  # Output the result in 畝#----- content ends here -----

"""
"""
