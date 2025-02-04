"""
假令芻甍上袤三丈下袤九丈廣六丈高一十二丈有甲縣六百三十二人乙縣二百四十三人夏程人功當積三十六尺限八日役自穿築二縣共造今甲縣先到問自下給高廣袤各多少
求甲縣均給積尺受廣袤術曰以程功乘乙縣人數又以限日乘之為積尺以六因之又高冪乘之又袤差乘廣而一所得又半之為實高乘上袤袤差而一為上袤之高三因上袤之高半之為廉法從開立方除之得乙高以減甍高余即甲高求廣袤依率求之
答曰高 a丈 上廣 b丈 袤 c丈 
"""

"""
This problem involves calculating the contribution of one county (甲縣) to the construction of a trapezoidal structure (芻甍) based on the labor force and work rate. The solution follows the ancient Chinese mathematical procedure provided.


"""


from fractions import Fraction
from math import isqrt

# 芻甍 dimensions
上袤 = 3  # 上袤 (top length) in 丈
下袤 = 9  # 下袤 (bottom length) in 丈
廣 = 6    # 廣 (width) in 丈
高 = 12   # 高 (height) in 丈

# 人數 and 工程 details
甲縣人數 = 632  # 甲縣 population
乙縣人數 = 243  # 乙縣 population
夏程人功 = 36   # 夏程人功 (work rate per person per day) in cubic 尺
限日 = 8        # 限日 (time limit) in days

# 求甲縣均給積尺
# 以程功乘乙縣人數
乙積尺 = 夏程人功 * 乙縣人數

# 又以限日乘之
乙積尺 *= 限日

# 為積尺
甲積尺 = 甲縣人數 * 夏程人功 * 限日

# 以六因之
乙積尺 *= 6

# 又高冪乘之
乙積尺 *= 高**2

# 又袤差乘廣而一所得
袤差 = 下袤 - 上袤
乙積尺 *= 袤差 * 廣

# 又半之為實
乙積尺 //= 2

# 高乘上袤
上袤高 = 高 * 上袤

# 袤差而一為上袤之高
上袤高 *= 袤差

# 三因上袤之高
上袤高 *= 3

# 半之為廉法
廉法 = 上袤高 // 2

# 從開立方除之得乙高
乙高 = isqrt(isqrt(乙積尺 // 廉法))

# 以減甍高余即甲高
甲高 = 高 - 乙高

# 求廣袤依率求之
甲廣 = 廣 * (甲高 / 高)
甲袤 = 上袤 + (袤差 * (甲高 / 高))

# 答案
a = Fraction(甲高)
b = Fraction(甲廣)
c = Fraction(甲袤)

# 答曰高 a丈 上廣 b丈 袤 c丈


"""
 

### Explanation of the Code:
1. **Input Dimensions and Parameters**: The dimensions of the trapezoidal structure (芻甍) and the population/work details of the two counties (甲縣 and 乙縣) are provided.
2. **乙縣 Contribution**: The total work (積尺) contributed by 乙縣 is calculated based on its population, work rate, and time limit.
3. **甲縣 Contribution**: The remaining work (積尺) is assigned to 甲縣.
4. **Height Calculation**: Using the given procedure, the height contributed by 乙縣 is calculated, and the remaining height is assigned to 甲縣.
5. **Width and Length Calculation**: The width and length contributed by 甲縣 are calculated proportionally based on its height contribution.
6. **Output**: The results are expressed as fractions for precision.

### Answer:
- 高 (Height): `a` 丈
- 上廣 (Top Width): `b` 丈
- 袤 (Length): `c` 丈
"""


"""
Variable 'a' has wrong value. Expected: 24/5, Actual: -30
Variable 'b' has wrong value. Expected: 18/5, Actual: -15
Variable 'c' has wrong value. Expected: 33/5, Actual: -12"""
