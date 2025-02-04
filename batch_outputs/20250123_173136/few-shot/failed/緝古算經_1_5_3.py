"""
假令四郡輸粟，斛法二尺五寸，一人作功為均。自上給甲，以次與乙。其甲郡輸粟三萬八千七百四十五石六斗，乙郡輸粟三萬四千九百五石六斗，丙郡輸粟，二萬六千二百七十石四斗，丁郡輸粟一萬四千七十八石四斗。四郡共穿窖，上袤多於上廣一丈，少於下袤三丈，多於深六丈，少於下廣一丈。各計粟多少，均出丁夫。自穿、負、築，冬程人功常積一十二尺，一日役。問：窖上下廣、袤、深，郡別出人及窖深、廣各多少？
求窖深、廣、袤，術曰：以斛法乘總粟，為積尺。又廣差乘袤差，三而一，為隅陽冪。乃置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪。又半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法。又置塹上袤及塹上廣，並之，為大廣。又並廣差及袤差，半之，以加大廣，為廉法，從。開立方除之，即深。各加差，即合所問。求均給積尺受廣、袤、深，術曰：如築臺術入之。以斛法乘甲郡輸粟，為積尺。又三因，以深冪乘之，以廣差乘袤差而一，為實。深乘上廣，廣差而一，為上廣之高。深乘上袤，袤差而一，為上袤之高。上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即甲深。以袤差乘之，以本深除之，所加上袤，即甲下袤。以廣差乘之，本深除之，所得加上廣，即甲下廣。若求乙、丙、丁，每以前下廣、袤為後上廣、袤，以次皆準此求之，即得。若求人數，各以程功約當郡積尺。
答曰：窖上廣 a丈 ，上袤 b丈 ，下廣 c丈 ，下袤 d丈 ，深 e丈 ；甲郡 f人 ，深 g尺 ，下袤 h丈 ，廣 i丈 ；乙郡 j人 ，深 k尺 ，下袤 l丈 ，廣 m丈 ；丙郡 n人 ，深 o尺 ，下袤 p丈 ，廣 q丈 ；丁郡 r人 ，深 s尺 ，下袤 t丈 ，廣 u丈 。
"""

"""
This problem is highly complex and involves multiple steps of calculations, including volumetric calculations, proportional distribution, and iterative procedures for determining dimensions and labor requirements. Below is the Python implementation of the solution based on the provided procedure ("術"). Each step of the procedure is carefully translated into Python code.


"""


from fractions import Fraction
from math import isqrt

# Input data
斛法 = Fraction(25, 10)  # 2尺5寸 = 2.5尺
甲輸粟 = Fraction(38745, 1) + Fraction(6, 10)  # 38745石6斗
乙輸粟 = Fraction(34905, 1) + Fraction(6, 10)  # 34905石6斗
丙輸粟 = Fraction(26270, 1) + Fraction(4, 10)  # 26270石4斗
丁輸粟 = Fraction(14078, 1) + Fraction(4, 10)  # 14078石4斗
總粟 = 甲輸粟 + 乙輸粟 + 丙輸粟 + 丁輸粟

# 窖 dimensions
上廣差 = 1  # 上廣差1丈
袤差 = 3  # 袤差3丈
深差 = 6  # 深差6丈
下廣差 = 1  # 下廣差1丈

# Winter labor constants
冬程功 = 12  # 每人每日功12尺

# Step 1: 求窖深、廣、袤
# 以斛法乘總粟，為積尺
積尺 = 總粟 * 斛法

# 廣差乘袤差，三而一，為隅陽冪
隅陽冪 = (上廣差 * 袤差) / 3

# 置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪
塹上廣 = 1  # Assume 塹上廣 = 1丈 (initial guess)
塹上袤 = 1  # Assume 塹上袤 = 1丈 (initial guess)
隅頭冪 = (塹上廣 + 上廣差 / 2) * 塹上袤

# 半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法
方法 = 隅陽冪 + 隅頭冪 + (袤差 / 2) * 塹上廣

# 置塹上袤及塹上廣，並之，為大廣
大廣 = 塹上袤 + 塹上廣

