"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the steps taken by two individuals,甲 (a) and乙 (c), based on their walking rates and directions. Here is the Python code:


"""


from fractions import Fraction

# Given data
side_length = 10  # The side length of the square city in li
rate_甲 = 5  # Rate of 甲 (steps per unit time)
rate_乙 = 3  # Rate of 乙 (steps per unit time)

# Calculations
rate_diagonal = Fraction(rate_甲**2 + rate_乙**2, 2)  # Diagonal walking rate
rate_south = rate_甲**2 - rate_diagonal  # Southward walking rate
rate_east = rate_乙 * rate_甲  # Eastward walking rate

half_side = Fraction(side_length, 2)  # Half of the side length of the city
a = Fraction(half_side * rate_south, rate_east + rate_south)  # Steps southward by 甲
b = a * rate_diagonal / rate_south  # Diagonal steps by 甲
c = a * rate_east / rate_south  # Eastward steps by 乙

# Results
a, b, c


"""


### Explanation:
1. **rate_diagonal**: The diagonal walking rate is calculated as the average of the squares of the rates of甲 and乙.
2. **rate_south**: The southward walking rate is derived by subtracting the diagonal walking rate from the square of甲's rate.
3. **rate_east**: The eastward walking rate is the product of the rates of甲 and乙.
4. **a**: The southward steps taken by甲 are calculated using the half side length of the city and the rates.
5. **b**: The diagonal steps taken by甲 are proportional to the southward steps and the diagonal rate.
6. **c**: The eastward steps taken by乙 are proportional to the southward steps of甲 and the eastward rate.

The variables `a`, `b`, and `c` represent the steps taken by甲 southward,甲 diagonally, and乙 eastward, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 800, Actual: 40/23
Variable 'b' has wrong value. Expected: 9775/2, Actual: 85/23
Variable 'c' has wrong value. Expected: 8625/2, Actual: 75/23"""
