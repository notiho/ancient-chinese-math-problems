"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the weights of each segment of a gold rod based on the given weights of the first and last segments. Here's the Python code:


"""


from fractions import Fraction

# Given data
total_length = 5  # Total length of the rod in 尺
weight_first_segment = 4  # Weight of the first segment in 斤
weight_last_segment = 2  # Weight of the last segment in 斤

# Step 1: Calculate the rate of decrease (差率)
rate_of_decrease = weight_first_segment - weight_last_segment  # 差率 = 本重 - 末重

# Step 2: Calculate the weight of each segment
# The weights decrease linearly from the first segment to the last segment
a = weight_last_segment  # Weight of the last segment (末一尺)
b = a + Fraction(rate_of_decrease, total_length - 1)  # Weight of the second-to-last segment
c = b + Fraction(rate_of_decrease, total_length - 1)  # Weight of the third-to-last segment
d = c + Fraction(rate_of_decrease, total_length - 1)  # Weight of the fourth-to-last segment
e = d + Fraction(rate_of_decrease, total_length - 1)  # Weight of the first segment

# Output the results
a, b, c, d, e


"""


### Explanation:
1. **Given Data**:
   - The total length of the rod is 5 尺.
   - The weight of the first segment (本一尺) is 4 斤.
   - The weight of the last segment (末一尺) is 2 斤.

2. **Rate of Decrease**:
   - The difference in weight between the first and last segments is calculated as `weight_first_segment - weight_last_segment`.

3. **Weight of Each Segment**:
   - The weights decrease linearly, so the difference between consecutive segments is `rate_of_decrease / (total_length - 1)`.
   - Starting from the last segment, the weights are calculated incrementally.

4. **Output**:
   - The variables `a`, `b`, `c`, `d`, and `e` represent the weights of the 5 segments from the last to the first.

This code calculates the weights of each segment as fractions to ensure precision.
"""


"""
"""
