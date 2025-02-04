"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a valley (冥谷) with the following dimensions:
- The top width is 2 zhang, and the top length is 7 zhang.
- The bottom width is 8 chi, and the bottom length is 4 zhang.
- The depth is 6 zhang and 5 chi.

Question: What is the total volume?

The procedure for irregular shapes like valleys (冥谷), ponds (曲池), and similar structures is the same:
1. Double the top length, and add the bottom length to it.
2. Double the bottom length, and add the top length to it.
3. Multiply each result by its respective width.
4. Add the two results together.
5. Multiply the sum by the depth.
6. Divide the final result by 6.

Answer: The total volume is *a* chi³.
"""

from fractions import Fraction

# Dimensions
top_width = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
top_length = 7 * 10  # Convert zhang to chi
bottom_width = 8  # Already in chi
bottom_length = 4 * 10  # Convert zhang to chi
depth = 6 * 10 + 5  # Convert depth to chi (6 zhang 5 chi)

# Step 1: Double the top length and add the bottom length
top_term = 2 * top_length + bottom_length

# Step 2: Double the bottom length and add the top length
bottom_term = 2 * bottom_length + top_length

# Step 3: Multiply each term by its respective width
top_area = top_term * top_width
bottom_area = bottom_term * bottom_width

# Step 4: Add the two areas together
total_area = top_area + bottom_area

# Step 5: Multiply the total area by the depth
volume = total_area * depth

# Step 6: Divide the result by 6
a = Fraction(volume, 6)

# Output the result
a#----- content ends here -----

"""
"""
