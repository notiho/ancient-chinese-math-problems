"""
假令四郡輸粟，斛法二尺五寸，一人作功為均。自上給甲，以次與乙。其甲郡輸粟三萬八千七百四十五石六斗，乙郡輸粟三萬四千九百五石六斗，丙郡輸粟，二萬六千二百七十石四斗，丁郡輸粟一萬四千七十八石四斗。四郡共穿窖，上袤多於上廣一丈，少於下袤三丈，多於深六丈，少於下廣一丈。各計粟多少，均出丁夫。自穿、負、築，冬程人功常積一十二尺，一日役。問：窖上下廣、袤、深，郡別出人及窖深、廣各多少？
求窖深、廣、袤，術曰：以斛法乘總粟，為積尺。又廣差乘袤差，三而一，為隅陽冪。乃置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪。又半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法。又置塹上袤及塹上廣，並之，為大廣。又並廣差及袤差，半之，以加大廣，為廉法，從。開立方除之，即深。各加差，即合所問。求均給積尺受廣、袤、深，術曰：如築臺術入之。以斛法乘甲郡輸粟，為積尺。又三因，以深冪乘之，以廣差乘袤差而一，為實。深乘上廣，廣差而一，為上廣之高。深乘上袤，袤差而一，為上袤之高。上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即甲深。以袤差乘之，以本深除之，所加上袤，即甲下袤。以廣差乘之，本深除之，所得加上廣，即甲下廣。若求乙、丙、丁，每以前下廣、袤為後上廣、袤，以次皆準此求之，即得。若求人數，各以程功約當郡積尺。
答曰：窖上廣 a丈 ，上袤 b丈 ，下廣 c丈 ，下袤 d丈 ，深 e丈 ；甲郡 f人 ，深 g尺 ，下袤 h丈 ，廣 i丈 ；乙郡 j人 ，深 k尺 ，下袤 l丈 ，廣 m丈 ；丙郡 n人 ，深 o尺 ，下袤 p丈 ，廣 q丈 ；丁郡 r人 ，深 s尺 ，下袤 t丈 ，廣 u丈 。
"""

