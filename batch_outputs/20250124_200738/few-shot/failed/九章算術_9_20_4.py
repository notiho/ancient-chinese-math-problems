"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with sides of 10 li, and each side has a gate in the middle.
Person A and Person B both start from the center of the city.
Person B exits through the east gate, while Person A exits through the south gate.
After exiting, Person A moves diagonally northeast along the city boundary and meets Person B.
The rates of movement are such that Person A walks 5 units while Person B walks 3 units in the same time.
Question: How far do Person A and Person B walk respectively?

The procedure says:
1. Square 5 (Person A's rate) and square 3 (Person B's rate), add them together, and halve the result to get the diagonal movement rate.
2. Subtract the diagonal movement rate from the square of 5 to get the southward movement rate.
3. Multiply 3 by 5 to get the eastward movement rate.
4. Take half the side length of the city and multiply it by the southward movement rate. Divide the result by the eastward movement rate to get the number of steps Person A takes to exit the south gate.
5. Add this result to half the side length of the city to get the total southward movement of Person A.
6. To find the diagonal movement, multiply the southward movement by the diagonal movement rate.
7. To find the eastward movement of Person B, multiply the southward movement by the eastward movement rate.
8. Divide each result by the southward movement rate to get the respective distances.

Answer: Person A exits the south gate and walks *a* steps south, then *b* steps diagonally northeast to meet Person B. Person B walks *c* steps east.
"""

from fractions import Fraction

# Rates of movement
甲速 = 5  # Person A's rate
乙速 = 3  # Person B's rate

# City dimensions
邑方 = 10  # Side length of the city in li
邑方半 = Fraction(邑方, 2)  # Half the side length

# Step 1: Calculate the diagonal movement rate
甲速平方 = 甲速 ** 2
乙速平方 = 乙速 ** 2
邪行率 = Fraction(甲速平方 +乙速平方, 2)

# Step 2: Calculate the southward movement rate
南行率 = 甲速平方 - 邪行率

# Step 3: Calculate the eastward movement rate
東行率 = 乙速 * 甲速

# Step 4: Calculate the steps Person A takes to exit the south gate
南門步數 = Fraction(邑方半 * 南行率, 東行率)

# Step 5: Calculate the total southward movement of Person A
南行 = 南門步數 + 邑方半

# Step 6: Calculate the diagonal movement of Person A
邪行 = Fraction(南行 * 邪行率, 南行率)

# Step 7: Calculate the eastward movement of Person B
東行 = Fraction(南行 * 東行率, 南行率)

# Final results
a = 南行
b = 邪行
c = 東行#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 800, Actual: 23/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: 391/24
Variable 'c' has wrong value. Expected: 8625/2, Actual: 115/8"""
