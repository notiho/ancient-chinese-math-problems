"""
假令築龍尾堤，其堤從頭高、上闊以次低狹至尾。上廣多，下廣少，堤頭上下廣差六尺，下廣少高一丈二尺，少袤四丈八尺。甲縣二千三百七十五人，乙縣二千三百七十八人，丙縣五千二百四十七人。各人程功常積一尺九寸八分，一日役畢，三縣共築。今從堤尾與甲縣，以次與乙、丙。問：龍尾堤從頭至尾高、袤、廣及各縣別給高、袤、廣各多少。
求龍尾堤廣、袤、高，術曰：以程功乘總人，為堤積。又六因之，為虛積。以少高乘少袤，為隅冪。以少上廣乘之，為鱉隅積。以減虛積，余，三約之，所得為實。並少高、袤，以少上廣乘之，為鱉從橫廉冪。三而一，加隅冪，為方法。又三除少上廣，以少袤、少高加之，為廉法，從。開立方除之，得下廣。加差，即高、廣、袤。求逐縣均給積尺受廣、袤，術曰：以程功乘當縣人，當積尺。各六因積尺。又乘袤冪。廣差乘高，為法。除之，為實。又三因末廣，以袤乘之，廣差而一，為都廉，從。開立方除之，即甲袤。以本高乘之，以本袤除之，即甲高。又以廣差乘甲袤，以本袤除之，所得加末廣，即甲上廣。其甲上廣即乙末廣，其甲高即垣高。求實與都廉，如前。又並甲上下廣，三之，乘甲高，又乘袤冪，以法除之，得垣方，從。開立方除之，即乙袤。余放此。
答曰：高 a丈 ，上廣 b丈 ，下廣 c丈 ，袤 d丈 ；甲縣高 e丈 ，袤 f丈 ，上廣 g丈 ；乙縣高 h丈 ，袤 i丈 ，上廣 j丈 ；丙縣高 k丈 ，袤 l丈 ，上廣 m丈 。
"""

