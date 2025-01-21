"""
今有曲池，上中周二丈，外周四丈，廣一丈，下中周一丈四尺，外周二丈四尺，廣五尺，深一丈。問︰積幾何？
荅曰： a尺 。
"""

"""
Suppose there is a curved pond with the following dimensions:
- The upper middle circumference is 2 zhang, the outer circumference is 4 zhang, and the width is 1 zhang.
- The lower middle circumference is 1 zhang 4 chi, the outer circumference is 2 zhang 4 chi, and the width is 5 chi.
- The depth is 1 zhang.

Question: What is the total volume of the pond?

Answer: The volume is *a* cubic chi.
"""

# Define dimensions
上中周 = 2 * 10  # Convert zhang to chi
上外周 = 4 * 10  # Convert zhang to chi
上廣 = 1 * 10  # Convert zhang to chi

下中周 = 1 * 10 + 4  # Convert zhang and chi to chi
下外周 = 2 * 10 + 4  # Convert zhang and chi to chi
下廣 = 5  # Already in chi

深 = 1 * 10  # Convert zhang to chi

# Calculate the average middle circumference and average width
平均中周 = Fraction(上中周 + 下中周, 2)
平均廣 = Fraction(上廣 + 下廣, 2)

# Calculate the volume
a = 平均中周 * 平均廣 * 深

# Output the result
a
"""
Variable 'a' has wrong value. Expected: 5650/3, Actual: 1275"""
