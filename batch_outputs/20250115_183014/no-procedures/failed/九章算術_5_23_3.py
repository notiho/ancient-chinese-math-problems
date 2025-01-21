"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a haystack (芻童) with the following dimensions:
- Bottom width: 2 zhang
- Bottom length: 3 zhang
- Top width: 3 zhang
- Top length: 4 zhang
- Height: 3 zhang

Question: What is the volume of the haystack?

Answer: The volume is *a* cubic chi.
"""

# Convert all dimensions to chi (1 zhang = 10 chi)
bottom_width = 2 * 10  # 2 zhang = 20 chi
bottom_length = 3 * 10  # 3 zhang = 30 chi
top_width = 3 * 10  # 3 zhang = 30 chi
top_length = 4 * 10  # 4 zhang = 40 chi
height = 3 * 10  # 3 zhang = 30 chi

# Calculate the average base area (using the formula for a trapezoid)
average_base_area = Fraction((bottom_width * bottom_length + top_width * top_length), 2)

# Calculate the volume (average base area * height)
a = average_base_area * height

a  # The volume in cubic chi
"""
Variable 'a' has wrong value. Expected: 26500, Actual: 27000"""
