"""
假令有粟三千七十二石，欲作方倉一、圓窖一，令徑與方等，方於窖深二尺，少於倉高三尺，盛各滿中而粟適盡。問：方、徑、高、深各多少？
答曰：方徑各 a丈 ，高 b丈 ，深 c丈 。
"""

"""
This is a classic ancient Chinese mathematical problem involving the relationship between the volume of a square granary and a round granary. Let's break it down step by step and solve it.

---

### Problem Breakdown:
1. **Given:**
   - Total millet: 3072 石 (shi).
   - A square granary and a round granary are to be constructed.
   - The diameter of the round granary is equal to the side length of the square granary.
   - The depth of the round granary is 2 chi (尺) less than the height of the square granary.
   - The height of the square granary is 3 chi (尺) less than the side length of the square granary.
   - Both granaries are filled to capacity, and the total millet is exactly used up.

2. **To Find:**
   - The side length of the square granary (方, `a` 丈).
   - The diameter of the round granary (徑, `a` 丈).
   - The height of the square granary (高, `b` 丈).
   - The depth of the round granary (深, `c` 丈).

3. **Conversions:**
   - 1 丈 = 10 尺.
   - Volumes are calculated in cubic 尺.

4. **Formulas:**
   - Volume of the square granary:
     \[
     V_{\text{square}} = \text{side}^2 \times \text{height}
     \]
   - Volume of the round granary:
     \[
     V_{\text{round}} = \frac{\pi}{4} \times \text{diameter}^2 \times \text{depth}
     \]
   - Total millet:
     \[
     V_{\text{square}} + V_{\text{round}} = 3072 \times 1000 \, (\text{convert 石 to cubic 尺})
     \]

5. **Relationships:**
   - Diameter of the round granary = Side of the square granary.
   - Depth of the round granary = Height of the square granary - 2 尺.
   - Height of the square granary = Side of the square granary - 3 尺.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Total millet in cubic chi
total_volume = 3072 * 1000  # Convert 石 to cubic 尺

# Let the side length of the square granary (and diameter of the round granary) be 'a' 丈
# Convert to 尺 for calculations
a = Fraction(1)  # Start with an initial guess (1 丈 = 10 尺)

# Relationships:
# Height of the square granary = a - 3 尺
# Depth of the round granary = a - 3 - 2 = a - 5 尺

# Volume formulas:
# Square granary volume: a^2 * (a - 3)
# Round granary volume: (π / 4) * a^2 * (a - 5)

# Solve for a such that the total volume matches
while True:
    # Calculate volumes
    square_volume = a**2 * (a - 3)
    round_volume = (math.pi / 4) * (a**2) * (a - 5)
    total = square_volume + round_volume
    
    # Check if the total matches the given total volume
    if abs(total - total_volume) < 1:  # Allow small error due to π approximation
        break
    
    # Increment 'a' by a small fraction (e.g., 1/10 尺)
    a += Fraction(1, 10)

# Calculate the final values
side_length = a / 10  # Convert back to 丈
height = (a - 3) / 10  # Convert back to 丈
depth = (a - 5) / 10  # Convert back to 丈

# Output the results
print(f"方徑各 {side_length} 丈")
print(f"高 {height} 丈")
print(f"深 {depth} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We start with an initial guess for the side length (`a`) of the square granary.
2. Using the relationships provided in the problem, we calculate the height of the square granary and the depth of the round granary.
3. We compute the volumes of both granaries and check if their sum matches the total millet volume.
4. If not, we increment `a` slightly and repeat the calculation until the total volume matches.
5. Finally, we convert the results back to 丈 for the answer.

---

### Final Answer:
After running the code, the results will be:

- 方徑各 `a` 丈.
- 高 `b` 丈.
- 深 `c` 丈.


"""


"""
Timed out"""
