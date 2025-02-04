"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi in length.
The first chi (base) weighs 4 jin, and the last chi (tip) weighs 2 jin.
Question: how much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base; the remainder is the rate of difference.
Then place the base weight, multiply it by the 4 intervals (since there are 5 chi, there are 4 intervals), and this becomes the first decreasing value.
Place the difference rate as an auxiliary, subtract it for each chi, and each becomes its own decreasing value.
Place the first decreasing value as the divisor.
Multiply the base weight (4 jin) by each decreasing value to obtain the dividend.
Divide the dividend by the divisor to obtain the weight of each chi.

Answer: The last chi weighs *a* jin, the second-to-last chi weighs *b* jin, the third chi weighs *c* jin, the fourth chi weighs *d* jin, and the first chi weighs *e* jin.
"""

from fractions import Fraction

# Known values
base_weight = 4  # Base weight in jin
tip_weight = 2   # Tip weight in jin
length = 5       # Length of the rod in chi

# Step 1: Calculate the rate of difference
difference_rate = base_weight - tip_weight  # 差率

# Step 2: Calculate the first decreasing value (法)
法 = base_weight * (length - 1)  # 4 intervals for 5 chi

# Step 3: Calculate the decreasing values for each chi
decreasing_values = [base_weight - i * Fraction(difference_rate, length - 1) for i in range(length)]

# Step 4: Calculate the weight of each chi
weights = [Fraction(base_weight * value, 法) for value in decreasing_values]

# Assign weights to each chi
e, d, c, b, a = weights  # From base to tip

# Output results
a, b, c, d, e  # Weights of each chi from tip to base#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 1/2
Variable 'b' has wrong value. Expected: 5/2, Actual: 5/8
Variable 'c' has wrong value. Expected: 3, Actual: 3/4
Variable 'd' has wrong value. Expected: 7/2, Actual: 7/8
Variable 'e' has wrong value. Expected: 4, Actual: 1"""
