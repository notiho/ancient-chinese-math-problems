"""
今有塹上廣一丈六尺三寸，下廣一丈，深六尺三寸，袤一十三丈二尺一寸。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a trench with the following dimensions:
- Top width: 1 zhang 6 chi 3 cun (1丈6尺3寸)
- Bottom width: 1 zhang (1丈)
- Depth: 6 chi 3 cun (6尺3寸)
- Length: 13 zhang 2 chi 1 cun (13丈2尺1寸)

Question: What is the volume of the trench?

Answer: The volume is *a* cubic chi (尺³).
"""

# Convert all dimensions to chi (尺)
top_width = 1 * 10 + 6 + Fraction(3, 10)  # 1丈6尺3寸 = 16.3尺
bottom_width = 1 * 10  # 1丈 = 10尺
depth = 6 + Fraction(3, 10)  # 6尺3寸 = 6.3尺
length = 13 * 10 + 2 + Fraction(1, 10)  # 13丈2尺1寸 = 132.1尺

# The formula for the volume of a trapezoidal prism is:
# V = (1/2) * (top_width + bottom_width) * depth * length
a = Fraction(1, 2) * (top_width + bottom_width) * depth * length

# The result is in cubic chi (尺³).
"""
Variable 'a' has wrong value. Expected: 54719/5, Actual: 21887649/2000"""
