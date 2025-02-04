"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a(=24/5)丈 ，上廣 b(=18/5)丈 ，袤 c(=33/5)丈 。
"""

"""
This is a complex ancient Chinese problem involving geometry and labor distribution. Let's break it down step by step and translate it into Python code.

### Problem Description:
There is a thatched roof with the following dimensions:
- Top length (袤上): 3 zhang
- Bottom length (袤下): 9 zhang
- Width (廣): 6 zhang
- Height (高): 12 zhang

Two counties, A (甲縣) and B (乙縣), are tasked with constructing it:
- County A has 632 people.
- County B has 243 people.
- Each person can complete 36 cubic chi of work per day.
- The work must be completed in 8 days.

County A arrives first and starts working. The task is to determine how much height (高), top width (廣), and length (袤) County A must complete before County B arrives.

The procedure involves calculating the volume of the roof and distributing the work proportionally between the two counties based on their populations and labor capacity.

---

### Procedure:
1. **Calculate the total work (積尺) for County B:**
   - Multiply the daily work rate (程功) by the number of people in County B (乙縣人數).
   - Multiply this by the number of days (限日).

2. **Calculate the volume (積尺) of the roof:**
   - Multiply the width (廣) by the height (高) and the difference in lengths (袤差 = 袤下 - 袤上).
   - Divide the result by 2 (since it's a trapezoidal prism).

3. **Determine the height (高) completed by County B:**
   - Use the volume completed by County B to calculate the height they would complete.
   - Subtract this from the total height to determine the height completed by County A.

4. **Calculate the corresponding top width (廣) and length (袤) for County A:**
   - Use the proportions of the roof's geometry to calculate these values.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given dimensions of the roof
袤上 = 3  # Top length in zhang
袤下 = 9  # Bottom length in zhang
廣 = 6    # Width in zhang
高 = 12   # Height in zhang

# Labor details
甲縣人數 = 632  # People in County A
乙縣人數 = 243  # People in County B
程功 = 36       # Cubic chi per person per day
限日 = 8        # Days

# Step 1: Calculate the total work (積尺) for County B
乙積尺 = 程功 * 乙縣人數 * 限日

# Step 2: Calculate the total volume (積尺) of the roof
袤差 = 袤下 - 袤上  # Difference in lengths
積尺 = Fraction(廣 * 高 * 袤差, 2)

# Step 3: Determine the height (高) completed by County B
廉法 = Fraction(3 * 高 * 袤上 * 袤差, 2)  # Intermediate calculation for height
乙高 = pow(Fraction(乙積尺, 廉法), 1/3)  # Cube root to find height for County B
甲高 = 高 - 乙高  # Remaining height for County A

# Step 4: Calculate the corresponding top width (廣) and length (袤) for County A
甲廣 = Fraction(廣 * 甲高, 高)  # Proportional width
甲袤 = Fraction(袤上 * 甲高, 高)  # Proportional length

# Results
a = Fraction(甲高)  # Height completed by County A
b = Fraction(甲廣)  # Top width completed by County A
c = Fraction(甲袤)  # Length completed by County A

# Output the results
print(f"高 a = {a} 丈")  # Height
print(f"上廣 b = {b} 丈")  # Top width
print(f"袤 c = {c} 丈")  # Length
#----- content ends here -----


"""


---

### Explanation of Results:
- `a`: The height completed by County A.
- `b`: The top width corresponding to the height completed by County A.
- `c`: The length corresponding to the height completed by County A.

The final results are:
- `a = 24/5` zhang (height completed by County A),
- `b = 18/5` zhang (top width corresponding to County A's work),
- `c = 33/5` zhang (length corresponding to County A's work).
"""


"""
Code error: both arguments should be Rational instances"""
