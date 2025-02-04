"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi in length.
Cutting off 1 chi from the base weighs 4 jin.
Cutting off 1 chi from the tip weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base; the remainder is the rate of difference.
Then place the base weight, multiply it by the 4 intervals, and this becomes the first weight decrease.
Place the difference rate, subtract it for each chi, and each becomes its own weight.
Place the first weight decrease as the divisor.
Multiply the base weight (4 jin) by the sequence of weights, and each becomes its own dividend.
Divide the dividend by the divisor to obtain the weight of each chi.

Answer: The tip weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the next chi weighs *e* jin.
"""

from fractions import Fraction

# Known values
base_weight = 4  # Base weight (斤)
tip_weight = 2   # Tip weight (斤)
length = 5       # Total length (尺)

# Step 1: Calculate the rate of difference
difference_rate = base_weight - tip_weight  # 差率

# Step 2: Calculate the first weight decrease
first_weight_decrease = difference_rate * (length - 1)  # 下第一衰

# Step 3: Calculate the weights for each chi
weights = []
for i in range(length):
    weight = base_weight - (difference_rate * i)
    weights.append(weight)

# Step 4: Normalize weights using the first weight decrease
normalized_weights = [Fraction(weight * base_weight, first_weight_decrease) for weight in weights]

# Assign results
a, b, c, d, e = normalized_weights

# Output results
a, b, c, d, e  # These are the weights for each chi in jin#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 5/2, Actual: 1
Variable 'c' has wrong value. Expected: 3, Actual: 0
Variable 'd' has wrong value. Expected: 7/2, Actual: -1
Variable 'e' has wrong value. Expected: 4, Actual: -2"""
