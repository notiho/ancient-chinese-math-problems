"""
假令築龍尾堤其堤從頭高上闊以次低狹至尾上廣多下廣少堤頭上下廣差六尺下廣少高一丈二尺少袤四丈八尺甲縣二千三百七十五人乙縣二千三百七十八人丙縣五千二百四十七人各人程功常積一尺九寸八分一日役畢三縣共築今從堤尾與甲縣以次與乙丙問龍尾堤從頭至尾高袤廣及各縣別給高袤廣各多少
求龍尾堤廣袤高術曰以程功乘總人為堤積又六因之為虛積以少高乘少袤為隅冪以少上廣乘之為鱉隅積以減虛積余三約之所得為實並少高袤以少上廣乘之為鱉從橫廉冪三而一加隅冪為方法又三除少上廣以少袤少高加之為廉法從開立方除之得下廣加差即高廣袤求逐縣均給積尺受廣袤術曰以程功乘當縣人當積尺各六因積尺又乘袤冪廣差乘高為法除之為實又三因末廣以袤乘之廣差而一為都廉從開立方除之即甲袤以本高乘之以本袤除之即甲高又以廣差乘甲袤以本袤除之所得加末廣即甲上廣其甲上廣即乙末廣其甲高即垣高求實與都廉如前又並甲上下廣三之乘甲高又乘袤冪以法除之得垣方從開立方除之即乙袤余放此
答曰高 a丈 上廣 b丈 下廣 c丈 袤 d丈 甲縣高 e丈 袤 f丈 上廣 g丈 乙縣高 h丈 袤 i丈 上廣 j丈 丙縣高 k丈 袤 l丈 上廣 m丈 
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures for calculating the dimensions of a trapezoidal dam (龍尾堤) and distributing the work among three counties. Below is the Python implementation of the procedure step by step.


"""

#----- content starts here -----

from fractions import Fraction
import math

# Constants and initial values
差 = 6  # 差 between upper and lower widths
少高 = Fraction(12, 1)  # 少高 (1丈2尺 = 12尺)
少袤 = Fraction(48, 1)  # 少袤 (4丈8尺 = 48尺)
少上廣 = Fraction(6, 1)  # 少上廣
程功 = Fraction(19, 10) + Fraction(8, 100)  # 程功 (1尺9寸8分 = 1.98尺)
甲縣人 = 2375  # 甲縣人數
乙縣人 = 2378  # 乙縣人數
丙縣人 = 5247  # 丙縣人數

# Step 1: Calculate the total work done by all counties
總人 = 甲縣人 + 乙縣人 + 丙縣人
堤積 = 程功 * 總人  # 堤積

# Step 2: Calculate 虛積
虛積 = 堤積 * 6

# Step 3: Calculate 隅冪 and 鱉隅積
隅冪 = 少高 * 少袤
鱉隅積 = 隅冪 * 少上廣

# Step 4: Subtract 鱉隅積 from 虛積 and divide by 3
余 = (虛積 - 鱉隅積) / 3

# Step 5: Add 少高 and 少袤, then calculate 鱉
鱉 = 少上廣 * (少高 + 少袤)

# Step 6: Calculate 橫廉冪 and 方法
橫廉冪 = (少高 + 少袤) ** 2
方法 = (橫廉冪 / 3) + 隅冪

# Step 7: Divide by 3 and solve for 下廣
廉法 = (少上廣 + 少袤 + 少高) / 3
下廣 = (余 / 方法) ** Fraction(1, 3) + 差

# Step 8: Calculate 高, 上廣, and 袤
高 = 下廣 - 差
上廣 = 少上廣
袤 = 少袤 + 高

# Step 9: Calculate individual contributions for each county
def calculate_county_contribution(縣人數, 縣程功, 縣少袤, 縣少高, 縣少上廣, 縣差):
    縣積尺 = 縣程功 * 縣人數 * 6
    縣法 = 縣少袤 * 縣少高 * 縣少上廣
    縣實 = 縣積尺 / 縣法
    縣末廣 = 縣少上廣 + 縣差
    縣袤 = (縣實 / 縣末廣) ** Fraction(1, 3)
    縣高 = 縣袤 * 縣少高 / 縣少袤
    縣上廣 = 縣少上廣 + 縣袤 * 縣差 / 縣少袤
    return 縣高, 縣袤, 縣上廣

甲高, 甲袤, 甲上廣 = calculate_county_contribution(甲縣人, 程功, 少袤, 少高, 少上廣, 差)
乙高, 乙袤, 乙上廣 = calculate_county_contribution(乙縣人, 程功, 少袤, 少高, 少上廣, 差)
丙高, 丙袤, 丙上廣 = calculate_county_contribution(丙縣人, 程功, 少袤, 少高, 少上廣, 差)

# Final results
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
1. **Initial Values**: The given dimensions and work rates are converted into fractions for precise calculations.
2. **堤積 and 虛積**: The total work done by all counties is calculated, and 虛積 is derived by multiplying by 6.
3. **隅冪 and 鱉隅積**: These intermediate values are calculated based on the given dimensions.
4. **余 and 方法**: These are used to solve for 下廣 (lower width).
5. **高, 上廣, and 袤**: The height, upper width, and length of the dam are calculated.
6. **County Contributions**: A function is used to calculate the contributions of each county based on their workforce and work rates.
7. **Final Results**: The results are printed for the overall dam and for each county.

This implementation follows the ancient Chinese procedure step by step and provides the required dimensions and contributions.
"""


"""
Variable 'a' has wrong value. Expected: 3, Actual: 2.787042538235676
Variable 'b' has wrong value. Expected: 17/5, Actual: 6
Variable 'c' has wrong value. Expected: 9/5, Actual: 8.787042538235676
Variable 'd' has wrong value. Expected: 33/5, Actual: 50.787042538235674
Variable 'e' has wrong value. Expected: 3/2, Actual: 0.2198779606444934
Variable 'f' has wrong value. Expected: 33/10, Actual: 0.8795118425779735
Variable 'g' has wrong value. Expected: 21/10, Actual: 6.109938980322247
Variable 'h' has wrong value. Expected: 21/10, Actual: 0.21997050188464684
Variable 'i' has wrong value. Expected: 33/25, Actual: 0.8798820075385874
Variable 'j' has wrong value. Expected: 111/50, Actual: 6.109985250942324
Variable 'k' has wrong value. Expected: 3, Actual: 0.2863721963237236
Variable 'l' has wrong value. Expected: 99/50, Actual: 1.1454887852948945
Variable 'm' has wrong value. Expected: 12/5, Actual: 6.143186098161862"""
