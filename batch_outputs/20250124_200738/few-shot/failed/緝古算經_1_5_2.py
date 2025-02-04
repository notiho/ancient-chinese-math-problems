"""
假令四郡輸粟，斛法二尺五寸，一人作功為均。自上給甲，以次與乙。其甲郡輸粟三萬八千七百四十五石六斗，乙郡輸粟三萬四千九百五石六斗，丙郡輸粟，二萬六千二百七十石四斗，丁郡輸粟一萬四千七十八石四斗。四郡共穿窖，上袤多於上廣一丈，少於下袤三丈，多於深六丈，少於下廣一丈。各計粟多少，均出丁夫。自穿、負、築，冬程人功常積一十二尺，一日役。問：窖上下廣、袤、深，郡別出人及窖深、廣各多少？
求窖深、廣、袤，術曰：以斛法乘總粟，為積尺。又廣差乘袤差，三而一，為隅陽冪。乃置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪。又半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法。又置塹上袤及塹上廣，並之，為大廣。又並廣差及袤差，半之，以加大廣，為廉法，從。開立方除之，即深。各加差，即合所問。求均給積尺受廣、袤、深，術曰：如築臺術入之。以斛法乘甲郡輸粟，為積尺。又三因，以深冪乘之，以廣差乘袤差而一，為實。深乘上廣，廣差而一，為上廣之高。深乘上袤，袤差而一，為上袤之高。上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即甲深。以袤差乘之，以本深除之，所加上袤，即甲下袤。以廣差乘之，本深除之，所得加上廣，即甲下廣。若求乙、丙、丁，每以前下廣、袤為後上廣、袤，以次皆準此求之，即得。若求人數，各以程功約當郡積尺。
答曰：窖上廣 a丈 ，上袤 b丈 ，下廣 c丈 ，下袤 d丈 ，深 e丈 ；甲郡 f人 ，深 g尺 ，下袤 h丈 ，廣 i丈 ；乙郡 j人 ，深 k尺 ，下袤 l丈 ，廣 m丈 ；丙郡 n人 ，深 o尺 ，下袤 p丈 ，廣 q丈 ；丁郡 r人 ，深 s尺 ，下袤 t丈 ，廣 u丈 。
"""

"""
This problem is highly complex and involves multiple steps of calculation for determining the dimensions of the granary (窖) and the distribution of labor across four regions. The solution requires careful adherence to the ancient Chinese mathematical procedure described in the problem. Below is the Python implementation of the solution, step by step.


"""

#----- content starts here -----

from fractions import Fraction
from math import pow

# Input data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
甲輸粟 = 38745 + Fraction(6, 10)  # 38745石6斗
乙輸粟 = 34905 + Fraction(6, 10)  # 34905石6斗
丙輸粟 = 26270 + Fraction(4, 10)  # 26270石4斗
丁輸粟 = 14078 + Fraction(4, 10)  # 14078石4斗
總粟 = 甲輸粟 + 乙輸粟 + 丙輸粟 + 丁輸粟

# Granary dimensions
上廣差 = 1  # 上廣多於下廣1丈
袤差 = 3  # 上袤少於下袤3丈
深差 = 6  # 深多於下廣6丈

# Winter labor constants
冬程功 = 12  # 每人每日12尺
每日役 = 1  # 每人每日1日

# Step 1: Calculate the total volume in cubic chi (積尺)
積尺 = 斛法 * 總粟

# Step 2: Calculate 隅陽冪
隅陽冪 = Fraction(上廣差 * 袤差, 3)

# Step 3: Calculate 隅頭冪
隅頭冪 = (上廣差 / 2 + 1) * (袤差 / 2 + 1)

# Step 4: Calculate 方法
方法 = 隅陽冪 + 隅頭冪 + (上廣差 / 2 * 袤差 / 2)

# Step 5: Calculate 大廣
大廣 = 1 + 1  # 上廣 + 下廣

# Step 6: Calculate 廉法
廉法 = (上廣差 + 袤差) / 2 + 大廣

# Step 7: Solve for 深 (depth)
深 = pow(積尺 / 方法, Fraction(1, 3))

# Step 8: Calculate 上廣, 上袤, 下廣, 下袤
上廣 = 1
上袤 = 1
下廣 = 上廣 + 上廣差
下袤 = 上袤 + 袤差

