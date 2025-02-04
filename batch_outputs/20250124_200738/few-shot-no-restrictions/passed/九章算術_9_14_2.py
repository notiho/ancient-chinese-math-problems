"""
今有句五步，股十二步。問︰句中容方幾何？
術曰：并句、股為法，句股相乘為實，實如法而一，得方一步。
荅曰：方 a步 。
"""

#----- content starts here -----
"""
Suppose there is a right triangle with a base (leg) of 5 bu and a height (leg) of 12 bu.
Question: how many square bu can fit into the rectangle formed by the base and height?

The procedure says: Add the base (leg) and height (leg) together to form the divisor.
Multiply the base (leg) by the height (leg) to form the dividend.
Divide the dividend by the divisor to obtain the square bu.

Answer: *a* square bu.
"""

# 句五步 (base/leg)
句 = 5

# 股十二步 (height/leg)
股 = 12

# 并句、股為法 (add base and height to form the divisor)
法 = 句 + 股

# 句股相乘為實 (multiply base and height to form the dividend)
實 = 句 * 股

# 實如法而一，得方一步 (divide the dividend by the divisor)
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
