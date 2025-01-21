"""
假令築龍尾堤其堤從頭高上闊以次低狹至尾上廣多下廣少堤頭上下廣差六尺下廣少高一丈二尺少袤四丈八尺甲縣二千三百七十五人乙縣二千三百七十八人丙縣五千二百四十七人各人程功常積一尺九寸八分一日役畢三縣共築今從堤尾與甲縣以次與乙丙問龍尾堤從頭至尾高袤廣及各縣別給高袤廣各多少
求龍尾堤廣袤高術曰以程功乘總人為堤積又六因之為虛積以少高乘少袤為隅冪以少上廣乘之為鱉隅積以減虛積余三約之所得為實並少高袤以少上廣乘之為鱉從橫廉冪三而一加隅冪為方法又三除少上廣以少袤少高加之為廉法從開立方除之得下廣加差即高廣袤求逐縣均給積尺受廣袤術曰以程功乘當縣人當積尺各六因積尺又乘袤冪廣差乘高為法除之為實又三因末廣以袤乘之廣差而一為都廉從開立方除之即甲袤以本高乘之以本袤除之即甲高又以廣差乘甲袤以本袤除之所得加末廣即甲上廣其甲上廣即乙末廣其甲高即垣高求實與都廉如前又並甲上下廣三之乘甲高又乘袤冪以法除之得垣方從開立方除之即乙袤余放此
答曰高 a丈 上廣 b丈 下廣 c丈 袤 d丈 甲縣高 e丈 袤 f丈 上廣 g丈 乙縣高 h丈 袤 i丈 上廣 j丈 丙縣高 k丈 袤 l丈 上廣 m丈 
"""

"""
This problem is extremely complex and involves multiple steps of ancient Chinese mathematics, including cubic equations and proportional distribution of work. Translating this into Python code while adhering strictly to the procedure is a significant task. Below is the Python implementation of the problem, broken into steps as described in the procedure.


"""


from fractions import Fraction
from math import pow

# Constants and initial values
差 = 6  # The difference between the upper and lower widths at the head of the dam
少高 = Fraction(12, 1)  # The height at the tail of the dam (1丈2尺 = 12尺)
少袤 = Fraction(48, 1)  # The length at the tail of the dam (4丈8尺 = 48尺)
少上廣 = Fraction(6, 1)  # The upper width at the tail of the dam
總人 = 2375 + 2378 + 5247  # Total number of workers from all counties
程功 = Fraction(198, 10)  # The amount of work each person completes in one day (1尺9寸8分 = 1.98尺)
日役 = 1  # One day of work

# Step 1: Calculate the total volume of the dam
# 堤積 = 程功 * 總人 * 日役
堤積 = 程功 * 總人 * 日役

# Step 2: Calculate the "虚積" (virtual volume)
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

# Step 6: Calculate the method for finding the lower width
# 方法 = (少上廣 * 少袤 * 少高 + 隅冪) / 3
方法 = (少上廣 * 少袤 * 少高 + 隅冪) / 3

# Step 7: Solve for the lower width (下廣) using the cubic root
# 下廣 = (實積 / 方法)^(1/3) + 差
下廣 = pow(float(實積 / 方法), 1/3) + 差

# Step 8: Calculate the height (高) and length (袤)
# 高 = 下廣 - 差
高 = 下廣 - 差

# 袤 = 實積 / (高 * (少上廣 + 下廣) / 2)
袤 = 實積 / (高 * (少上廣 + 下廣) / 2)

# Step 9: Calculate the work distribution for each county
# 甲縣積 = 程功 * 甲縣人數 * 日役
甲縣人數 = 2375
甲縣積 = 程功 * 甲縣人數 * 日役

# 乙縣積 = 程功 * 乙縣人數 * 日役
乙縣人數 = 2378
乙縣積 = 程功 * 乙縣人數 * 日役

# 丙縣積 = 程功 * 丙縣人數 * 日役
丙縣人數 = 5247
丙縣積 = 程功 * 丙縣人數 * 日役

# Step 10: Calculate the dimensions for each county
# 甲縣袤 = (甲縣積 / (高 * (少上廣 + 下廣) / 2))^(1/3)
甲縣袤 = pow(float(甲縣積 / (高 * (少上廣 + 下廣) / 2)), 1/3)

# 甲縣高 = 高
甲縣高 = 高

# 甲縣上廣 = 少上廣 + (甲縣袤 * 差 / 袤)
甲縣上廣 = 少上廣 + (甲縣袤 * 差 / 袤)

# Repeat the same calculations for 乙縣 and 丙縣
乙縣袤 = pow(float(乙縣積 / (高 * (少上廣 + 下廣) / 2)), 1/3)
乙縣高 = 高
乙縣上廣 = 甲縣上廣

丙縣袤 = pow(float(丙縣積 / (高 * (少上廣 + 下廣) / 2)), 1/3)
丙縣高 = 高
丙縣上廣 = 乙縣上廣

# Final results
a = 高 / 10  # Convert to 丈
b = 少上廣 / 10  # Convert to 丈
c = 下廣 / 10  # Convert to 丈
d = 袤 / 10  # Convert to 丈

e = 甲縣高 / 10  # Convert to 丈
f = 甲縣袤 / 10  # Convert to 丈
g = 甲縣上廣 / 10  # Convert to 丈

h = 乙縣高 / 10  # Convert to 丈
i = 乙縣袤 / 10  # Convert to 丈
j = 乙縣上廣 / 10  # Convert to 丈

k = 丙縣高 / 10  # Convert to 丈
l = 丙縣袤 / 10  # Convert to 丈
m = 丙縣上廣 / 10  # Convert to 丈

# Print the results
print(f"高 {a}丈 上廣 {b}丈 下廣 {c}丈 袤 {d}丈")
print(f"甲縣高 {e}丈 袤 {f}丈 上廣 {g}丈")
print(f"乙縣高 {h}丈 袤 {i}丈 上廣 {j}丈")
print(f"丙縣高 {k}丈 袤 {l}丈 上廣 {m}丈")


"""


This code follows the ancient Chinese procedure step by step, using Python's `Fraction` class for precise arithmetic and `pow` for cubic roots. The results are converted to 丈 (1丈 = 10尺) for the final output.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 0.6647783868071272
Variable 'b' has wrong value. Expected: 17/5, Actual: 3/5
Variable 'c' has wrong value. Expected: 9/5, Actual: 1.2647783868071272
Variable 'd' has wrong value. Expected: 33/5, Actual: 637.0240369522088
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.6647783868071272
Variable 'f' has wrong value. Expected: 33/10, Actual: 0.9120491169869384
Variable 'g' has wrong value. Expected: 21/10, Actual: 0.6008590405360688
Variable 'h' has wrong value. Expected: 21/10, Actual: 0.6647783868071272
Variable 'i' has wrong value. Expected: 33/25, Actual: 0.91243297608823
Variable 'j' has wrong value. Expected: 111/50, Actual: 0.6008590405360688
Variable 'k' has wrong value. Expected: 3, Actual: 0.6647783868071272
Variable 'l' has wrong value. Expected: 99/50, Actual: 1.1878657961948103
Variable 'm' has wrong value. Expected: 12/5, Actual: 0.6008590405360688"""
