"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,644,864,375,000 cubic chi (尺).
Question: what is the diameter of a sphere with this volume?

Answer: the diameter is *a* chi.
"""

# Given volume
積 = 1644864375000

# Formula for the volume of a sphere: V = (π/6) * d^3
# Rearranging for diameter: d = (6 * V / π)^(1/3)

# Since π is approximated as 3 in ancient Chinese mathematics:
π = 3

# Calculate the diameter
a = Fraction(6 * 積, π) ** Fraction(1, 3)

# Note: The result `a` will be in terms of fractions, representing the diameter in chi.
"""
Variable 'a' has wrong value. Expected: 14300, Actual: 14872.59311856179"""
