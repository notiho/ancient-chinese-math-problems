"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""
Suppose there is a golden rod, 5 chi long. 
The first chi from the base weighs 4 jin, and the last chi from the tip weighs 2 jin.
Question: How much does each of the remaining chi weigh?

Answer: The first chi from the tip weighs *a* jin, the second chi weighs *b* jin, the third chi weighs *c* jin, the fourth chi weighs *d* jin, and the fifth chi weighs *e* jin.
"""

# Known values
total_length = 5  # chi
base_weight = 4  # jin
tip_weight = 2  # jin

# Weight difference per chi (assuming linear distribution)
weight_difference_per_chi = Fraction(base_weight - tip_weight, total_length - 1)

# Calculate weights for each chi
e = tip_weight  # last chi (5th chi)
d = e + weight_difference_per_chi  # 4th chi
c = d + weight_difference_per_chi  # 3rd chi
b = c + weight_difference_per_chi  # 2nd chi
a = b + weight_difference_per_chi  # 1st chi

# Results
a, b, c, d, e  # These are the weights of each chi from base to tip.
"""
Variable 'a' has wrong value. Expected: 2, Actual: 4
Variable 'b' has wrong value. Expected: 5/2, Actual: 7/2
Variable 'd' has wrong value. Expected: 7/2, Actual: 5/2
Variable 'e' has wrong value. Expected: 4, Actual: 2"""
