"""
今有芻童，下廣二丈，袤三丈，上廣三丈，袤四丈，高三丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a haystack (芻童) with the following dimensions:
- Bottom width: 2 zhang
- Bottom length: 3 zhang
- Top width: 3 zhang
- Top length: 4 zhang
- Height: 3 zhang

Question: What is the total volume?

The procedure for haystacks, curved ponds, circular ponds, and deep valleys is the same. The procedure says:
Double the top length, and let the bottom length follow it. Also, double the bottom length, and let the top length follow it.
Multiply each by its respective width, add them together, and multiply by the height (or depth). Divide the result by 6.

For curved ponds, add the inner, middle, and outer perimeters of the top and halve them to get the top length. Do the same for the bottom.

Answer: *a* cubic chi.
"""

from fractions import Fraction

# Dimensions of the haystack
下廣 = 2  # Bottom width in zhang
下袤 = 3  # Bottom length in zhang
上廣 = 3  # Top width in zhang
上袤 = 4  # Top length in zhang
高 = 3    # Height in zhang

# Convert zhang to chi (1 zhang = 10 chi)
下廣 *= 10
下袤 *= 10
上廣 *= 10
上袤 *= 10
高 *= 10

# Procedure:
# Double the top length, and let the bottom length follow it
倍上袤 = 2 * 上袤
倍下袤 = 下袤

# Double the bottom length, and let the top length follow it
倍下袤 = 2 * 下袤
倍上袤 = 上袤

# Multiply each by its respective width
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# Add them together
總積 = 上積 + 下積

# Multiply by the height
總積 *= 高

# Divide by 6
a = Fraction(總積, 6)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26500, Actual: 12000"""
