"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""
Suppose there is a golden rod (金箠) that is 5 chi long. 
The first chi (base) weighs 4 jin, and the last chi (tip) weighs 2 jin.
Question: How much does each of the remaining chi weigh?

Answer: The last chi weighs *a* jin, the next chi weighs *b* jin, the next chi weighs *c* jin, the next chi weighs *d* jin, and the first chi weighs *e* jin.
"""

# Total length of the rod
total_length = 5

# Weight of the first chi (base)
base_weight = 4

# Weight of the last chi (tip)
tip_weight = 2

# The weight difference per chi (assuming linear distribution of weight)
weight_difference_per_chi = Fraction(base_weight - tip_weight, total_length - 1)

# Calculate the weight of each chi
e = base_weight  # First chi (base)
d = e - weight_difference_per_chi  # Second chi
c = d - weight_difference_per_chi  # Third chi
b = c - weight_difference_per_chi  # Fourth chi
a = tip_weight  # Fifth chi (tip)

# Results
a, b, c, d, e
"""
"""
