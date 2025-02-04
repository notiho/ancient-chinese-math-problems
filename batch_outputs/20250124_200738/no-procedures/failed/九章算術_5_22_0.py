"""
今有芻甍，下廣三丈，袤四丈，上袤二丈，無廣，高一丈。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a thatched roof (芻甍) with the following dimensions:
- Bottom width: 3 zhang
- Bottom length: 4 zhang
- Top length: 2 zhang (no width at the top)
- Height: 1 zhang

Question: What is the volume of the roof?

Answer: The volume is *a* cubic chi.
"""

# Dimensions in zhang
下廣 = 3  # Bottom width in zhang
袤下 = 4  # Bottom length in zhang
袤上 = 2  # Top length in zhang
高 = 1    # Height in zhang

# Convert all dimensions to chi (1 zhang = 10 chi)
下廣 = 下廣 * 10
袤下 = 袤下 * 10
袤上 = 袤上 * 10
高 = 高 * 10

# The volume of a trapezoidal prism is calculated as:
# V = (1/2) * 高 * (袤下 + 袤上) * 下廣
a = Fraction(1, 2) * 高 * (袤下 + 袤上) * 下廣

a  # The volume in cubic chi#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 5000, Actual: 9000"""
