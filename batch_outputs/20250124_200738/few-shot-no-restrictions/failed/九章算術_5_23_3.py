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

The procedure for calculating the volume of a haystack, curved pond, circular pond, or deep valley is the same:
1. Double the top length, and add it to the bottom length.
2. Double the bottom length, and add it to the top length.
3. Multiply each by its respective width.
4. Add these two results together.
5. Multiply the sum by the height (or depth).
6. Divide the result by 6 to get the final volume.

For curved ponds, the top and bottom lengths are calculated by summing the inner, middle, and outer perimeters and halving them.

Answer: The volume is *a* chi³.
"""

from fractions import Fraction

# Dimensions of the haystack (in zhang)
下廣 = 2  # Bottom width
下袤 = 3  # Bottom length
上廣 = 3  # Top width
上袤 = 4  # Top length
高 = 3    # Height

# Step 1: Double the top length and add it to the bottom length
倍上袤 = 2 * 上袤
下袤從之 = 倍上袤 + 下袤

# Step 2: Double the bottom length and add it to the top length
倍下袤 = 2 * 下袤
上袤從之 = 倍下袤 + 上袤

# Step 3: Multiply each by its respective width
上積 = 上袤從之 * 上廣
下積 = 下袤從之 * 下廣

# Step 4: Add the two results together
總積 = 上積 + 下積

# Step 5: Multiply the sum by the height
體積 = 總積 * 高

# Step 6: Divide by 6
a = Fraction(體積, 6)

# Convert the result to chi³ (1 zhang³ = 1000 chi³)
a_in_chi_cubed = a * 1000

a_in_chi_cubed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26500, Actual: 26"""
