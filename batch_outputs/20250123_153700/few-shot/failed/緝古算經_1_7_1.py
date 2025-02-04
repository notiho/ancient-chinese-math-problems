"""
假令芻甍上袤三丈，下袤九丈，廣六丈，高一十二丈。有甲縣六百三十二人，乙縣二百四十三人。夏程人功當積三十六尺，限八日役。自穿築，二縣共造。今甲縣先到。問：自下給高、廣、袤、各多少？
求甲縣均給積尺受廣、袤，術曰：以程功乘乙縣人數，又以限日乘之，為積尺。以六因之，又高冪乘之，又袤差乘廣而一，所得又半之，為實。高乘上袤，袤差而一，為上袤之高。三因上袤之高，半之，為廉法，從。開立方除之，得乙高。以減甍高，余即甲高。求廣、袤，依率求之。
答曰：高 a丈 ，上廣 b丈 ，袤 c丈 。
"""

"""
This is a complex problem involving the division of labor between two counties for constructing a roof-like structure. Let's break it down step by step and encode the procedure into Python.

### Problem Breakdown:
- The roof structure has dimensions: top length (上袤) = 3 zhang, bottom length (下袤) = 9 zhang, width (廣) = 6 zhang, and height (高) = 12 zhang.
- County A (甲縣) has 632 people, and County B (乙縣) has 243 people.
- Each person can complete 36 cubic chi of work per day, and the work is to be completed in 8 days.
- County A arrives first, and the task is to determine how much of the height, width, and length County A is responsible for.

The procedure involves calculating the volume of work (積尺) for County B first, then determining the height, width, and length that County A must complete.

### Procedure:
1. Calculate the total work volume (積尺) for County B using their population, daily work rate, and the number of days.
2. Use the geometric properties of the roof to calculate the height (高) for County A.
3. Use the height to calculate the width (廣) and length (袤) for County A.

Now, let's encode this step-by-step in Python:


"""


from fractions import Fraction
from math import pow

# Roof dimensions
上袤 = 3  # zhang
下袤 = 9  # zhang
廣 = 6    # zhang
高 = 12   # zhang

# County populations
甲縣人數 = 632
乙縣人數 = 243

# Work rate and duration
每日人功 = 36  # cubic chi per person per day
限日 = 8       # days

# Step 1: Calculate the total work volume (積尺) for County B
乙積尺 = 每日人功 * 乙縣人數 * 限日

# Step 2: Calculate the "實" (intermediate value for height calculation)
實 = (6 * 乙積尺 * 高**2 * (下袤 - 上袤)) / 2

# Step 3: Calculate the height for County B (乙高)
廉法 = (3 * 高 * 上袤 * (下袤 - 上袤)) / 2
乙高 = pow(Fraction(實, 廉法), 1/3)

# Step 4: Calculate the height for County A (甲高)
甲高 = 高 - 乙高

# Step 5: Calculate the width (廣) and length (袤) for County A
甲廣 = 廣  # Width remains the same
甲袤 = 上袤 + (下袤 - 上袤) * (甲高 / 高)

# Final results
a = 甲高  # Height for County A
b = 甲廣  # Width for County A
c = 甲袤  # Length for County A

# Output the results
a, b, c


"""


### Explanation of Variables:
- `乙積尺`: Total work volume for County B.
- `實`: Intermediate value used to calculate the height for County B.
- `廉法`: A divisor used in the height calculation.
- `乙高`: Height completed by County B.
- `甲高`: Remaining height for County A.
- `甲廣`: Width for County A (unchanged from the original width).
- `甲袤`: Length for County A, calculated proportionally based on the height.

### Final Answer:
- `a`: Height (高) for County A in zhang.
- `b`: Width (廣) for County A in zhang.
- `c`: Length (袤) for County A in zhang.
"""


"""
Code error: both arguments should be Rational instances"""
