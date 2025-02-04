"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi in length.
Cut off 1 chi from the base, and it weighs 4 jin.
Cut off 1 chi from the tip, and it weighs 2 jin.
Question: How much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base, and the remainder is the rate of difference.
Then place the base weight, multiply it by the 4 intervals, and this gives the first decreasing value.
Place the base weight again, subtract the rate of difference from it, and each chi is successively reduced by this amount.
Place the first decreasing value as the divisor.
Multiply the base weight (4 jin) by each successive weight, and these are the dividends.
Divide the dividends by the divisor to obtain the weight of each chi.

Answer: The tip weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the base weighs *e* jin.
"""

from fractions import Fraction

# Given data
base_weight = 4  # Base weight in jin
tip_weight = 2   # Tip weight in jin
length = 5       # Total length in chi

# Step 1: Calculate the rate of difference
rate_of_difference = base_weight - tip_weight  # 差率

# Step 2: Calculate the first decreasing value (法)
法 = length - 1  # 4 intervals (5 chi total - 1 chi at the base)

# Step 3: Calculate the weights for each chi
weights = []
for i in range(法):
    weight = base_weight - i * Fraction(rate_of_difference, 法)
    weights.append(weight)

# Assign weights to each chi
e = weights[0]  # Base chi
d = weights[1]  # Next chi
c = weights[2]  # Next chi
b = weights[3]  # Next chi
a = weights[4]  # Tip chi

# Output
a, b, c, d, e#----- content ends here -----

"""
Code error: list index out of range"""
