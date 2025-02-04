"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
芻童、曲池、盤池、冥谷，皆同術。術曰：倍上袤，下袤從之，亦倍下袤，上袤從之，各以其廣乘之，并，以高若深乘之，皆六而一。其曲池者，并上中、外周而半之，以為上袤；亦并下中、外周而半之，以為下袤。
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a curved pond. The dimensions are as follows:
- The upper middle circumference is 2 zhang.
- The upper outer circumference is 4 zhang.
- The width at the top is 1 zhang.
- The lower middle circumference is 1 zhang 4 chi.
- The lower outer circumference is 2 zhang 4 chi.
- The width at the bottom is 5 chi.
- The depth is 1 zhang.

Question: What is the volume of the pond?

The procedure for curved ponds, circular ponds, and valleys is the same:
1. Double the upper length, and add the lower length to it. Similarly, double the lower length, and add the upper length to it.
2. Multiply each by its respective width.
3. Add the two results together, and multiply by the height or depth.
4. Divide the result by 6 to get the volume.
For curved ponds, add the upper middle and outer circumferences, divide by 2 to get the upper length. Similarly, add the lower middle and outer circumferences, divide by 2 to get the lower length.

Answer: The volume is *a* chi³.
"""

from fractions import Fraction

# Dimensions
上中周 = 2 * 10  # Convert zhang to chi
上外周 = 4 * 10  # Convert zhang to chi
上廣 = 1 * 10    # Convert zhang to chi
下中周 = 1 * 10 + 4  # Convert zhang and chi to chi
下外周 = 2 * 10 + 4  # Convert zhang and chi to chi
下廣 = 5           # Already in chi
深 = 1 * 10        # Convert zhang to chi

# Calculate 上袤 (upper length)
上袤 = Fraction(上中周 + 上外周, 2)

# Calculate 下袤 (lower length)
下袤 = Fraction(下中周 + 下外周, 2)

# Double the upper length and add the lower length
倍上袤 = 2 * 上袤 + 下袤

# Double the lower length and add the upper length
倍下袤 = 2 * 下袤 + 上袤

# Multiply each by its respective width
上積 = 倍上袤 * 上廣
下積 = 倍下袤 * 下廣

# Add the two results together
總積 = 上積 + 下積

# Multiply by the depth
體積 = 總積 * 深

# Divide by 6 to get the final volume
a = Fraction(體積, 6)

# Output the result
a#----- content ends here -----

"""
"""
