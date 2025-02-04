"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex ancient Chinese math problem involving the calculation of shared labor and geometric dimensions. Let's break it down and translate it into Python code step by step, following the procedure ("術") provided.

### Problem Description:
There is a roof-like structure (芻甍) with the following dimensions:
- Top length (上袤): 3 zhang
- Bottom length (下袤): 9 zhang
- Width (廣): 6 zhang
- Height (高): 12 zhang

Two counties, 甲縣 and 乙縣, are tasked with constructing it:
- 甲縣 has 632 people.
- 乙縣 has 243 people.

Each person can complete 36 cubic chi of work per day, and the construction is limited to 8 days. The two counties will work together, but 甲縣 arrives first.

The task is to calculate how much height (高), width (廣), and length (袤) 甲縣 should complete based on their share of the workload.

---

### Procedure:
1. **Calculate the total workload for 乙縣:**
   - Multiply the daily work rate (36 chi³) by the number of people in 乙縣 (243) and the number of days (8).
   - This gives the total cubic chi of work for 乙縣.

2. **Calculate the corresponding volume for 乙縣:**
   - Multiply the total workload by 6 (width), then by the square of the height (高²), and then by the difference in lengths (袤差 = 下袤 - 上袤).
   - Divide the result by 2 to get the actual volume.

3. **Calculate the height completed by 乙縣:**
   - Multiply the height (高) by the top length (上袤), then divide by the difference in lengths (袤差).
   - Multiply the result by 3 and divide by 2 to get the "廉法" (a proportional factor).
   - Take the cube root of the previous result to find the height completed by 乙縣 (乙高).

4. **Calculate the height completed by 甲縣:**
   - Subtract 乙高 from the total height (高) to get 甲高.

5. **Calculate the width and length for 甲縣:**
   - Use the proportional relationship to calculate the width (廣) and length (袤) for 甲縣.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
上袤 = 3  # Top length in zhang
下袤 = 9  # Bottom length in zhang
廣 = 6    # Width in zhang
高 = 12   # Height in zhang
甲縣人數 = 632
乙縣人數 = 243
每日人功 = 36  # Daily work rate in cubic chi
限日 = 8       # Days of work

# Step 1: Calculate total workload for 乙縣
乙積尺 = 每日人功 * 乙縣人數 * 限日

# Step 2: Calculate the corresponding volume for 乙縣
袤差 = 下袤 - 上袤
實 = Fraction(乙積尺 * 6 * 高**2 * 袤差, 2)

# Step 3: Calculate the height completed by 乙縣
上袤之高 = Fraction(高 * 上袤, 袤差)
廉法 = Fraction(3 * 上袤之高, 2)
乙高 = pow(實 / 廉法, Fraction(1, 3))  # Cube root

# Step 4: Calculate the height completed by 甲縣
甲高 = 高 - 乙高

# Step 5: Calculate the width and length for 甲縣
甲廣 = Fraction(甲高 * 廣, 高)
甲袤 = Fraction(甲高 * 袤差, 高) + 上袤

# Final answers
a = 甲高
b = 甲廣
c = 甲袤

print(f"高 a = {a} 丈")
print(f"上廣 b = {b} 丈")
print(f"袤 c = {c} 丈")
#----- content ends here -----


"""


---

### Explanation of Variables:
- `乙積尺`: Total cubic chi of work completed by 乙縣.
- `袤差`: Difference between the bottom and top lengths.
- `實`: The actual volume corresponding to 乙縣's workload.
- `上袤之高`: A proportional factor based on the top length and height.
- `廉法`: Another proportional factor used to calculate the height.
- `乙高`: Height completed by 乙縣.
- `甲高`: Height completed by 甲縣.
- `甲廣`: Width completed by 甲縣.
- `甲袤`: Length completed by 甲縣.

This code follows the procedure step by step and calculates the required dimensions for 甲縣.
"""


"""
Code error: both arguments should be Rational instances"""
