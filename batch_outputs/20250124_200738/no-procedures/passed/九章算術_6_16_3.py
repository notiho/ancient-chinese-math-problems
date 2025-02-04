"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

#----- content starts here -----
"""
Suppose there is a golden rod, 5 chi long. 
The first chi (from the base) weighs 4 jin, and the last chi (from the tip) weighs 2 jin.
Question: How much does each of the intermediate chi weigh?

Answer: The last chi weighs *a* jin, the second-to-last chi weighs *b* jin, the third-to-last chi weighs *c* jin, the fourth-to-last chi weighs *d* jin, and the first chi weighs *e* jin.
"""

# Length of the rod
total_length = 5

# Weight of the first chi (base)
base_weight = 4

# Weight of the last chi (tip)
tip_weight = 2

# The weight decreases linearly from the base to the tip
# Calculate the weight of each chi
e = base_weight
d = base_weight - Fraction(base_weight - tip_weight, total_length - 1) * 1
c = base_weight - Fraction(base_weight - tip_weight, total_length - 1) * 2
b = base_weight - Fraction(base_weight - tip_weight, total_length - 1) * 3
a = tip_weight

# Results:
# e: weight of the first chi
# d: weight of the second chi
# c: weight of the third chi
# b: weight of the fourth chi
# a: weight of the fifth chi#----- content ends here -----

"""
"""
