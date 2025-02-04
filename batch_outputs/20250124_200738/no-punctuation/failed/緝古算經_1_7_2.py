"""
假令芻甍上袤三丈下袤九丈廣六丈高一十二丈有甲縣六百三十二人乙縣二百四十三人夏程人功當積三十六尺限八日役自穿築二縣共造今甲縣先到問自下給高廣袤各多少
求甲縣均給積尺受廣袤術曰以程功乘乙縣人數又以限日乘之為積尺以六因之又高冪乘之又袤差乘廣而一所得又半之為實高乘上袤袤差而一為上袤之高三因上袤之高半之為廉法從開立方除之得乙高以減甍高余即甲高求廣袤依率求之
答曰高 a丈 上廣 b丈 袤 c丈 
"""

"""
This is a complex ancient Chinese problem involving the division of labor and geometry. Let's break it down and translate the procedure into Python code step by step.

### Problem Breakdown:
- A roof structure (芻甍) has dimensions: 
  - Top length (袤上) = 3 zhang
  - Bottom length (袤下) = 9 zhang
  - Width (廣) = 6 zhang
  - Height (高) = 12 zhang
- Two counties (甲縣 and 乙縣) are tasked with constructing the structure:
  - 甲縣 has 632 people.
  - 乙縣 has 243 people.
- Each person can complete 36 cubic chi of work in 8 days.
- 甲縣 arrives first and starts working. The task is to determine how much of the structure (in terms of height, width, and length) 甲縣 completes before 乙縣 arrives.

### Procedure:
1. Calculate the total volume of work (積尺) that 乙縣 would complete in 8 days.
2. Use this volume to determine the height (高) that 甲縣 completes before 乙縣 arrives.
3. Use the calculated height to determine the corresponding width (廣) and length (袤).

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
袤上 = 3  # Top length in zhang
袤下 = 9  # Bottom length in zhang
廣 = 6    # Width in zhang
高 = 12   # Height in zhang
甲縣人數 = 632  # People in 甲縣
乙縣人數 = 243  # People in 乙縣
程功 = 36  # Work per person in cubic chi
限日 = 8   # Days

# Step 1: Calculate the total volume (積尺) that 乙縣 completes in 8 days
乙積尺 = 程功 * 乙縣人數 * 限日

# Step 2: Calculate the height (高) that 甲縣 completes
# Using the formula provided in the procedure
實 = 6 * 高**2 * (袤下 - 袤上) / 2  # Volume formula for a trapezoidal prism
廉法 = 3 * 高 * 袤上 / 2  # Simplified formula for height calculation
乙高 = pow(乙積尺 / 廉法, 1/3)  # Solve for height (乙高)
甲高 = 高 - 乙高  # Subtract 乙高 from total height to get 甲高

# Step 3: Calculate the corresponding width (廣) and length (袤) for 甲縣
甲廣 = 廣 * (甲高 / 高)  # Proportional width
甲袤 = 袤上 + (袤下 - 袤上) * (甲高 / 高)  # Proportional length

# Results
a = Fraction(甲高).limit_denominator()  # Height completed by 甲縣
b = Fraction(甲廣).limit_denominator()  # Width completed by 甲縣
c = Fraction(甲袤).limit_denominator()  # Length completed by 甲縣

# Output
print(f"高 a = {a} 丈")
print(f"上廣 b = {b} 丈")
print(f"袤 c = {c} 丈")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Volume Calculation**: The total volume of work completed by 乙縣 in 8 days is calculated using the number of people, their work rate, and the number of days.
2. **Height Calculation**: The height completed by 甲縣 is determined by subtracting the height corresponding to 乙縣's work from the total height.
3. **Width and Length Calculation**: The width and length completed by 甲縣 are proportional to the height they complete.

### Answer:
The output will provide the height (`a`), width (`b`), and length (`c`) completed by 甲縣 in terms of zhang.
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: 1029005/937781
Variable 'b' has wrong value. Expected: 18/5, Actual: 430743/785113
Variable 'c' has wrong value. Expected: 33/5, Actual: 2786082/785113"""
