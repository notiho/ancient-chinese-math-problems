"""
假令四郡輸粟，斛法二尺五寸，一人作功為均。自上給甲，以次與乙。其甲郡輸粟三萬八千七百四十五石六斗，乙郡輸粟三萬四千九百五石六斗，丙郡輸粟，二萬六千二百七十石四斗，丁郡輸粟一萬四千七十八石四斗。四郡共穿窖，上袤多於上廣一丈，少於下袤三丈，多於深六丈，少於下廣一丈。各計粟多少，均出丁夫。自穿、負、築，冬程人功常積一十二尺，一日役。問：窖上下廣、袤、深，郡別出人及窖深、廣各多少？
求窖深、廣、袤，術曰：以斛法乘總粟，為積尺。又廣差乘袤差，三而一，為隅陽冪。乃置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪。又半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法。又置塹上袤及塹上廣，並之，為大廣。又並廣差及袤差，半之，以加大廣，為廉法，從。開立方除之，即深。各加差，即合所問。求均給積尺受廣、袤、深，術曰：如築臺術入之。以斛法乘甲郡輸粟，為積尺。又三因，以深冪乘之，以廣差乘袤差而一，為實。深乘上廣，廣差而一，為上廣之高。深乘上袤，袤差而一，為上袤之高。上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即甲深。以袤差乘之，以本深除之，所加上袤，即甲下袤。以廣差乘之，本深除之，所得加上廣，即甲下廣。若求乙、丙、丁，每以前下廣、袤為後上廣、袤，以次皆準此求之，即得。若求人數，各以程功約當郡積尺。
答曰：窖上廣 a丈 ，上袤 b丈 ，下廣 c丈 ，下袤 d丈 ，深 e丈 ；甲郡 f人 ，深 g尺 ，下袤 h丈 ，廣 i丈 ；乙郡 j人 ，深 k尺 ，下袤 l丈 ，廣 m丈 ；丙郡 n人 ，深 o尺 ，下袤 p丈 ，廣 q丈 ；丁郡 r人 ，深 s尺 ，下袤 t丈 ，廣 u丈 。
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. I'll break it down into sections and encode the solution step by step in Python. The solution will follow the structure of the procedure ("術") provided.


"""

#----- content starts here -----

from fractions import Fraction
import math

# 四郡輸粟
甲粟 = 38745 + Fraction(6, 10)  # 石
乙粟 = 34905 + Fraction(6, 10)  # 石
丙粟 = 26270 + Fraction(4, 10)  # 石
丁粟 = 14078 + Fraction(4, 10)  # 石

# 斛法二尺五寸
斛法 = Fraction(25, 10)  # 尺

# 冬程人功常積一十二尺，一日役
人功 = 12  # 尺

# 窖上下廣、袤、深的差
上廣差 = 1  # 丈
下袤差 = 3  # 丈
深差 = 6  # 丈
下廣差 = 1  # 丈

# 四郡總粟
總粟 = 甲粟 + 乙粟 + 丙粟 + 丁粟

# 求窖深、廣、袤
# 以斛法乘總粟，為積尺
積尺 = 總粟 * 斛法

# 廣差乘袤差，三而一，為隅陽冪
隅陽冪 = Fraction(上廣差 * 下袤差, 3)

# 置塹上廣，半廣差加之，以乘塹上袤，為隅頭冪
塹上廣 = 1  # 初始假設上廣為 1 丈
塹上袤 = 1  # 初始假設上袤為 1 丈
隅頭冪 = (塹上廣 + Fraction(上廣差, 2)) * 塹上袤

# 半袤差，乘塹上廣，以隅陽冪及隅頭冪加之，為方法
方法 = (Fraction(下袤差, 2) * 塹上廣) + 隅陽冪 + 隅頭冪

# 置塹上袤及塹上廣，並之，為大廣
大廣 = 塹上袤 + 塹上廣

# 並廣差及袤差，半之，以加大廣，為廉法
廉法 = 大廣 + Fraction(上廣差 + 下袤差, 2)

# 開立方除之，即深
深 = (積尺 / 方法) ** Fraction(1, 3)

# 各加差，即合所問
窖深 = 深 + 深差
窖上廣 = 塹上廣
窖上袤 = 塹上袤
窖下廣 = 塹上廣 + 下廣差
窖下袤 = 塹上袤 + 下袤差

# 求均給積尺受廣、袤、深
def 計算郡(郡粟, 上廣, 上袤, 深):
    # 以斛法乘郡輸粟，為積尺
    積尺 = 郡粟 * 斛法

    # 三因，以深冪乘之，以廣差乘袤差而一，為實
    實 = (深 ** 3) * Fraction(上廣差 * 下袤差, 3)

    # 深乘上廣，廣差而一，為上廣之高
    上廣之高 = 深 * 上廣 * Fraction(上廣差, 3)

    # 深乘上袤，袤差而一，為上袤之高
    上袤之高 = 深 * 上袤 * Fraction(下袤差, 3)

    # 上廣之高乘上袤之高，三之，為方法
    方法 = (上廣之高 * 上袤之高) * Fraction(1, 3)

    # 並兩高，三之，二而一，為廉法
    廉法 = (上廣之高 + 上袤之高) * Fraction(3, 2)

    # 開立方除之，即郡深
    郡深 = (積尺 / 方法) ** Fraction(1, 3)

    # 以袤差乘之，以本深除之，所加上袤，即郡下袤
    郡下袤 = 上袤 + (下袤差 * 郡深 / 深)

    # 以廣差乘之，本深除之，所得加上廣，即郡下廣
    郡下廣 = 上廣 + (上廣差 * 郡深 / 深)

    return 郡深, 郡下袤, 郡下廣

# 計算各郡
甲深, 甲下袤, 甲下廣 = 計算郡(甲粟, 窖上廣, 窖上袤, 窖深)
乙深, 乙下袤, 乙下廣 = 計算郡(乙粟, 甲下廣, 甲下袤, 甲深)
丙深, 丙下袤, 丙下廣 = 計算郡(丙粟, 乙下廣, 乙下袤, 乙深)
丁深, 丁下袤, 丁下廣 = 計算郡(丁粟, 丙下廣, 丙下袤, 丙深)

# 計算人數
甲人 = math.ceil(甲粟 * 斛法 / 人功)
乙人 = math.ceil(乙粟 * 斛法 / 人功)
丙人 = math.ceil(丙粟 * 斛法 / 人功)
丁人 = math.ceil(丁粟 * 斛法 / 人功)

# 答案
a = 窖上廣
b = 窖上袤
c = 窖下廣
d = 窖下袤
e = 窖深
f = 甲人
g = 甲深
h = 甲下袤
i = 甲下廣
j = 乙人
k =乙深#----- content ends here -----


"""

"""


"""
Variable 'a' has wrong value. Expected: 8, Actual: 1
Variable 'b' has wrong value. Expected: 9, Actual: 1
Variable 'c' has wrong value. Expected: 10, Actual: 2
Variable 'd' has wrong value. Expected: 12, Actual: 4
Variable 'e' has wrong value. Expected: 3, Actual: 47.45672170924848
Variable 'g' has wrong value. Expected: 12, Actual: 7.28791245141519
Variable 'h' has wrong value. Expected: 51/5, Actual: 1.4607089694942985
Variable 'i' has wrong value. Expected: 44/5, Actual: 1.1535696564980995
Variable 'k' has wrong value. Expected: 9, Actual: 20.626297179113948
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
