"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the division of labor between two counties to construct a roof structure. Let's break it down step by step and translate it into Python code.

### Problem Description:
A roof structure has the following dimensions:
- Top length (上袤): 3 zhang
- Bottom length (下袤): 9 zhang
- Width (廣): 6 zhang
- Height (高): 12 zhang

There are two counties:
- County A (甲縣): 632 people
- County B (乙縣): 243 people

The work rate is:
- Each person completes 36 cubic chi of work per day.
- The total work must be completed in 8 days.

County A arrives first and starts working. The task is to determine how much height, width, and length County A should complete before County B arrives.

---

### Procedure:
1. **Calculate the total volume of the roof structure**:
   The roof is a trapezoidal prism, so its volume is calculated using the formula:
   \[
   V = \frac{1}{2} \times 高 \times (上袤 + 下袤) \times 廣
   \]

2. **Calculate the total work capacity of County B**:
   Multiply the work rate (36 cubic chi per person per day) by the number of people in County B and the number of days.

3. **Determine the portion of the roof volume County B will complete**:
   Using the total work capacity of County B, calculate the volume they will complete.

4. **Determine the height County B will complete**:
   Using the proportion of the volume County B will complete, calculate the height they will work on.

5. **Determine the remaining height for County A**:
   Subtract the height completed by County B from the total height to find the height County A will complete.

6. **Determine the width and length for County A**:
   Using the height completed by County A, calculate the corresponding width and length.

---

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction
import math

# Roof dimensions
上袤 = 3  # Top length in zhang
下袤 = 9  # Bottom length in zhang
廣 = 6    # Width in zhang
高 = 12   # Height in zhang

# County populations
甲縣人數 = 632
乙縣人數 = 243

# Work rate and time
人功 = 36  # Cubic chi per person per day
限日 = 8   # Days

# Step 1: Calculate the total volume of the roof (in cubic zhang)
總積 = Fraction(1, 2) * 高 * (上袤 + 下袤) * 廣

# Step 2: Calculate the total work capacity of County B (in cubic chi)
乙縣積尺 = 人功 * 乙縣人數 * 限日

# Step 3: Convert County B's work capacity to cubic zhang
乙縣積丈 = Fraction(乙縣積尺, 1000)  # 1 cubic zhang = 1000 cubic chi

# Step 4: Determine the height County B will complete
# Volume of a trapezoidal prism: V = (1/2) * 高 * (上袤 + 下袤) * 廣
# Solve for 高 (乙高):
廉法 = Fraction(1, 2) * 廣 * (上袤 + 下袤)  # Constant factor for the trapezoidal prism
乙高 = Fraction(乙縣積丈, 廉法)

# Step 5: Determine the remaining height for County A
甲高 = 高 - 乙高

# Step 6: Determine the corresponding width and length for County A
# For a trapezoidal prism, the width and length are proportional to the height
甲上袤 = 上袤 + (下袤 - 上袤) * Fraction(甲高, 高)
甲廣 = 廣  # The width remains constant

# Convert results to decimals for clarity
a = float(甲高)  # Height completed by County A
b = float(甲廣)  # Width completed by County A
c = float(甲上袤)  # Length completed by County A

# Output the results
print(f"高 a丈 = {a:.2f}")
print(f"上廣 b丈 = {b:.2f}")
print(f"袤 c丈 = {c:.2f}")
#----- content ends here -----


"""


---

### Explanation of Results:
- `a`: The height (in zhang) completed by County A before County B arrives.
- `b`: The width (in zhang) corresponding to the portion completed by County A.
- `c`: The length (in zhang) corresponding to the portion completed by County A.

This code follows the procedure described in the problem and uses the `Fraction` class to ensure accuracy in calculations involving fractions.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: 10.056
Variable 'b' has wrong value. Expected: 18/5, Actual: 6.0
Variable 'c' has wrong value. Expected: 33/5, Actual: 8.028"""
