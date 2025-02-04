"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The solution involves calculating the steps taken by two individuals, "甲" (a) and "乙" (c), based on their respective rates and directions. The problem also involves a diagonal path (b) that connects their meeting point. Here's the Python code:


"""


from fractions import Fraction

# Given data
side_length = 10  # The side length of the square city (in li)
rate_甲 = 5  # Rate of 甲 (steps per unit time)
rate_乙 = 3  # Rate of 乙 (steps per unit time)

# Step 1: Calculate the diagonal rate (邪行率)
rate_diagonal = Fraction(rate_甲**2 + rate_乙**2, 2)

# Step 2: Calculate the southward rate (南行率)
rate_south = rate_甲**2 - rate_diagonal

# Step 3: Calculate the eastward rate (乙東行率)
rate_east = rate_甲 * rate_乙

# Step 4: Calculate the southward distance (出南門步數)
half_side = Fraction(side_length, 2)
a = Fraction(half_side * rate_south, rate_east + rate_south)

# Step 5: Calculate the diagonal distance (邪東北行 b步)
b = a * rate_diagonal / rate_south

# Step 6: Calculate the eastward distance (乙東行 c步)
c = a * rate_east / rate_south

# Results
a  # 甲出南門步數 (steps south)
b  # 甲邪東北行步數 (diagonal steps)
c  # 乙東行步數 (steps east)


"""


### Explanation of the Variables
1. `a`: The number of steps 甲 takes southward to exit the south gate.
2. `b`: The diagonal distance 甲 travels northeast to meet 乙.
3. `c`: The number of steps 乙 takes eastward to meet 甲.

### Output
The variables `a`, `b`, and `c` will hold the respective distances in steps. You can print them to see the results.
"""


"""
Variable 'a' has wrong value. Expected: 800, Actual: 40/23
Variable 'b' has wrong value. Expected: 9775/2, Actual: 85/23
Variable 'c' has wrong value. Expected: 8625/2, Actual: 75/23"""