"""
This problem is highly intricate and involves multiple steps of calculation. To solve it, we will break it down into smaller parts, following the procedure ("術") provided. The solution will be implemented step by step in Python, adhering to the structure of the ancient Chinese algorithm.

### Problem Breakdown:
We are tasked with calculating the dimensions of a "Dragon Tail Dam" (龍尾堤) and distributing the work among three counties (甲, 乙, 丙). The calculations involve determining the height, width, and length of the dam, as well as the specific contributions of each county.

### Procedure:
The procedure involves:
1. Calculating the total dam volume.
2. Determining the dimensions of the dam (height, width, and length).
3. Allocating the work among the counties and calculating their respective contributions.

Below is the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction
from math import isqrt

# Input data
差 = 6  # 上廣多，下廣少，差六尺
少下廣 = 1  # 下廣少一丈 (converted to 丈)
少高 = 1 + Fraction(2, 10)  # 高一丈二尺 (converted to 丈)
少袤 = 4 + Fraction(8, 10)  # 袤四丈八尺 (converted to 丈)
甲人 = 2375  # 甲縣人數
乙人 = 2378  # 乙縣人數
丙人 = 5247  # 丙縣人數
程功 = Fraction(1, 1) + Fraction(9, 10) + Fraction(8, 100)  # 每人程功一尺九寸八分 (converted to 丈)

# Step 1: Calculate the total dam volume
總人 = 甲人 + 乙人 + 丙人  # 總人數
堤積 = 程功 * 總人  # 堤積 = 程功 × 總人
虛積 = 堤積 * 6  # 虛積 = 堤積 × 6

# Step 2: Calculate the dimensions of the dam
隅冪 = 少高 * 少袤  # 隅冪 = 少高 × 少袤
鱉隅積 = 隅冪 * 少下廣  # 鱉隅積 = 隅冪 × 少下廣
實積 = (虛積 - 鱉隅積) / 3  # 實積 = (虛積 - 鱉隅積) ÷ 3

# Calculate the method for determining dimensions
鱉從橫廉冪 = (少高 + 少袤) * 少下廣 / 3 + 隅冪  # 鱉從橫廉冪
方法 = 鱉從橫廉冪 / 3  # 方法
廉法 = (少袤 + 少高 + 少下廣) / 3  # 廉法

# Solve for 下廣 (using cube root approximation)
下廣 = isqrt(int(實積 / 方法))  # Approximation for cube root
上廣 = 下廣 + 差  # 上廣 = 下廣 + 差
高 = 下廣  # 高 = 下廣
袤 = 下廣  # 袤 = 下廣

# Step 3: Allocate work among counties
def calculate_county_contribution(縣人數, 縣程功, 縣少袤, 縣少高, 縣少下廣, 縣差):
    縣積尺 = 縣程功 * 縣人數  # 縣積尺 = 縣程功 × 縣人數
    縣虛積 = 縣積尺 * 6  # 縣虛積 = 縣積尺 × 6
    縣實積 = 縣虛積 / 3  # 縣實積 = 縣虛積 ÷ 3

    # Solve for dimensions
    縣下廣 = isqrt(int(縣實積 / 方法))  # Approximation for cube root
    縣上廣 = 縣下廣 + 縣差  # 縣上廣 = 縣下廣 + 縣差
    縣高 = 縣下廣  # 縣高 = 縣下廣
    縣袤 = 縣下廣  # 縣袤 = 縣下廣

    return 縣高, 縣袤, 縣上廣

# Calculate contributions for each county
甲高, 甲袤, 甲上廣 = calculate_county_contribution(甲人, 程功, 少袤, 少高, 少下廣, 差)
乙高, 乙袤, 乙上廣 = calculate_county_contribution(乙人, 程功, 少袤, 少高, 少下廣, 差)
丙高, 丙袤, 丙上廣 = calculate_county_contribution(丙人, 程功, 少袤, 少高, 少下廣, 差)

# Final results
a = 高
b = 上廣
c = 下廣
d = 袤
e, f, g = 甲高, 甲袤, 甲上廣
h, i, j = 乙高, 乙袤, 乙上廣
k, l, m = 丙高, 丙袤, 丙上廣

# Output results
print(f"高 {a}丈 ，上廣 {b}丈 ，下廣 {c}丈 ，袤 {d}丈")
print(f"甲縣高 {e}丈 ，袤 {f}丈 ，上廣 {g}丈")
print(f"乙縣高 {h}丈 ，袤 {i}丈 ，上廣 {j}丈")
print(f"丙縣高 {k}丈 ，袤 {l}丈 ，上廣 {m}丈")
#----- content ends here -----


"""


### Explanation:
1. **Total Dam Volume**: The total volume of the dam is calculated based on the total number of workers and their daily work contribution.
2. **Dam Dimensions**: Using the relationships between height, width, and length, the dimensions are calculated iteratively.
3. **County Contributions**: Each county's contribution is calculated based on its population and the total work required.

### Output:
The program will output the height, width, and length of the dam, as well as the contributions of each county in terms of height, width, and length.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 123
Variable 'b' has wrong value. Expected: 17/5, Actual: 129
Variable 'c' has wrong value. Expected: 9/5, Actual: 123
Variable 'd' has wrong value. Expected: 33/5, Actual: 123
Variable 'e' has wrong value. Expected: 3/2, Actual: 60
Variable 'f' has wrong value. Expected: 33/10, Actual: 60
Variable 'g' has wrong value. Expected: 21/10, Actual: 66
Variable 'h' has wrong value. Expected: 21/10, Actual: 60
Variable 'i' has wrong value. Expected: 33/25, Actual: 60
Variable 'j' has wrong value. Expected: 111/50, Actual: 66
Variable 'k' has wrong value. Expected: 3, Actual: 89
Variable 'l' has wrong value. Expected: 99/50, Actual: 89
Variable 'm' has wrong value. Expected: 12/5, Actual: 95"""
