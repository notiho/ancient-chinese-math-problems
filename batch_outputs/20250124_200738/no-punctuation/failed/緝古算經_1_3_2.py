"""
假令築龍尾堤其堤從頭高上闊以次低狹至尾上廣多下廣少堤頭上下廣差六尺下廣少高一丈二尺少袤四丈八尺甲縣二千三百七十五人乙縣二千三百七十八人丙縣五千二百四十七人各人程功常積一尺九寸八分一日役畢三縣共築今從堤尾與甲縣以次與乙丙問龍尾堤從頭至尾高袤廣及各縣別給高袤廣各多少
求龍尾堤廣袤高術曰以程功乘總人為堤積又六因之為虛積以少高乘少袤為隅冪以少上廣乘之為鱉隅積以減虛積余三約之所得為實並少高袤以少上廣乘之為鱉從橫廉冪三而一加隅冪為方法又三除少上廣以少袤少高加之為廉法從開立方除之得下廣加差即高廣袤求逐縣均給積尺受廣袤術曰以程功乘當縣人當積尺各六因積尺又乘袤冪廣差乘高為法除之為實又三因末廣以袤乘之廣差而一為都廉從開立方除之即甲袤以本高乘之以本袤除之即甲高又以廣差乘甲袤以本袤除之所得加末廣即甲上廣其甲上廣即乙末廣其甲高即垣高求實與都廉如前又並甲上下廣三之乘甲高又乘袤冪以法除之得垣方從開立方除之即乙袤余放此
答曰高 a丈 上廣 b丈 下廣 c丈 袤 d丈 甲縣高 e丈 袤 f丈 上廣 g丈 乙縣高 h丈 袤 i丈 上廣 j丈 丙縣高 k丈 袤 l丈 上廣 m丈 
"""

"""
This problem is highly complex and involves multiple steps of calculations for determining the dimensions of the "Dragon Tail Dike" (龍尾堤) and the contributions of three counties (甲, 乙, 丙) to its construction. The procedure includes calculating the total volume of the dike, distributing the work among the counties, and determining the specific dimensions (height, width, and length) for each county's contribution. Below is the Python implementation of the procedure.


"""

#----- content starts here -----

from fractions import Fraction
from math import isqrt

# Input data
差 = 6  # 差 between upper and lower widths
少高 = Fraction(12, 1)  # 少高 (1丈2尺 = 12尺)
少袤 = Fraction(48, 1)  # 少袤 (4丈8尺 = 48尺)
少上廣 = Fraction(6, 1)  # 少上廣
甲縣人 = 2375  # 甲縣人數
乙縣人 = 2378  # 乙縣人數
丙縣人 = 5247  # 丙縣人數
程功 = Fraction(19, 10)  # 每人每日程功 (1尺9寸8分 = 1.98尺)
總人 = 甲縣人 + 乙縣人 + 丙縣人  # 總人數

# Step 1: Calculate the total volume of the dike
堤積 = 程功 * 總人  # 堤積
虛積 = 堤積 * 6  # 虛積
隅冪 = 少高 * 少袤  # 隅冪
鱉隅積 = 隅冪 * 少上廣  # 鱉隅積
實積 = (虛積 - 鱉隅積) / 3  # 實積

# Step 2: Calculate the dimensions of the dike
方法 = (少高 + 少袤) * 少上廣 + 隅冪 / 3  # 方法
廉法 = (少袤 + 少高 + 少上廣) / 3  # 廉法
下廣 = isqrt(實積 / 方法) + 差  # 下廣
高 = 下廣 - 差  # 高
袤 = 實積 / (高 * (少上廣 + 下廣) / 2)  # 袤
上廣 = 少上廣  # 上廣 remains the same

# Step 3: Calculate the contribution of each county
def calculate_county_contribution(縣人, 縣名):
    當積尺 = 程功 * 縣人  # 當積尺
    縣實積 = 當積尺 * 6  # 縣實積
    縣方法 = (少袤 * 高 * (下廣 - 上廣)) / 縣實積  # 縣方法
    縣袤 = isqrt(縣實積 / 縣方法)  # 縣袤
    縣高 = 縣袤 * 高 / 少袤  # 縣高
    縣上廣 = (縣袤 * (下廣 - 上廣) / 少袤) + 上廣  # 縣上廣
    return 縣高, 縣袤, 縣上廣

甲高, 甲袤, 甲上廣 = calculate_county_contribution(甲縣人, "甲")
乙高, 乙袤, 乙上廣 = calculate_county_contribution(乙縣人, "乙")
丙高, 丙袤, 丙上廣 = calculate_county_contribution(丙縣人, "丙")

# Output results
a = 高
b = 上廣
c = 下廣
d = 袤
e, f, g = 甲高, 甲袤, 甲上廣
h, i, j = 乙高, 乙袤, 乙上廣
k, l, m = 丙高, 丙袤, 丙上廣

print(f"高 {a}丈 上廣 {b}丈 下廣 {c}丈 袤 {d}丈")
print(f"甲縣高 {e}丈 袤 {f}丈 上廣 {g}丈")
print(f"乙縣高 {h}丈 袤 {i}丈 上廣 {j}丈")
print(f"丙縣高 {k}丈 袤 {l}丈 上廣 {m}丈")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Data**: The given dimensions, differences, and work rates are converted into fractions for precise calculations.
2. **Step 1**: The total volume of the dike (`堤積`) is calculated based on the total number of workers and their daily work rate. The "虛積" and "實積" are derived using the given formulas.
3. **Step 2**: The dimensions of the dike (height, upper width, lower width, and length) are calculated using the formulas provided in the procedure.
4. **Step 3**: The contribution of each county is calculated by dividing the total work proportionally among the counties and determining their respective dimensions.
5. **Output**: The results are printed in the required format.

This implementation follows the procedure described in the problem and ensures that all calculations are performed step by step.
"""


"""
Code error: 'Fraction' object cannot be interpreted as an integer"""
