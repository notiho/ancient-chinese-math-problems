"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi long. 
Cutting off 1 chi from the base weighs 4 jin. 
Cutting off 1 chi from the tip weighs 2 jin. 
Question: how much does each intermediate chi weigh?

The procedure says: Subtract the weight of the tip from the weight of the base; the remainder is the rate of difference.
Place the base weight, and multiply it by the 4 intervals, obtaining the first decreasing value.
Place the base weight again, subtracting the rate of difference each time, to obtain the weights for each chi.
Place the first decreasing value as the divisor.
Multiply the base weight (4 jin) by each weight in the sequence to obtain the dividend.
Divide the dividend by the divisor to obtain the weight of each chi.

Answer: The tip chi weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the base chi weighs *e* jin.
"""

from fractions import Fraction

# Given data
base_weight = 4  # Base weight in jin
tip_weight = 2   # Tip weight in jin
length = 5       # Total length in chi

# Step 1: Calculate the rate of difference
rate_of_difference = base_weight - tip_weight  # 差率

# Step 2: Calculate the weights for each chi
weights = [base_weight - i * Fraction(rate_of_difference, length - 1) for i in range(length)]

# Step 3: Assign weights to each chi
e, d, c, b, a = weights  # Assigning weights from base to tip

# Output the results
a, b, c, d, e  # Weights of each chi from tip to base#----- content ends here -----

"""
"""