"""
This is a complex ancient Chinese mathematical problem involving the distribution of labor for digging a granary (窖) and calculating its dimensions based on the amount of grain contributed by four regions. The solution involves multiple steps, including calculating the granary's dimensions and distributing labor proportionally to the grain contributed by each region. Below is the Python implementation of the problem:

---


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Input data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
甲輸粟 = 38745 + Fraction(6, 10)  # 石6斗
乙輸粟 = 34905 + Fraction(6, 10)  # 石6斗
丙輸粟 = 26270 + Fraction(4, 10)  # 石4斗
丁輸粟 = 14078 + Fraction(4, 10)  # 石4斗
總粟 = 甲輸粟 + 乙輸粟 + 丙輸粟 + 丁輸粟

# Granary dimensions
上廣差 = 1  # 上廣多於下廣1丈
袤差 = 3  # 上袤少於下袤3丈
深差 = 6  # 深多於下廣6丈

# Winter labor constants
冬程功 = 12  # 每人每日完成12尺積功

# Step 1: Calculate the total volume of the granary in cubic chi
積尺 = 總粟 * 斛法

# Step 2: Calculate 隅陽冪 (corner volume adjustment)
隅陽冪 = (上廣差 * 袤差) / 3

# Step 3: Calculate 隅頭冪 (top corner volume adjustment)
隅頭冪 = ((上廣差 / 2) + 1) * ((袤差 / 2) + 1)

# Step 4: Calculate 方法 (method volume)
方法 = 隅陽冪 + 隅頭冪

# Step 5: Calculate 大廣 (total width)
大廣 = 1 + 上廣差 + 袤差

# Step 6: Calculate 廉法 (edge method)
廉法 = 大廣 + (上廣差 + 袤差) / 2

# Step 7: Solve for depth (深)
深 = pow(積尺 / 廉法, 1 / 3)

# Step 8: Calculate 上廣, 上袤, 下廣, 下袤
上廣 = 1
上袤 = 1
下廣 = 上廣 + 上廣差
下袤 = 上袤 + 袤差

# Step 9: Calculate labor distribution for each region
def calculate_labor(輸粟, 上廣, 上袤, 深, 廣差, 袤差, 深差):
    積尺 = 輸粟 * 斛法
    深冪 = 深 ** 3
    上廣之高 = 深 * (1 + 廣差)
    上袤之高 = 深 * (1 + 袤差)
    方法 = (上廣之高 * 上袤之高 * 3) + ((上廣之高 + 上袤之高) * 3 / 2)
    深 = pow(積尺 / 方法, 1 / 3)
    下袤 = 上袤 + (袤差 * 深)
    下廣 = 上廣 + (廣差 * 深)
    return 深, 下袤, 下廣

甲深, 甲下袤, 甲下廣 = calculate_labor(甲輸粟, 上廣, 上袤, 深, 上廣差, 袤差, 深差)
乙深, 乙下袤, 乙下廣 = calculate_labor(乙輸粟, 甲下廣, 甲下袤, 甲深, 上廣差, 袤差, 深差)
丙深, 丙下袤, 丙下廣 = calculate_labor(丙輸粟, 乙下廣, 乙下袤, 乙深, 上廣差, 袤差, 深差)
丁深, 丁下袤, 丁下廣 = calculate_labor(丁輸粟, 丙下廣, 丙下袤, 丙深, 上廣差, 袤差, 深差)

# Step 10: Calculate labor for each region
甲人 = int((甲輸粟 * 斛法) / 冬程功)
乙人 = int((乙輸粟 * 斛法) / 冬程功)
丙人 = int((丙輸粟 * 斛法) / 冬程功)
丁人 = int((丁輸粟 * 斛法) / 冬程功)

# Final output
print(f"窖上廣 {上廣}丈 ，上袤 {上袤}丈 ，下廣 {下廣}丈 ，下袤 {下袤}丈 ，深 {深}丈；")
print(f"甲郡 {甲人}人 ，深 {甲深}尺 ，下袤 {甲下袤}丈 ，廣 {甲下廣}丈；")
print(f"乙郡 {乙人}人 ，深 {乙深}尺 ，下袤 {乙下袤}丈 ，廣 {乙下廣}丈；")
print(f"丙郡 {丙人}人 ，深 {丙深}尺 ，下袤 {丙下袤}丈 ，廣 {丙下廣}丈；")
print(f"丁郡 {丁人}人 ，深 {丁深}尺 ，下袤 {丁下袤}丈 ，廣 {丁下廣}丈；")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Input Data**: The grain contributions from the four regions are converted into `石` and `斗`, and the `斛法` (volume per unit) is defined.
2. **Granary Dimensions**: The differences in dimensions (e.g., `上廣差`, `袤差`, `深差`) are used to calculate the granary's dimensions.
3. **Volume Calculations**: The total volume (`積尺`) is calculated based on the grain contributions and the `斛法`.
4. **Labor Distribution**: The labor required for each region is calculated proportionally to the grain contributed.
5. **Granary Dimensions for Each Region**: The dimensions of the granary for each region are calculated iteratively, using the previous region's dimensions as the starting point for the next.

This code provides the final dimensions of the granary and the labor distribution for each region.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'
Missing variable in output: 'i'
Missing variable in output: 'j'
Missing variable in output: 'k'
Missing variable in output: 'l'
Missing variable in output: 'm'
Missing variable in output: 'n'
Missing variable in output: 'o'
Missing variable in output: 'p'
Missing variable in output: 'q'
Missing variable in output: 'r'
Missing variable in output: 's'
Missing variable in output: 't'
Missing variable in output: 'u'"""
