"""
假令築龍尾堤其堤從頭高上闊以次低狹至尾上廣多下廣少堤頭上下廣差六尺下廣少高一丈二尺少袤四丈八尺甲縣二千三百七十五人乙縣二千三百七十八人丙縣五千二百四十七人各人程功常積一尺九寸八分一日役畢三縣共築今從堤尾與甲縣以次與乙丙問龍尾堤從頭至尾高袤廣及各縣別給高袤廣各多少
求龍尾堤廣袤高術曰以程功乘總人為堤積又六因之為虛積以少高乘少袤為隅冪以少上廣乘之為鱉隅積以減虛積余三約之所得為實並少高袤以少上廣乘之為鱉從橫廉冪三而一加隅冪為方法又三除少上廣以少袤少高加之為廉法從開立方除之得下廣加差即高廣袤求逐縣均給積尺受廣袤術曰以程功乘當縣人當積尺各六因積尺又乘袤冪廣差乘高為法除之為實又三因末廣以袤乘之廣差而一為都廉從開立方除之即甲袤以本高乘之以本袤除之即甲高又以廣差乘甲袤以本袤除之所得加末廣即甲上廣其甲上廣即乙末廣其甲高即垣高求實與都廉如前又並甲上下廣三之乘甲高又乘袤冪以法除之得垣方從開立方除之即乙袤余放此
答曰高 a丈 上廣 b丈 下廣 c丈 袤 d丈 甲縣高 e丈 袤 f丈 上廣 g丈 乙縣高 h丈 袤 i丈 上廣 j丈 丙縣高 k丈 袤 l丈 上廣 m丈 
"""

"""
This problem is quite complex and involves multiple steps to calculate the dimensions of the 龙尾堤 (Dragon Tail Embankment) and the contributions of each county. I'll break it down step by step and encode the procedure in Python.

### Problem Breakdown
1. **General Dimensions of the Embankment**:
   - Calculate the total volume of the embankment based on the work done by all counties.
   - Use the given relationships between the dimensions (height, width, length) to determine the overall dimensions of the embankment.

2. **Contribution of Each County**:
   - Divide the total work among the counties based on their contributions.
   - Calculate the specific dimensions of the portion of the embankment built by each county.

### Python Code

"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Given data
差 = 6  # Difference between upper and lower widths (in chi)
少高 = Fraction(12, 1)  # Minimum height (in chi)
少袤 = Fraction(48, 1)  # Minimum length (in chi)
少上廣 = Fraction(6, 1)  # Minimum upper width (in chi)
總人 = 2375 + 2378 + 5247  # Total number of workers
程功 = Fraction(19, 10) + Fraction(8, 100)  # Work done per person per day (in cubic chi)
日役 = 1  # Number of days worked

# Step 1: Calculate the total volume of the embankment
堤積 = 總人 * 程功 * 日役  # Total volume of the embankment

# Step 2: Calculate the "虚积" (virtual volume)
虛積 = 堤積 * 6

# Step 3: Calculate the "隅冪" (corner volume) and "鱉隅積" (upper corner volume)
隅冪 = 少高 * 少袤
鱉隅積 = 隅冪 * 少上廣

# Step 4: Subtract "鱉隅積" from "虚积" and divide by 3 to get the "實積" (real volume)
實積 = (虛積 - 鱉隅積) / 3

# Step 5: Calculate the method for determining the dimensions
方法 = (少上廣 * 少袤 + 少高) * 3

# Step 6: Solve for the lower width (下廣)
下廣 = pow(float(實積 / 方法), 1/3) + 差

# Step 7: Calculate the height (高), upper width (上廣), and length (袤)
高 = 下廣 - 差
上廣 = 少上廣 + 差
袤 = 實積 / (高 * (上廣 + 下廣) / 2)

# Step 8: Calculate the contributions of each county
# County A (甲縣)
甲積 = 程功 * 2375 * 日役 * 6
甲方法 = (袤**2 * 差 * 高) / 甲積
甲袤 = pow(float(甲積 / 甲方法), 1/3)
甲高 = 高 * 甲袤 / 袤
甲上廣 = 少上廣 + 差 * 甲袤 / 袤

# County B (乙縣)
乙積 = 程功 * 2378 * 日役 * 6
乙方法 = (袤**2 * 差 * 高) / 乙積
乙袤 = pow(float(乙積 / 乙方法), 1/3)
乙高 = 高 * 乙袤 / 袤
乙上廣 = 甲上廣

# County C (丙縣)
丙積 = 程功 * 5247 * 日役 * 6
丙方法 = (袤**2 * 差 * 高) / 丙積
丙袤 = pow(float(丙積 / 丙方法), 1/3)
丙高 = 高 * 丙袤 / 袤
丙上廣 = 乙上廣

# Final Results
a = 高 / 10  # Convert to 丈
b = 上廣 / 10  # Convert to 丈
c = 下廣 / 10  # Convert to 丈
d = 袤 / 10  # Convert to 丈

e = 甲高 / 10  # Convert to 丈
f = 甲袤 / 10  # Convert to 丈
g = 甲上廣 / 10  # Convert to 丈

h = 乙高 / 10  # Convert to 丈
i = 乙袤 / 10  # Convert to 丈
j = 乙上廣 / 10  # Convert to 丈

k = 丙高 / 10  # Convert to 丈
l = 丙袤 / 10  # Convert to 丈
m = 丙上廣 / 10  # Convert to 丈

# Output the results
print(f"高: {a}丈, 上廣: {b}丈, 下廣: {c}丈, 袤: {d}丈")
print(f"甲縣高: {e}丈, 袤: {f}丈, 上廣: {g}丈")
print(f"乙縣高: {h}丈, 袤: {i}丈, 上廣: {j}丈")
print(f"丙縣高: {k}丈, 袤: {l}丈, 上廣: {m}丈")
#----- content ends here -----


"""


### Explanation of the Code
1. **General Dimensions**:
   - The total volume of the embankment is calculated based on the total number of workers, their daily work rate, and the number of days worked.
   - Using the relationships between height, width, and length, the dimensions of the embankment are determined.

2. **County Contributions**:
   - The total work done by each county is calculated.
   - Using the same relationships, the specific dimensions of the portion of the embankment built by each county are determined.

3. **Units**:
   - All calculations are performed in chi, but the final results are converted to 丈 (1 丈 = 10 chi).

This code follows the procedure described in the problem and provides the required dimensions for the embankment and the contributions of each county.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 0.3495777220154258
Variable 'b' has wrong value. Expected: 17/5, Actual: 6/5
Variable 'c' has wrong value. Expected: 9/5, Actual: 0.9495777220154258
Variable 'd' has wrong value. Expected: 33/5, Actual: 102.3309129324477
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.0011305437424909545
Variable 'f' has wrong value. Expected: 33/10, Actual: 0.33094092098369016
Variable 'g' has wrong value. Expected: 21/10, Actual: 0.6019404161157176
Variable 'h' has wrong value. Expected: 21/10, Actual: 0.0011314955790103676
Variable 'i' has wrong value. Expected: 33/25, Actual: 0.3312195494369921
Variable 'j' has wrong value. Expected: 111/50, Actual: 0.6019404161157176
Variable 'k' has wrong value. Expected: 3, Actual: 0.0019177220892508337
Variable 'l' has wrong value. Expected: 99/50, Actual: 0.5613694460057703
Variable 'm' has wrong value. Expected: 12/5, Actual: 0.6019404161157176"""
