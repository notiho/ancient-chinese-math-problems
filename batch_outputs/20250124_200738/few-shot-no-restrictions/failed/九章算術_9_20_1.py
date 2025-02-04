"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
This problem involves two people,甲 (Jia) and 乙 (Yi), starting from the center of a square city with a side length of 10 li. Jia exits through the south gate and then walks diagonally northeast along the city boundary, meeting Yi, who exits through the east gate and walks east. Jia's walking rate is 5, and Yi's walking rate is 3. The goal is to determine how far Jia walks south, how far Jia walks diagonally northeast, and how far Yi walks east.

### Translation of the procedure:
1. Square the rates of Jia and Yi (5 and 3, respectively), sum them, and halve the result to find the diagonal walking rate (邪行率).
2. Subtract the diagonal walking rate from the square of Jia's rate (5²) to find the southward walking rate (南行率).
3. Multiply the rates of Jia and Yi (5 × 3) to find Yi's eastward walking rate (乙東行率).
4. Halve the side length of the city (10 li) to find half the side length (邑方半).
5. Multiply the southward walking rate by half the side length, divide by the eastward walking rate, and solve for Jia's southward walking distance (出南門步數).
6. Add the result to half the side length to find Jia's total southward walking distance (南行).
7. To find the diagonal distance (邪東北行), multiply the diagonal walking rate by the southward walking distance.
8. To find Yi's eastward walking distance, multiply the eastward walking rate by the southward walking distance.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Rates of Jia and Yi
甲率 = 5  # Jia's rate
乙率 = 3  # Yi's rate

# Square the rates
甲率平方 = 甲率 ** 2
乙率平方 = 乙率 ** 2

# Step 1: Calculate the diagonal walking rate (邪行率)
邪行率 = Fraction(甲率平方 + 乙率平方, 2)

# Step 2: Calculate the southward walking rate (南行率)
南行率 = 甲率平方 - 邪行率

# Step 3: Calculate Yi's eastward walking rate (乙東行率)
乙東行率 = 甲率 * 乙率

# Step 4: Halve the side length of the city (邑方半)
邑方 = 10  # Side length of the city in li
邑方半 = Fraction(邑方, 2)

# Step 5: Calculate Jia's southward walking distance (出南門步數)
出南門步數 = Fraction(南行率 * 邑方半, 乙東行率)

# Step 6: Calculate Jia's total southward walking distance (南行)
南行 = 出南門步數 + 邑方半

# Step 7: Calculate Jia's diagonal walking distance (邪東北行)
邪東北行 = 邪行率 * 出南門步數

# Step 8: Calculate Yi's eastward walking distance (乙東行)
乙東行 = 乙東行率 * 出南門步數

# Results
a = 南行
b = 邪東北行
c = 乙東行

print(f"甲出南門 {a} 步，邪東北行 {b} 步，及乙。乙東行 {c} 步。")
#----- content ends here -----


"""


### Explanation of Results:
- `a`: Jia's total southward walking distance.
- `b`: Jia's diagonal walking distance northeast.
- `c`: Yi's eastward walking distance.

This code calculates the exact distances for Jia and Yi based on the given rates and city dimensions.
"""


"""
Variable 'a' has wrong value. Expected: 800, Actual: 23/3
Variable 'b' has wrong value. Expected: 9775/2, Actual: 136/3
Variable 'c' has wrong value. Expected: 8625/2, Actual: 40"""
