"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
side_length = 10  # The side length of the square city in li
rate_甲 = 5  # Rate of 甲's movement
rate_乙 = 3  # Rate of 乙's movement

# Step 1: Calculate the diagonal movement rate (邪行率)
rate_diagonal = Fraction(rate_甲**2 + rate_乙**2, 2)

# Step 2: Calculate the southward movement rate (南行率)
rate_south = rate_甲**2 - rate_diagonal

# Step 3: Calculate the eastward movement rate (乙東行率)
rate_east = rate_甲 * rate_乙

# Step 4: Calculate the southward distance (出南門步數)
half_side = Fraction(side_length, 2)
a = Fraction(half_side * rate_south, rate_east + rate_south)

# Step 5: Calculate the diagonal distance (邪東北行 b步)
b = a * rate_diagonal / rate_south

# Step 6: Calculate the eastward distance (乙東行 c步)
c = a * rate_east / rate_south

# Results
a  # 甲出南門步數
b  # 甲邪東北行步數
c  # 乙東行步數
#----- content ends here -----


"""


### Explanation of the Code:
1. **Diagonal Movement Rate (邪行率)**: This is calculated as the average of the squares of the rates of 甲 and 乙.
2. **Southward Movement Rate (南行率)**: This is the difference between the square of 甲's rate and the diagonal movement rate.
3. **Eastward Movement Rate (乙東行率)**: This is the product of the rates of 甲 and 乙.
4. **Southward Distance (出南門步數)**: This is calculated using the formula provided in the problem, which involves the half-side length of the city and the movement rates.
5. **Diagonal Distance (邪東北行步數)**: This is proportional to the southward distance based on the diagonal movement rate.
6. **Eastward Distance (乙東行步數)**: This is proportional to the southward distance based on the eastward movement rate.

The variables `a`, `b`, and `c` represent the distances traveled by 甲 and 乙 as described in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 800, Actual: 40/23
Variable 'b' has wrong value. Expected: 9775/2, Actual: 85/23
Variable 'c' has wrong value. Expected: 8625/2, Actual: 75/23"""
