"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This is a complex ancient Chinese mathematics problem involving the construction of a tapered dam (龍尾堤, "Dragon Tail Dam"). It requires calculating the dimensions of the dam (height, width, and length) and distributing the construction workload among three counties based on their labor contributions. Below is the Python implementation of the problem, step by step, using the provided procedure.


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Constants
差 = 6  # Difference between top and bottom widths (in chi)
少高 = 12  # Minimum height (in chi, 1丈 = 10尺)
少袤 = 48  # Minimum length (in chi, 1丈 = 10尺)
少上廣 = 6  # Minimum top width (in chi)
程功 = Fraction(198, 10)  # Work per person per day (in chi^3)
甲縣人 = 2375  # Number of workers in County A
乙縣人 = 2378  # Number of workers in County B
丙縣人 = 5247  # Number of workers in County C

# Step 1: Calculate the total dam volume
總人 = 甲縣人 + 乙縣人 + 丙縣人
堤積 = 程功 * 總人  # Total dam volume (in chi^3)

# Step 2: Calculate the "虚积" (virtual volume)
虛積 = 堤積 * 6

# Step 3: Calculate the "隅冪" (corner area)
隅冪 = 少高 * 少袤

# Step 4: Calculate the "鱉隅積" (turtle corner volume)
鱉隅積 = 隅冪 * 少上廣

# Step 5: Subtract 虛積 by 鱉隅積 and divide by 3 to get the "實積" (real volume)
實積 = (虛積 - 鱉隅積) / 3

# Step 6: Calculate the "方法" (method volume)
方法 = 隅冪 + (少高 * 少袤 * 少上廣) / 3

# Step 7: Calculate the "廉法" (edge method)
廉法 = (少袤 + 少高 + 少上廣 / 3) / 少上廣

# Step 8: Solve for 下廣 (bottom width) using cubic root
下廣 = pow(實積 / 方法, 1/3)

# Step 9: Add 差 to 下廣 to get 上廣 (top width)
上廣 = 下廣 + 差

# Step 10: Calculate the total height and length
高 = 少高 + 下廣
袤 = 少袤 + 下廣

# Step 11: Distribute workload among counties
def calculate_county_dimensions(縣人, 縣程功, 本高, 本袤, 本上廣, 本下廣):
    當積尺 = 縣程功 * 縣人  # County-specific volume
    實 = 當積尺 * 6
    廉 = pow(實 / (本袤 * 本高 * (本上廣 + 本下廣) / 3), 1/3)
    縣袤 = 廉 * 本袤
    縣高 = 廉 * 本高
    縣上廣 = 廉 * 本上廣
    return 縣高, 縣袤, 縣上廣

# Calculate dimensions for each county
甲高, 甲袤, 甲上廣 = calculate_county_dimensions(甲縣人, 程功, 高, 袤, 上廣, 下廣)
乙高, 乙袤, 乙上廣 = calculate_county_dimensions(乙縣人, 程功, 高, 袤, 上廣, 下廣)
丙高, 丙袤, 丙上廣 = calculate_county_dimensions(丙縣人, 程功, 高, 袤, 上廣, 下廣)

# Final results
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

# Output
print(f"高 {a}丈 ，上廣 {b}丈 ，下廣 {c}丈 ，袤 {d}丈")
print(f"甲縣高 {e}丈 ，袤 {f}丈 ，上廣 {g}丈")
print(f"乙縣高 {h}丈 ，袤 {i}丈 ，上廣 {j}丈")
print(f"丙縣高 {k}丈 ，袤 {l}丈 ，上廣 {m}丈")
#----- content ends here -----


"""


### Explanation:
1. **General Dimensions**:
   - The dam's total height, top width, bottom width, and length are calculated using the given relationships and formulas.
   - The cubic root is used to solve for the bottom width (下廣).

2. **County Workload Distribution**:
   - Each county's contribution is calculated based on the number of workers and their productivity.
   - The dimensions for each county's portion of the dam are calculated proportionally.

3. **Units**:
   - All calculations are performed in chi (尺), and the final results are converted to zhang (丈) for output (1丈 = 10尺).

This code follows the ancient procedure step by step and provides the required dimensions for the dam and the contributions of each county.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 1.8113577210992744
Variable 'b' has wrong value. Expected: 17/5, Actual: 1.2113577210992745
Variable 'c' has wrong value. Expected: 9/5, Actual: 0.6113577210992747
Variable 'd' has wrong value. Expected: 33/5, Actual: 5.411357721099274
Variable 'e' has wrong value. Expected: 3/2, Actual: 6.554328664887959
Variable 'f' has wrong value. Expected: 33/10, Actual: 19.580791035488613
Variable 'g' has wrong value. Expected: 21/10, Actual: 4.383251603121184
Variable 'h' has wrong value. Expected: 21/10, Actual: 6.5570872210490405
Variable 'i' has wrong value. Expected: 33/25, Actual: 19.58903211012974
Variable 'j' has wrong value. Expected: 111/50, Actual: 4.385096406202259
Variable 'k' has wrong value. Expected: 3, Actual: 8.5364512645552
Variable 'l' has wrong value. Expected: 99/50, Actual: 25.50230190489619
Variable 'm' has wrong value. Expected: 12/5, Actual: 5.708809491165036"""