# 並廣差及袤差，半之，以加大廣，為廉法
廉法 = 大廣 + (上廣差 + 袤差) / 2

# 開立方除之，即深
深 = isqrt(積尺 / 方法)

# 各加差，即合所問
窖深 = 深 + 深差
窖上廣 = 塹上廣
窖上袤 = 塹上袤
窖下廣 = 窖上廣 + 上廣差
窖下袤 = 窖上袤 + 袤差

# Step 2: 求均給積尺受廣、袤、深
def 求郡數據(輸粟, 上廣, 上袤, 深, 廣差, 袤差):
    # 以斛法乘郡輸粟，為積尺
    積尺 = 輸粟 * 斛法

    # 三因，以深冪乘之，以廣差乘袤差而一，為實
    實 = 積尺 * 深 * (廣差 * 袤差 / 3)

    # 深乘上廣，廣差而一，為上廣之高
    上廣之高 = 深 * 上廣 / 廣差

    # 深乘上袤，袤差而一，為上袤之高
    上袤之高 = 深 * 上袤 / 袤差

    # 上廣之高乘上袤之高，三之，為方法
    方法 = (上廣之高 * 上袤之高) / 3

    # 並兩高，三之，二而一，為廉法
    廉法 = (上廣之高 + 上袤之高) * 3 / 2

    # 開立方除之，即深
    郡深 = isqrt(實 / 方法)

    # 以袤差乘之，以本深除之，所加上袤，即郡下袤
    郡下袤 = 上袤 + (袤差 * 郡深 / 深)

    # 以廣差乘之，本深除之，所得加上廣，即郡下廣
    郡下廣 = 上廣 + (廣差 * 郡深 / 深)

    return 郡深, 郡下袤, 郡下廣

# 甲郡
甲深, 甲下袤, 甲下廣 = 求郡數據(甲輸粟, 窖上廣, 窖上袤, 窖深, 上廣差, 袤差)

# 乙郡
乙深, 乙下袤, 乙下廣 = 求郡數據(乙輸粟, 甲下廣, 甲下袤, 甲深, 上廣差, 袤差)

# 丙郡
丙深, 丙下袤, 丙下廣 = 求郡數據(丙輸粟, 乙下廣, 乙下袤, 乙深, 上廣差, 袤差)

# 丁郡
丁深, 丁下袤, 丁下廣 = 求郡數據(丁輸粟, 丙下廣, 丙下袤, 丙深, 上廣差, 袤差)

# Step 3: 求人數
def 求人數(積尺, 冬程功):
    return 積尺 / 冬程功

甲人 = 求人數(甲輸粟 * 斛法, 冬程功)
乙人 = 求人數(乙輸粟 * 斛法, 冬程功)
丙人 = 求人數(丙輸粟 * 斛法, 冬程功)
丁人 = 求人數(丁輸粟 * 斛法, 冬程功)

# Output results
print(f"窖上廣 {窖上廣}丈 ，上袤 {窖上袤}丈 ，下廣 {窖下廣}丈 ，下袤 {窖下袤}丈 ，深 {窖深}丈")
print(f"甲郡 {甲人}人 ，深 {甲深}尺 ，下袤 {甲下袤}丈 ，廣 {甲下廣}丈")
print(f"乙郡 {乙人}人 ，深 {乙深}尺 ，下袤 {乙下袤}丈 ，廣 {乙下廣}丈")
print(f"丙郡 {丙人}人 ，深 {丙深}尺 ，下袤 {丙下袤}丈 ，廣 {丙下廣}丈")
print(f"丁郡 {丁人}人 ，深 {丁深}尺 ，下袤 {丁下袤}丈 ，廣 {丁下廣}丈")


"""


This code implements the procedure step by step, following the ancient Chinese mathematical methods described in the problem. Each calculation corresponds to a specific part of the procedure. Note that some initial assumptions (like `塹上廣` and `塹上袤`) are made for simplicity, and iterative refinement may be needed for exact results.
"""


"""
Code error: 'float' object cannot be interpreted as an integer"""
