"""
今有穿地，袤一丈六尺，深一丈，上廣六尺，為垣積五百七十六尺。問︰穿地下廣幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is an excavation with:
- Length (袤) = 1 zhang 6 chi = 16 chi,
- Depth (深) = 1 zhang = 10 chi,
- Top width (上廣) = 6 chi,
- Total volume (垣積) = 576 chi³.

Question: What is the bottom width (下廣)?

Answer: The bottom width is *a* chi.
"""

# Given values
length = 16  # chi
depth = 10  # chi
top_width = 6  # chi
volume = 576  # chi³

# Formula for the volume of a trapezoidal prism:
# Volume = ( (Top Width + Bottom Width) / 2 ) * Depth * Length
# Rearrange to solve for Bottom Width:
# Bottom Width = ( (2 * Volume) / (Depth * Length) ) - Top Width

a = Fraction(2 * volume, depth * length) - top_width

# The bottom width is `a`.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 18/5, Actual: 6/5"""
