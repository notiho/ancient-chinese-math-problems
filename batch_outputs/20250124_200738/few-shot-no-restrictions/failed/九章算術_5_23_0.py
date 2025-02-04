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
1. Double the top length, and let the bottom length follow it.
2. Double the bottom length, and let the top length follow it.
3. Multiply each by its respective width.
4. Add the results together.
5. Multiply the sum by the height (or depth).
6. Divide the result by 6.

For curved ponds:
- Add the inner, middle, and outer circumferences of the top and halve it to get the top length.
- Similarly, add the inner, middle, and outer circumferences of the bottom and halve it to get the bottom length.

Answer: The volume is *a* chi³.
"""

from fractions import Fraction

# Dimensions in zhang
下廣 = 2  # Bottom width
下袤 = 3  # Bottom length
上廣 = 3  # Top width
上袤 = 4  # Top length
高 = 3    # Height

# Step 1: Double the top length, bottom length follows
倍上袤 = 2 * 上袤
倍上積 = 倍上袤 * 上廣

# Step 2: Double the bottom length, top length follows
倍下袤 = 2 * 下袤
倍下積 = 倍下袤 * 下廣

# Step 3: Add the results
積和 = 倍上積 + 倍下積

# Step 4: Multiply by height
積高 = 積和 * 高

# Step 5: Divide by 6
a = Fraction(積高, 6)

# Convert to chi³ (1 zhang = 10 chi, so 1 zhang³ = 1000 chi³)
a_in_chi_cubed = a * 1000

a_in_chi_cubed#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 26500, Actual: 18"""
