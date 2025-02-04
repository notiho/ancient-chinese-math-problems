"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a volume of 1,644,864,375,000 cubic chi.
Question: what is the diameter of a sphere with this volume?

Answer: the diameter is *a* chi.
"""

# Volume of the sphere
積 = 1644864375000

# Formula for the volume of a sphere: V = (π/6) * d^3
# Rearrange to solve for diameter (d): d = (6 * V / π)^(1/3)

# Since π is approximated as 3 in ancient Chinese mathematics:
π = 3

# Calculate diameter
a = Fraction(6 * 積, π) ** Fraction(1, 3)

a  # Diameter in chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 14300, Actual: 14872.59311856179"""
