"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi long. 
The first chi (base) weighs 4 jin, and the last chi (tip) weighs 2 jin. 
Question: how much does each of the intermediate chi weigh?

Answer: the first chi (base) weighs *a* jin, the second chi weighs *b* jin, the third chi weighs *c* jin, the fourth chi weighs *d* jin, and the fifth chi (tip) weighs *e* jin.
"""

# Total length of the rod
total_length = 5

# Weight of the base (first chi)
base_weight = 4

# Weight of the tip (last chi)
tip_weight = 2

# Weight difference per chi (linear distribution assumption)
weight_difference_per_chi = Fraction(base_weight - tip_weight, total_length - 1)

# Calculate the weight of each chi
a = base_weight
b = base_weight - weight_difference_per_chi
c = base_weight - 2 * weight_difference_per_chi
d = base_weight - 3 * weight_difference_per_chi
e = tip_weight

# Results
a, b, c, d, e#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 4
Variable 'b' has wrong value. Expected: 5/2, Actual: 7/2
Variable 'd' has wrong value. Expected: 7/2, Actual: 5/2
Variable 'e' has wrong value. Expected: 4, Actual: 2"""
