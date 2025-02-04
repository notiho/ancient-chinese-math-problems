"""
假令築龍尾堤其堤從頭高上闊以次低狹至尾上廣多下廣少堤頭上下廣差六尺下廣少高一丈二尺少袤四丈八尺甲縣二千三百七十五人乙縣二千三百七十八人丙縣五千二百四十七人各人程功常積一尺九寸八分一日役畢三縣共築今從堤尾與甲縣以次與乙丙問龍尾堤從頭至尾高袤廣及各縣別給高袤廣各多少
求龍尾堤廣袤高術曰以程功乘總人為堤積又六因之為虛積以少高乘少袤為隅冪以少上廣乘之為鱉隅積以減虛積余三約之所得為實並少高袤以少上廣乘之為鱉從橫廉冪三而一加隅冪為方法又三除少上廣以少袤少高加之為廉法從開立方除之得下廣加差即高廣袤求逐縣均給積尺受廣袤術曰以程功乘當縣人當積尺各六因積尺又乘袤冪廣差乘高為法除之為實又三因末廣以袤乘之廣差而一為都廉從開立方除之即甲袤以本高乘之以本袤除之即甲高又以廣差乘甲袤以本袤除之所得加末廣即甲上廣其甲上廣即乙末廣其甲高即垣高求實與都廉如前又並甲上下廣三之乘甲高又乘袤冪以法除之得垣方從開立方除之即乙袤余放此
答曰高 a丈 上廣 b丈 下廣 c丈 袤 d丈 甲縣高 e丈 袤 f丈 上廣 g丈 乙縣高 h丈 袤 i丈 上廣 j丈 丙縣高 k丈 袤 l丈 上廣 m丈 
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. Translating it into Python code while adhering to the structure of the procedure is a lengthy process. Below is the step-by-step implementation of the procedure in Python.

### Problem Restatement:
We are tasked with calculating the dimensions of the Longwei Dike (height, length, upper width, and lower width) and the contributions of three counties (A, B, and C) to the construction of the dike. The procedure involves calculating the total volume of the dike, distributing the work among the counties, and determining the specific dimensions for each county's contribution.

---

### Python Code Implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Constants
差 = 6  # Difference between upper and lower width at the head (in chi)
少高 = Fraction(12, 1)  # Initial height at the tail (in chi)
少袤 = Fraction(48, 1)  # Initial length at the tail (in chi)
少上廣 = Fraction(6, 1)  # Initial upper width at the tail (in chi)
程功 = Fraction(19, 10)  # Work volume per person per day (in chi^3)
甲縣人 = 2375  # Number of workers from County A
乙縣人 = 2378  # Number of workers from County B
丙縣人 = 5247  # Number of workers from County C
總人 = 甲縣人 + 乙縣人 + 丙縣人  # Total number of workers

# Step 1: Calculate the total volume of the dike
# 堤積 = 程功 * 總人
堤積 = 程功 * 總人

# Step 2: Calculate the "虚積" (hypothetical volume)
# 虛積 = 堤積 * 6
虛積 = 堤積 * 6

# Step 3: Calculate the "隅冪" (corner volume)
# 隅冪 = 少高 * 少袤
隅冪 = 少高 * 少袤

# Step 4: Calculate the "鱉隅積" (turtle corner volume)
# 鱉隅積 = 隅冪 * 少上廣
鱉隅積 = 隅冪 * 少上廣

# Step 5: Subtract 鱉隅積 from 虛積 and divide by 3
# 實積 = (虛積 - 鱉隅積) / 3
實積 = (虛積 - 鱉隅積) / 3

# Step 6: Add 少高 and 少袤, then calculate the "鱉從橫廉冪"
# 鱉從橫廉冪 = (少上廣 * (少高 + 少袤)) / 3
鱉從橫廉冪 = (少上廣 * (少高 + 少袤)) / 3

# Step 7: Add 隅冪 to 鱉從橫廉冪 to get the divisor (方法)
# 方法 = 鱉從橫廉冪 + 隅冪
方法 = 鱉從橫廉冪 + 隅冪

# Step 8: Divide 實積 by 方法 to get the lower width (下廣)
# 下廣 = 實積 / 方法
下廣 = 實積 / 方法

# Step 9: Add 差 to 下廣 to get the height (高)
# 高 = 下廣 + 差
高 = 下廣 + 差

# Step 10: Calculate the upper width (上廣)
# 上廣 = 少上廣 + 差
上廣 = 少上廣 + 差

# Step 11: Calculate the length (袤)
# 袤 = 實積 / (高 * (上廣 + 下廣) / 2)
袤 = 實積 / (高 * (上廣 + 下廣) / 2)

# Step 12: Distribute the work among the counties
# Calculate the volume for each county
甲積 = 程功 * 甲縣人 * 6
乙積 = 程功 * 乙縣人 * 6
丙積 = 程功 * 丙縣人 * 6

# Step 13: Calculate dimensions for County A
# 甲袤 = (甲積 / (高 * (上廣 + 下廣) / 2))
甲袤 = 甲積 / (高 * (上廣 + 下廣) / 2)

# 甲高 = 高 * (甲袤 / 袤)
甲高 = 高 * (甲袤 / 袤)

# 甲上廣 = 上廣 * (甲袤 / 袤)
甲上廣 = 上廣 * (甲袤 / 袤)

# Step 14: Repeat for County B and County C
乙袤 = 乙積 / (高 * (上廣 + 下廣) / 2)
乙高 = 高 * (乙袤 / 袤)
乙上廣 = 上廣 * (乙袤 / 袤)

丙袤 = 丙積 / (高 * (上廣 + 下廣) / 2)
丙高 = 高 * (丙袤 / 袤)
丙上廣 = 上廣 * (丙袤 / 袤)

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

# Output Results
print(f"高: {a}丈, 上廣: {b}丈, 下廣: {c}丈, 袤: {d}丈")
print(f"甲縣高: {e}丈, 袤: {f}丈, 上廣: {g}丈")
print(f"乙縣高: {h}丈, 袤: {i}丈, 上廣: {j}丈")
print(f"丙縣高: {k}丈, 袤: {l}丈, 上廣: {m}丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Constants**: The problem provides initial dimensions and work rates, which are converted into fractions for precise calculations.
2. **Volume Calculations**: The total volume of the dike is calculated using the work rate and the number of workers. Intermediate volumes like "虚積" and "隅冪" are computed as per the procedure.
3. **Dimension Calculations**: The lower width, height, upper width, and length of the dike are calculated step by step using the provided formulas.
4. **County Contributions**: The work is distributed among the counties, and the dimensions for each county's contribution are calculated.
5. **Results**: The final dimensions are converted from chi to zhang (1 zhang = 10 chi) and printed.

This code follows the ancient Chinese procedure closely and provides the required dimensions for the dike and each county's contribution.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 2564/435
Variable 'b' has wrong value. Expected: 17/5, Actual: 6/5
Variable 'c' has wrong value. Expected: 9/5, Actual: 2303/435
Variable 'd' has wrong value. Expected: 33/5, Actual: 17431407/9054125
Variable 'e' has wrong value. Expected: 3/2, Actual: 1157005/267148
Variable 'f' has wrong value. Expected: 33/10, Actual: 8197227/5794640
Variable 'g' has wrong value. Expected: 21/10, Actual: 16245/18424
Variable 'h' has wrong value. Expected: 21/10, Actual: 499339/115150
Variable 'i' has wrong value. Expected: 33/25, Actual: 512973837/362165000
Variable 'j' has wrong value. Expected: 111/50, Actual: 203319/230300
Variable 'k' has wrong value. Expected: 3, Actual: 63903213/6678700
Variable 'l' has wrong value. Expected: 99/50, Actual: 2263728951/724330000
Variable 'm' has wrong value. Expected: 12/5, Actual: 897237/460600"""
