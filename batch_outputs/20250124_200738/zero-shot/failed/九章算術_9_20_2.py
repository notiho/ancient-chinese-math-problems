"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
To solve the problem, let's translate the ancient Chinese math problem into Python code. We'll use the `Fraction` class from the `fractions` module to handle numbers that might not be integers.

### Problem Breakdown:
1. The city is square-shaped with a side length of 10 li (里).
2. Both individuals start from the center of the city.
3. Person 甲 (A) moves south to the southern gate, then moves diagonally northeast.
4. Person 乙 (B) moves east directly.
5. The ratio of their speeds is given: 甲 moves 5 units while 乙 moves 3 units in the same time.
6. We need to calculate:
   - `a`: The distance 甲 moves south to the southern gate.
   - `b`: The diagonal distance 甲 moves northeast.
   - `c`: The distance 乙 moves east.

### Solution:

"""

#----- content starts here -----

from fractions import Fraction

# Given data
city_side = 10  # side length of the square city in li
speed_ratio_甲 = 5  # 甲's speed ratio
speed_ratio_乙 = 3  # 乙's speed ratio

# Step 1: Calculate the diagonal (斜行率) rate
斜行率 = Fraction(speed_ratio_甲**2 + speed_ratio_乙**2, 2)

# Step 2: Calculate the southward (南行率) rate for 甲
南行率 = Fraction(speed_ratio_甲**2 - 斜行率)

# Step 3: Calculate the eastward (東行率) rate for 乙
東行率 = Fraction(speed_ratio_甲 * speed_ratio_乙)

# Step 4: Calculate the distance 甲 moves south to the southern gate (a)
half_city_side = Fraction(city_side, 2)
a = Fraction(half_city_side * 南行率, 東行率 + 南行率)

# Step 5: Calculate the diagonal distance 甲 moves northeast (b)
b = a * 斜行率

# Step 6: Calculate the distance 乙 moves east (c)
c = a * 東行率

# Results
a = float(a)  # Distance 甲 moves south to the southern gate
b = float(b)  # Diagonal distance 甲 moves northeast
c = float(c)  # Distance 乙 moves east

# Output the results
a, b, c
#----- content ends here -----


"""


### Explanation of the Code:
1. **斜行率 (Diagonal Rate)**: This is calculated as the average of the squares of the speed ratios of 甲 and 乙.
2. **南行率 (Southward Rate)**: This is the difference between the square of 甲's speed ratio and the diagonal rate.
3. **東行率 (Eastward Rate)**: This is the product of the speed ratios of 甲 and 乙.
4. **Distance Calculations**:
   - The distance 甲 moves south (`a`) is calculated using the formula derived from the problem.
   - The diagonal distance 甲 moves northeast (`b`) is proportional to the diagonal rate.
   - The distance 乙 moves east (`c`) is proportional to the eastward rate.

### Results:
The variables `a`, `b`, and `c` will contain the respective distances in li (里).
"""


"""
Variable 'a' has wrong value. Expected: 800, Actual: 1.7391304347826086
Variable 'b' has wrong value. Expected: 9775/2, Actual: 29.565217391304348
Variable 'c' has wrong value. Expected: 8625/2, Actual: 26.08695652173913"""
