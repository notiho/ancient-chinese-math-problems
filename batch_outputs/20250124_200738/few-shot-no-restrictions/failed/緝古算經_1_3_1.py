"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This is a very complex problem involving ancient Chinese mathematics for calculating the dimensions of a trapezoidal dam (the "Dragon Tail Dam") and distributing the work among three counties. The problem involves multiple steps of geometric calculations and proportional work distribution. Below is the Python implementation of the problem, step by step:

---

### Problem Setup and Definitions


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Constants
差 = 6  # Difference between top and bottom width (in chi)
少高 = 12  # Bottom height (in chi, 1丈 = 10尺)
少袤 = 48  # Bottom length (in chi, 1丈 = 10尺)
少上廣 = 6  # Bottom top width (in chi)
程功 = Fraction(19, 10)  # Work per person per day (in chi^3)
甲縣人 = 2375  # People in County A
乙縣人 = 2378  # People in County B
丙縣人 = 5247  # People in County C

# Total people
總人 = 甲縣人 + 乙縣人 + 丙縣人

# Step 1: Calculate the total dam volume
堤積 = 程功 * 總人  # Total dam volume
虛積 = 堤積 * 6  # Virtual volume

# Step 2: Calculate the "鱉隅積" (corner volume)
隅冪 = 少高 * 少袤  # Corner area
鱉隅積 = 隅冪 * 少上廣  # Corner volume

# Step 3: Subtract virtual volume to get the real volume
實積 = (虛積 - 鱉隅積) / 3  # Real volume

# Step 4: Calculate the "鱉從橫廉冪" (side area)
鱉從橫廉冪 = (少高 + 少袤) * 少上廣 / 3 + 隅冪  # Side area

# Step 5: Calculate the bottom width (下廣)
廉法 = (少袤 + 少高 + 少上廣) / 3
下廣 = pow(實積 / 廉法, 1/3)

# Step 6: Calculate the top width, height, and length
上廣 = 下廣 + 差
高 = 下廣
袤 = 下廣

# Step 7: Calculate work distribution for each county
def calculate_county_work(縣人數, 縣名):
    縣積尺 = 程功 * 縣人數  # Total work volume for the county
    縣虛積 = 縣積尺 * 6  # Virtual volume for the county
    縣實積 = 縣虛積 / 廉法  # Real volume for the county
    縣袤 = pow(縣實積 / 廉法, 1/3)  # Length for the county
    縣高 = 高 * 縣袤 / 袤  # Height for the county
    縣上廣 = 上廣 * 縣袤 / 袤  # Top width for the county
    return 縣高, 縣袤, 縣上廣

# Calculate for each county
甲高, 甲袤, 甲上廣 = calculate_county_work(甲縣人, "甲縣")
乙高, 乙袤, 乙上廣 = calculate_county_work(乙縣人, "乙縣")
丙高, 丙袤, 丙上廣 = calculate_county_work(丙縣人, "丙縣")

# Final Results
a = 高 / 10  # Convert chi to zhang
b = 上廣 / 10  # Convert chi to zhang
c = 下廣 / 10  # Convert chi to zhang
d = 袤 / 10  # Convert chi to zhang
e = 甲高 / 10  # Convert chi to zhang
f = 甲袤 / 10  # Convert chi to zhang
g = 甲上廣 / 10  # Convert chi to zhang
h = 乙高 / 10  # Convert chi to zhang
i = 乙袤 / 10  # Convert chi to zhang
j = 乙上廣 / 10  # Convert chi to zhang
k = 丙高 / 10  # Convert chi to zhang
l = 丙袤 / 10  # Convert chi to zhang
m = 丙上廣 / 10  # Convert chi to zhang

# Print Results
print(f"高 {a}丈 ，上廣 {b}丈 ，下廣 {c}丈 ，袤 {d}丈")
print(f"甲縣高 {e}丈 ，袤 {f}丈 ，上廣 {g}丈")
print(f"乙縣高 {h}丈 ，袤 {i}丈 ，上廣 {j}丈")
print(f"丙縣高 {k}丈 ，袤 {l}丈 ，上廣 {m}丈")
#----- content ends here -----


"""


---

### Explanation of the Code

1. **Input Parameters**:
   - The problem starts with the given dimensions of the dam (height, width, and length at the bottom) and the work capacity of each county.

2. **Volume Calculations**:
   - The total dam volume (`堤積`) is calculated based on the total number of people and their work capacity.
   - The "virtual volume" (`虛積`) is calculated by multiplying the total volume by 6.
   - The "corner volume" (`鱉隅積`) is calculated using the bottom dimensions.

3. **Real Volume**:
   - The real volume is obtained by subtracting the corner volume from the virtual volume and dividing by 3.

4. **Bottom Width Calculation**:
   - The bottom width (`下廣`) is calculated using the cube root of the real volume divided by the side area.

5. **Top Width, Height, and Length**:
   - The top width, height, and length are calculated based on the bottom width and the given differences.

6. **Work Distribution**:
   - For each county, the work volume is calculated, and the corresponding dimensions (height, length, and top width) are determined proportionally.

7. **Output**:
   - The results are converted from chi to zhang (1丈 = 10尺) and printed.

---

### Example Output

```
高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈
甲縣高 e丈 ，袤 f丈 ，上廣 g丈
乙縣高 h丈 ，袤 i丈 ，上廣 j丈
丙縣高 k丈 ，袤 l丈 ，上廣 m丈
```

This implementation follows the ancient Chinese mathematical procedure described in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 1.1875823832713175
Variable 'b' has wrong value. Expected: 17/5, Actual: 1.7875823832713174
Variable 'c' has wrong value. Expected: 9/5, Actual: 1.1875823832713175
Variable 'd' has wrong value. Expected: 33/5, Actual: 1.1875823832713175
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.3824497381255102
Variable 'f' has wrong value. Expected: 33/10, Actual: 0.3824497381255102
Variable 'g' has wrong value. Expected: 21/10, Actual: 0.5756740955323688
Variable 'h' has wrong value. Expected: 21/10, Actual: 0.3826107018390118
Variable 'i' has wrong value. Expected: 33/25, Actual: 0.3826107018390118
Variable 'j' has wrong value. Expected: 111/50, Actual: 0.575916382638219
Variable 'k' has wrong value. Expected: 3, Actual: 0.4981080012267167
Variable 'l' has wrong value. Expected: 99/50, Actual: 0.4981080012267167
Variable 'm' has wrong value. Expected: 12/5, Actual: 0.7497661640168857"""
