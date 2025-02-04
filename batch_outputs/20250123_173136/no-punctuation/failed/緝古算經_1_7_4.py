"""
假令芻甍上袤三丈下袤九丈廣六丈高一十二丈有甲縣六百三十二人乙縣二百四十三人夏程人功當積三十六尺限八日役自穿築二縣共造今甲縣先到問自下給高廣袤各多少
求甲縣均給積尺受廣袤術曰以程功乘乙縣人數又以限日乘之為積尺以六因之又高冪乘之又袤差乘廣而一所得又半之為實高乘上袤袤差而一為上袤之高三因上袤之高半之為廉法從開立方除之得乙高以減甍高余即甲高求廣袤依率求之
答曰高 a丈 上廣 b丈 袤 c丈 
"""

"""
This is a complex ancient Chinese mathematical problem involving labor distribution and geometric calculations. Let's break it down step by step and translate it into Python code.

### Problem Description:
There is a thatched roof with:
- Top length (袤) = 3 zhang
- Bottom length (袤) = 9 zhang
- Width (廣) = 6 zhang
- Height (高) = 12 zhang

Two counties, Jia (甲) and Yi (乙), are tasked with building it:
- Jia county has 632 people.
- Yi county has 243 people.

Each person can complete 36 cubic chi of work per day, and the task must be completed in 8 days. Jia county arrives first, and we need to calculate how much of the height, width, and length Jia county must complete.

### Procedure:
1. **Calculate Yi county's total work (積尺):**
   - Multiply the number of people in Yi county by their daily work rate and the number of days.
2. **Calculate the volume (積尺) Jia county must complete:**
   - Subtract Yi county's work from the total volume of the roof.
3. **Distribute the work to Jia county:**
   - Use geometric proportions to calculate the height, width, and length Jia county must complete.

---

### Python Code:


"""


from fractions import Fraction
from math import pow

# Roof dimensions
上袤 = 3  # Top length (in zhang)
下袤 = 9  # Bottom length (in zhang)
廣 = 6    # Width (in zhang)
高 = 12   # Height (in zhang)

# County populations
甲縣人數 = 632
乙縣人數 = 243

# Work rate and time
每日人功 = 36  # Cubic chi per person per day
限日 = 8       # Days

# Total roof volume (積尺)
積尺 = Fraction(廣 * 高 * (上袤 + 下袤) / 2 * 1000)  # Convert zhang^3 to chi^3

# Yi county's total work (乙縣積尺)
乙縣積尺 = 每日人功 * 乙縣人數 * 限日

# Jia county's required work (甲縣積尺)
甲縣積尺 = 積尺 - 乙縣積尺

# Calculate Jia county's height (甲高)
廉法 = Fraction(3 * (上袤 + 下袤) / 2)  # Average length
甲高 = pow(甲縣積尺 / (廣 * 廉法), 1/3)

# Calculate Jia county's width (甲廣)
甲廣 = 廣

# Calculate Jia county's length (甲袤)
甲袤 = Fraction(甲縣積尺 / (甲廣 * 甲高))

# Convert results to zhang
a = Fraction(甲高, 1000)  # Height in zhang
b = Fraction(甲廣, 1000)  # Width in zhang
c = Fraction(甲袤, 1000)  # Length in zhang

# Output results
print(f"高 a丈 = {a}")
print(f"上廣 b丈 = {b}")
print(f"袤 c丈 = {c}")


"""


---

### Explanation of the Code:
1. **Volume Calculation:**
   - The roof is a trapezoidal prism, so its volume is calculated as:
     \[
     V = \frac{(上袤 + 下袤)}{2} \times 廣 \times 高
     \]
   - The result is converted from zhang³ to chi³ by multiplying by 1000.

2. **Yi County's Work:**
   - Multiply the number of people in Yi county by their daily work rate and the number of days.

3. **Jia County's Work:**
   - Subtract Yi county's work from the total roof volume.

4. **Geometric Proportions:**
   - Jia county's height is calculated using the cubic root of the ratio of their work to the product of width and average length.
   - Width remains constant.
   - Length is calculated based on the remaining volume.

5. **Conversion to Zhang:**
   - Results are converted back to zhang for the final answer.

---

### Final Answer:
The code calculates:
- \( a \): Height (高) in zhang
- \( b \): Width (廣) in zhang
- \( c \): Length (袤) in zhang
"""


"""
Code error: both arguments should be Rational instances"""
