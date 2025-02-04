"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
This is a classic ancient Chinese problem involving geometry and relative motion. Let's break it down and translate the procedure into Python code.

### Problem Description:
- There is a square city with sides of 10 li (里), and gates are located at the middle of each side.
- Two people, A (甲) and B (乙), start from the center of the city.
  - B exits through the east gate.
  - A exits through the south gate but then moves diagonally northeast along the city's boundary until meeting B.
- The walking rates are:
  - A walks 5 units of distance for every 3 units walked by B.
- The task is to calculate:
  1. The distance A walks south to exit the south gate.
  2. The diagonal distance A walks northeast to meet B.
  3. The distance B walks east.

---

### Procedure:
1. **Define the walking rates**:
   - A's rate: 5
   - B's rate: 3

2. **Calculate the diagonal walking rate**:
   - \( \text{Diagonal rate} = \sqrt{5^2 + 3^2} / 2 = \frac{\sqrt{34}}{2} \)

3. **Calculate the southward walking rate**:
   - \( \text{South rate} = 5^2 - \text{Diagonal rate}^2 \)

4. **Calculate the eastward walking rate**:
   - \( \text{East rate} = 3 \times 5 \)

5. **Solve for the distances**:
   - Use the dimensions of the city (10 li) to calculate the distances walked by A and B.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# City dimensions
邑方 = 10  # li
邑方半 = Fraction(邑方, 2)  # Half the city's side length

# Walking rates
甲率 = 5
乙率 = 3

# Step 1: Calculate diagonal walking rate
邪行率 = Fraction(sqrt(甲率**2 + 乙率**2), 2)

# Step 2: Calculate southward walking rate
南行率 = Fraction(甲率**2, 1) - Fraction(邪行率**2, 1)

# Step 3: Calculate eastward walking rate
東行率 = 乙率 * 甲率

# Step 4: Solve for distances
# Southward distance (甲出南門步數)
南行步數 = (邑方半 * 南行率) / 東行率

# Diagonal distance (甲邪東北行步數)
邪東北行步數 = 南行步數 *邪#----- content ends here -----


"""

"""


"""
Code error: both arguments should be Rational instances"""