# Step 9: Calculate labor distribution for each region
def calculate_labor(輸粟, 上廣, 上袤, 深, 廣差, 袤差):
    積尺 = 輸粟 * 斛法
    深冪 = 深 ** 3
    上廣之高 = 深 * (1 + 廣差)
    上袤之高 = 深 * (1 + 袤差)
    方法 = 3 * 上廣之高 * 上袤之高
    廉法 = 3 * (上廣之高 + 上袤之高) / 2
    深度 = pow(積尺 / 方法, Fraction(1, 3))
    下袤 = 上袤 + 袤差 * 深度 / 深
    下廣 = 上廣 + 廣差 * 深度 / 深
    人數 = 積尺 / (冬程功 * 每日役)
    return 深度, 下袤, 下廣, 人數

# Calculate for 甲郡
甲深, 甲下袤, 甲下廣, 甲人數 = calculate_labor(甲輸粟, 上廣, 上袤, 深, 上廣差, 袤差)

# Calculate for 乙郡
乙深, 乙下袤, 乙下廣, 乙人數 = calculate_labor(乙輸粟, 甲下廣, 甲下袤, 甲深, 上廣差, 袤差)

# Calculate for 丙郡
丙深, 丙下袤, 丙下廣, 丙人數 = calculate_labor(丙輸粟, 乙下廣, 乙下袤, 乙深, 上廣差, 袤差)

# Calculate for 丁郡
丁深, 丁下袤, 丁下廣, 丁人數 = calculate_labor(丁輸粟, 丙下廣, 丙下袤, 丙深, 上廣差, 袤差)

# Output results
a = 上廣
b = 上袤
c = 下廣
d = 下袤
e = 深
f, g, h, i = 甲人數, 甲深, 甲下袤, 甲下廣
j, k, l, m = 乙人數, 乙深, 乙下袤, 乙下廣
n, o, p, q = 丙人數, 丙深, 丙下袤, 丙下廣
r, s, t, u = 丁人數, 丁深, 丁下袤, 丁下廣

print(f"窖上廣 {a}丈 ，上袤 {b}丈 ，下廣 {c}丈 ，下袤 {d}丈 ，深 {e}丈 ；")
print(f"甲郡 {f}人 ，深 {g}尺 ，下袤 {h}丈 ，廣 {i}丈 ；")
print(f"乙郡 {j}人 ，深 {k}尺 ，下袤 {l}丈 ，廣 {m}丈 ；")
print(f"丙郡 {n}人 ，深 {o}尺 ，下袤 {p}丈 ，廣 {q}丈 ；")
print(f"丁郡 {r}人 ，深 {s}尺 ，下袤 {t}丈 ，廣 {u}丈 。")
#----- content ends here -----


"""


This code follows the ancient procedure step by step, calculating the dimensions of the granary and the labor distribution for each region. Each calculation is based on the relationships and formulas provided in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 1
Variable 'b' has wrong value. Expected: 9, Actual: 1
Variable 'c' has wrong value. Expected: 10, Actual: 2
Variable 'd' has wrong value. Expected: 12, Actual: 4
Variable 'e' has wrong value. Expected: 3, Actual: 37.28155830624904
Variable 'g' has wrong value. Expected: 12, Actual: 1.4266617402470232
Variable 'h' has wrong value. Expected: 51/5, Actual: 1.1148016717966338
Variable 'i' has wrong value. Expected: 44/5, Actual: 1.0382672239322113
Variable 'k' has wrong value. Expected: 9, Actual: 12.133719429140186
Variable 'l' has wrong value. Expected: 111/10, Actual: 26.629720352603048
Variable 'm' has wrong value. Expected: 47/5, Actual: 9.543240117534348
Variable 'o' has wrong value. Expected: 6, Actual: 2.6489220910637425
Variable 'p' has wrong value. Expected: 117/10, Actual: 27.28465277621805
Variable 'q' has wrong value. Expected: 49/5, Actual: 9.761550925406015
Variable 's' has wrong value. Expected: 3, Actual: 5.934460346898008
Variable 't' has wrong value. Expected: 12, Actual: 34.00564359008703
Variable 'u' has wrong value. Expected: 10, Actual: 12.001881196695674"""
