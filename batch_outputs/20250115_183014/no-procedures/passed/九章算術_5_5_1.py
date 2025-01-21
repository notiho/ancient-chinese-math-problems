"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a ditch with the following dimensions:
- Top width: 1 zhang 5 chi
- Bottom width: 1 zhang
- Depth: 5 chi
- Length: 7 zhang

Question: What is the volume of the ditch?

Answer: The volume is *a* cubic chi.
"""

# Dimensions of the ditch
上廣 = 1 * 10 + 5  # Convert 1 zhang 5 chi to chi
下廣 = 1 * 10       # Convert 1 zhang to chi
深 = 5             # Depth in chi
袤 = 7 * 10        # Convert 7 zhang to chi

# The formula for the volume of a trapezoidal prism is:
# Volume = ((Top Width + Bottom Width) / 2) * Depth * Length
a = Fraction((上廣 + 下廣), 2) * 深 * 袤

# Result is in cubic chi
a
"""
"""
