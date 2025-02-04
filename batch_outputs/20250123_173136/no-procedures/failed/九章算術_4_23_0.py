"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,644,864,375,000 cubic chi.
Question: what is the diameter of the cylinder if it is perfectly circular?

Answer: the diameter is *a* chi.
"""

# 積 (volume) = 1,644,864,375,000 cubic chi
積 = 1644864375000

# Formula for the volume of a cylinder: V = (π * r^2 * h)
# Here, we assume the height (h) is equal to the diameter (d), so:
# V = (π * (d/2)^2 * d) = (π * d^3) / 4
# Rearranging for d: d = (4 * V / π)^(1/3)

# Since π is approximated as 3 in ancient Chinese mathematics:
pi = 3

# Calculate the diameter
a = (Fraction(4 * 積, pi)) ** Fraction(1, 3)

# The result `a` is the diameter in chi.
"""
Variable 'a' has wrong value. Expected: 14300, Actual: 12992.406808347088"""
