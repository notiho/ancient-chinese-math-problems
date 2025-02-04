"""
今有邑方十里，各中開門。甲乙俱從邑中央而出。乙東出；甲南出，出門不知步數，邪向東北磨邑，適與乙會。率甲行五，乙行三。問︰甲、乙行各幾何？
術曰：令五自乘，三亦自乘，并而半之，為邪行率。邪行率減於五自乘者，餘，為南行率。以三乘五，為乙東行率。置邑方半之，以南行率乘之，如東行率而一，即得出南門步數。以增邑方半，即南行。置南行步求弦者，以邪行率乘之，求東者以東行率乘之，各自為實。實如南行率得一步。
荅曰：甲出南門 a步 ，邪東北行 b步 ，及乙。乙東行 c步 。
"""

"""
This is a classic ancient Chinese math problem involving geometry and relative motion. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
- There is a square city with sides of 10 li (里). Each side has a gate in the middle.
- Two people, A (甲) and B (乙), start from the center of the city and exit through different gates:
  - B exits through the east gate.
  - A exits through the south gate but does not know how many steps it takes to reach the gate. After exiting, A moves diagonally northeast along the city boundary and meets B.
- The walking rates are:
  - A walks 5 steps for every 3 steps B walks.
- The task is to calculate:
  - How many steps A takes to exit the south gate (denoted as `a`).
  - How many steps A takes diagonally northeast to meet B (denoted as `b`).
  - How many steps B takes eastward to meet A (denoted as `c`).

---

### Procedure:
1. **Define the rates and city dimensions:**
   - A's rate: 5
   - B's rate: 3
   - City side length: 10 li (convert to steps if necessary).

2. **Calculate the diagonal (hypotenuse) rate:**
   - The diagonal rate is derived using the Pythagorean theorem:
     \[
     \text{Diagonal rate} = \sqrt{(5^2 + 3^2)} = \sqrt{34}
     \]

3. **Determine the southward steps (A's steps to exit the south gate):**
   - Use the relationship between the rates and the city dimensions.

4. **Calculate the diagonal steps (A's steps northeast):**
   - Use the diagonal rate and the southward steps.

5. **Calculate B's eastward steps:**
   - Use the relationship between A's diagonal steps and B's eastward steps.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Rates of A and B
rate_A = 5  # A's walking rate
rate_B = 3  # B's walking rate

# City dimensions
city_side = 10  # in li

# Step 1: Calculate the diagonal (hypotenuse) rate
diagonal_rate = sqrt(rate_A**2 + rate_B**2)

# Step 2: Calculate the southward steps (A's steps to exit the south gate)
# Half the city side is the distance from the center to the south gate
half_city_side = city_side / 2
south_rate = rate_A**2 - (diagonal_rate**2 / 2)
south_steps = Fraction(half_city_side, south_rate)

# Step 3: Calculate the diagonal steps (A's steps northeast)
diagonal_steps = south_steps * diagonal_rate

# Step 4: Calculate B's eastward steps
east_rate = rate_A * rate_B
east_steps = south_steps * east_rate

# Results
a = south_steps
b = diagonal_steps
c = east_steps

print(f"甲出南門 {a} 步，邪東北行 {b} 步，及乙。乙東行 {c} 步。")
#----- content ends here -----


"""


---

### Explanation of Results:
- `a`: The number of steps A takes to exit the south gate.
- `b`: The number of steps A takes diagonally northeast to meet B.
- `c`: The number of steps B takes eastward to meet A.

This code follows the ancient Chinese mathematical procedure and uses modern tools like the `math` module for square roots and `fractions.Fraction` for precise calculations.
"""


"""
Code error: both arguments should be Rational instances"""
