"""
假令有粟二萬三千一百二十斛七斗三升，欲作方倉一，圓窖一，盛各滿中而粟適盡。令高、深等，使方面少於圓徑九寸，多於高二丈九尺八寸，率徑七，周二十二。問：方、徑、深多少？
答曰：倉方 a丈 ，窖徑 b丈 ，高與深各 c丈 。
"""

"""
This is a classic ancient Chinese math problem involving the calculation of the dimensions of a square granary and a circular granary, given specific conditions. Let's break it down and solve step by step.

---

### Problem Breakdown:
1. **Given:**
   - Total millet: `23120斛7斗3升`
   - Square granary (倉) and circular granary (窖) must each be filled completely.
   - The height (or depth) of both granaries is the same.
   - The side length of the square granary is 9 cun less than the diameter of the circular granary.
   - The side length of the square granary is 2丈9尺8寸 more than the height (or depth).
   - Use the approximation for π: \( \frac{22}{7} \).

2. **To Find:**
   - Side length of the square granary (`a` 丈),
   - Diameter of the circular granary (`b` 丈),
   - Height (or depth) of both granaries (`c` 丈).

3. **Conversions:**
   - 1斛 = 10斗
   - 1斗 = 10升
   - 1丈 = 10尺
   - 1尺 = 10寸

   Total millet in **升**:
   \[
   23120斛7斗3升 = 23120 \times 100 + 7 \times 10 + 3 = 2312073升
   \]

---

### Formulas:
1. Volume of the square granary:
   \[
   V_{\text{square}} = \text{side}^2 \times \text{height}
   \]

2. Volume of the circular granary:
   \[
   V_{\text{circle}} = \pi \times \left(\frac{\text{diameter}}{2}\right)^2 \times \text{height}
   \]

3. Total millet is split evenly:
   \[
   V_{\text{square}} = V_{\text{circle}} = \frac{2312073}{2}
   \]

4. Relationships:
   - \(\text{side} = \text{diameter} - 9寸\)
   - \(\text{side} = \text{height} + 2丈9尺8寸\)

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Total millet in 升
total_millet = 23120 * 100 + 7 * 10 + 3

# Millet in each granary
millet_per_granary = Fraction(total_millet, 2)

# Relationships and constants
pi = Fraction(22, 7)
height_to_side_offset = 2 * 10 + 9 + Fraction(8, 10)  # 2丈9尺8寸 in 尺
side_to_diameter_offset = Fraction(9, 10)  # 9寸 in 尺

# Solve for height, side, and diameter
# Volume of square granary: side^2 * height = millet_per_granary
# Volume of circular granary: pi * (diameter / 2)^2 * height = millet_per_granary
# side = diameter - side_to_diameter_offset
# side = height + height_to_side_offset

# Let height = c, side = a, diameter = b
# a = b - side_to_diameter_offset
# a = c + height_to_side_offset
# Substitute a into the volume equations

# Step 1: Express side (a) in terms of height (c)
def solve_granary():
    for c in range(1, 100):  # Iterate over possible heights (in 尺)
        c = Fraction(c)
        a = c + height_to_side_offset  # side in terms of height
        b = a + side_to_diameter_offset  # diameter in terms of side

        # Square granary volume
        square_volume = a**2 * c

        # Circular granary volume
        circular_volume = pi * (b / 2)**2 * c

        # Check if volumes match the millet per granary
        if square_volume == millet_per_granary and circular_volume == millet_per_granary:
            return a / 10, b / 10, c / 10  # Convert from 尺 to 丈

# Solve and print the results
a, b, c = solve_granary()
print(f"倉方 a = {a}丈")
print(f"窖徑 b = {b}丈")
print(f"高與深各 c = {c}丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. Convert all measurements into a consistent unit (e.g., 尺).
2. Use the relationships between side, diameter, and height to express all variables in terms of height.
3. Iterate over possible values for height (`c`) and calculate the corresponding side (`a`) and diameter (`b`).
4. Check if the calculated volumes match the given millet volume for each granary.
5. Convert the results back to 丈 for the final answer.

---

### Final Answer:
The Python code will output the values of:
- \( a \): side length of the square granary in 丈,
- \( b \): diameter of the circular granary in 丈,
- \( c \): height (or depth) of both granaries in 丈.
"""


"""
Code error: cannot unpack non-iterable NoneType object"""
