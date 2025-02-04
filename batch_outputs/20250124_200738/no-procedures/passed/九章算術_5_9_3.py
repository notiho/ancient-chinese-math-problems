"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a canal with the following dimensions:
- Top width: 1 zhang 8 chi (18 chi)
- Bottom width: 3 chi 6 cun (3.6 chi)
- Depth: 1 zhang 8 chi (18 chi)
- Length: 51824 chi

Question: What is the total volume of the canal?

Answer: The volume is *a* cubic chi.
"""

# Dimensions
top_width = 18  # in chi
bottom_width = 3 + Fraction(6, 10)  # 3 chi 6 cun = 3.6 chi
depth = 18  # in chi
length = 51824  # in chi

# Formula for the volume of a trapezoidal prism:
# Volume = ( (top_width + bottom_width) / 2 ) * depth * length
a = Fraction((top_width + bottom_width), 2) * depth * length

# Result
a#----- content ends here -----

"""
"""
