"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
城、垣、隄、溝、壍、渠，皆同術。術曰：并上下廣而半之，以高若深乘之，又以袤乘之，即積尺。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a levee with the following dimensions:
- Bottom width: 2 zhang
- Top width: 8 chi
- Height: 4 chi
- Length: 12 zhang and 7 chi

Question: What is the total volume in cubic chi?

The procedure says: Add the top and bottom widths, then halve the sum. Multiply this by the height (or depth), and then multiply the result by the length. This gives the total volume in cubic chi.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Dimensions
下廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上廣 = 8  # Already in chi
高 = 4  # Height in chi
袤 = 12 * 10 + 7  # Convert length to chi (12 zhang and 7 chi)

# Procedure
# Add top and bottom widths, then halve the sum
平均廣 = Fraction(下廣 + 上廣, 2)

# Multiply by height
截面積 = 平均廣 * 高

# Multiply by length
積 = 截面積 * 袤

# Answer
a = 積
a#----- content ends here -----

"""
"""
