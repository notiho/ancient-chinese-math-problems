"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
術曰：令七自乘，三亦自乘，并而半之，以為甲邪行率。邪行率減於七自乘，餘為南行率。以三乘七為乙東行率。置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實。實如南行率而一，各得行數。
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
south_steps = 10  #甲南行十步
rate_甲 = 7  #甲行率七
rate_乙 = 3  #乙行率三

# Calculations
rate_甲邪 = Fraction(rate_甲**2 + rate_乙**2, 2)  #甲邪行率
rate_甲南 = rate_甲**2 - rate_甲邪  #甲南行率
rate_乙東 = rate_甲 * rate_乙  #乙東行率

# Compute the distances
a = Fraction(south_steps * rate_乙東, rate_甲南)  #乙東行 a步
b = Fraction(south_steps * rate_甲邪, rate_甲南)  #甲邪行 b步

# Results
a, b
#----- content ends here -----


"""


This code computes the values of `a` (乙東行步數) and `b` (甲邪行步數) using the given rates and relationships described in the problem. The results will be stored in variables `a` and `b`.
"""


"""
"""
