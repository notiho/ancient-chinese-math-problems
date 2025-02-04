"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex problem involving the division of labor between two counties (甲縣 and 乙縣) to construct a roof structure with specified dimensions. The problem involves calculating how much of the structure each county is responsible for, based on their respective populations and the work rate per person. Let's break this down step by step and encode it in Python.

---

### Problem Breakdown:
1. **Given Dimensions of the Roof:**
   - Top length (上袤): 3 丈
   - Bottom length (下袤): 9 丈
   - Width (廣): 6 丈
   - Height (高): 12 丈

2. **Population of Counties:**
   - 甲縣: 632 people
   - 乙縣: 243 people

3. **Work Rate:**
   - Each person completes 36 cubic chi (積尺) of work in 8 days.

4. **Objective:**
   - Determine how much height (高), width (廣), and length (袤) 甲縣 is responsible for.

5. **Procedure:**
   - Use the given formula to calculate the volume of work (積尺) for 乙縣.
   - Use the relationship between the roof dimensions and the work volume to calculate the height, width, and length for 甲縣.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given dimensions of the roof (in 丈)
上袤 = 3
下袤 = 9
廣 = 6
高 = 12

# Population of the counties
甲縣人口 = 632
乙縣人口 = 243

# Work rate (積尺 per person in 8 days)
程功 = 36
限日 = 8

# Step 1: Calculate the total work volume (積尺) for 乙縣
乙積尺 = 程功 * 乙縣人口 * 限日

# Step 2: Calculate the "實" (intermediate value for volume distribution)
袤差 = 下袤 - 上袤
實 = Fraction(乙積尺 * 6 * 高**2 * 袤差 * 廣, 2)

# Step 3: Calculate the height for 乙縣 (乙高)
上袤之高 = Fraction(高 * 上袤 * 袤差, 1)
廉法 = Fraction(3 * 上袤之高, 2)
乙高 = pow(Fraction(實, 廉法), 1/3)

# Step 4: Calculate the height for 甲縣 (甲高)
甲高 = 高 - 乙高

# Step 5: Calculate the width (廣) and length (袤) for 甲縣
甲廣 = Fraction(廣 * 甲高, 高)
甲袤 = Fraction(袤差 * 甲高, 高) + 上袤

# Final Results
a = 甲高
b = 甲廣
c = 甲袤

# Output the results
print(f"高 a = {a} 丈")
print(f"上廣 b = {b} 丈")
print(f"袤 c = {c} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Step 1:** Calculate the total work volume (積尺) for 乙縣 based on its population, work rate, and time limit.
2. **Step 2:** Use the given formula to calculate the intermediate value "實," which is based on the roof's dimensions and the work volume.
3. **Step 3:** Solve for the height (乙高) that 乙縣 is responsible for using the cubic root formula.
4. **Step 4:** Subtract 乙高 from the total height (高) to get the height (甲高) that 甲縣 is responsible for.
5. **Step 5:** Use the proportional relationships to calculate the width (廣) and length (袤) for 甲縣.

---

### Output:
The code will output the following:
- `高 a`: The height (in 丈) that 甲縣 is responsible for.
- `上廣 b`: The width (in 丈) that 甲縣 is responsible for.
- `袤 c`: The length (in 丈) that 甲縣 is responsible for.

This approach ensures that the calculations follow the ancient Chinese mathematical procedure described in the problem.
"""


"""
Code error: both arguments should be Rational instances"""
