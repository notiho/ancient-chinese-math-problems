"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a gold rod with a total length of 5 feet. The weight of the first and last foot is given, and we need to calculate the weight of each intermediate foot.

Here is the Python code:


"""


from fractions import Fraction

# Given data
total_length = 5  # in feet
weight_first_foot = 4  # in jin
weight_last_foot = 2  # in jin

# Step 1: Calculate the rate of decrease (差率)
rate_of_decrease = weight_first_foot - weight_last_foot  # 差率 = 本重 - 末重
rate_of_decrease_per_foot = Fraction(rate_of_decrease, total_length - 1)  # 差率 per foot

# Step 2: Calculate the weight of each foot
a = weight_last_foot  # 末一尺
b = a + rate_of_decrease_per_foot  # 次一尺
c = b + rate_of_decrease_per_foot  # 次一尺
d = c + rate_of_decrease_per_foot  # 次一尺
e = d + rate_of_decrease_per_foot  # 次一尺

# Results
a, b, c, d, e


"""


### Explanation:
1. **Rate of Decrease (差率):** The difference in weight between the first and last foot is divided evenly across the intermediate sections. This gives the rate of decrease per foot.
2. **Weight Calculation:** Starting from the last foot's weight (`a`), we add the rate of decrease per foot to calculate the weight of each subsequent foot (`b`, `c`, `d`, `e`).

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will contain the weights of each foot in `jin` as fractions.
"""


"""
"""
