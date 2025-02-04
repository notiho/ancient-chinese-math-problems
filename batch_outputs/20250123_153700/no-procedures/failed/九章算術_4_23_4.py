"""
又有積一萬六千四百四十八億六千六百四十三萬七千五百尺。問︰為立圓徑幾何？
荅曰： a尺 。
"""

"""
Suppose there is a volume of 1,644,864,375,000 cubic chi.
Question: what is the diameter of a sphere with this volume?

Answer: the diameter is *a* chi.
"""

# 積 (volume) = 1,644,864,375,000 cubic chi
積 = 1644864375000

# Formula for the volume of a sphere: V = (π/6) * d^3
# Rearranging for diameter (d): d = (6 * V / π)^(1/3)

# Since π is approximated as 3 in ancient Chinese mathematics:
pi = 3

# Calculate the diameter
a = Fraction(6 * 積, pi) ** Fraction(1, 3)

# Note: The cube root calculation is symbolic here since Python's `Fraction` does not directly support roots.
"""
Variable 'a' has wrong value. Expected: 14300, Actual: 14872.59311856179"""
