"""
今有二人同所立。甲行率七，乙行率三。乙東行。甲南行十步而邪東北與乙會。問︰甲乙行各幾何？
術曰：令七自乘，三亦自乘，并而半之，以為甲邪行率。邪行率減於七自乘，餘為南行率。以三乘七為乙東行率。置南行十步，以甲邪行率乘之，副置十步，以乙東行率乘之，各自為實。實如南行率而一，各得行數。
荅曰：乙東行 a步 ；甲邪行 b步 及之。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
rate_甲 = 7  # Rate of 甲行
rate_乙 = 3  # Rate of 乙行
南行_甲 = 10  # 甲南行 10 steps

# Step 1: Calculate 甲邪行率
甲邪行率 = Fraction(rate_甲**2 + rate_乙**2, 2)

# Step 2: Calculate 甲南行率
甲南行率 = rate_甲**2 - 甲邪行率

# Step 3: Calculate 乙東行率
乙東行率 = rate_甲 * rate_乙

# Step 4: Calculate the actual distances
# For 甲邪行
甲邪行 = Fraction(南行_甲 * 甲邪行率, 甲南行率)

# For 乙東行
乙東行 = Fraction(南行_甲 * 乙東行率, 甲南行率)

# Results
a = 乙東行  # 乙東行 a步
b = 甲邪行  # 甲邪行 b步

# Output the results
a, b


"""


This code calculates the values of `a` (乙東行) and `b` (甲邪行) using the given rates and steps. The results are stored in the variables `a` and `b`.
"""


"""
"""
