"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is extremely complex and involves multiple steps, including calculations for volumes, areas, and geometric relationships. It also requires iterative calculations for each of the four regions (甲, 乙, 丙, 丁) and their respective parameters. Below is the Python code implementing the procedure step by step:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants
程功 = Fraction(3, 7, 2)  # 每人程功常積三尺七寸二分
限日 = 96  # 限九十六日役

# 人數
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944

# 河的參數
袤 = 276  # 袤一里二百七十六步
小頭下廣 = Fraction(6, 1, 2)  # 下廣六步一尺二寸
小頭深 = Fraction(1, 8, 6)  # 北頭深一丈八尺六寸
小頭上廣 = Fraction(12, 2, 4)  # 上廣十二步二尺四寸
南頭深 = Fraction(241, 8)  # 南頭深二百四十一尺八寸
南頭上廣 = Fraction(86, 4, 8)  # 上廣八十六步四尺八寸

# 漘的參數
北頭高 = Fraction(223, 2)  # 北頭高二百二十三尺二寸
南頭高 = 0  # 南頭無高
漘下廣 = Fraction(406, 7, 5)  # 下廣四百六尺七寸五厘
漘袤 = 袤  # 袤與河同

# Step 1: Calculate total work for each 郡
def calculate_total_work(people, days, work_per_person):
    return Fraction(people * days * work_per_person, 4, 3)

甲積 = calculate_total_work(甲郡人, 限日, 程功)
乙積 = calculate_total_work(乙郡人, 限日, 程功)
丙積 = calculate_total_work(丙郡人, 限日, 程功)
丁積 = calculate_total_work(丁郡人, 限日, 程功)

# Step 2: Calculate 河 parameters for 甲郡
def calculate_river_params(袤, 小頭上廣, 小頭深, 南頭上廣, 南頭深, 積):
    # Calculate 法
    上廣差 = 南頭上廣 - 小頭上廣
    深差 = 南頭深 - 小頭深
    法 = 上廣差 * 深差

    # Calculate 正袤
    正袤 = 積 / 法

    # Calculate 上廣
    上廣 = 小頭上廣 + (上廣差 * 正袤 / 袤)

    # Calculate 深
    深 = 小頭深 + (深差 * 正袤 / 袤)

    # Calculate 斜袤
    斜袤 = sqrt(正袤**2 + 深差**2)

    return 正袤, 斜袤, 上廣, 深

甲正袤, 甲斜袤, 甲上廣, 甲深 = calculate_river_params(袤, 小頭上廣, 小頭深, 南頭上廣, 南頭深, 甲積)

# Step 3: Calculate 河 parameters for 乙郡, 丙郡, 丁郡
乙正袤, 乙斜袤, 乙上廣, 乙深 = calculate_river_params(袤 - 甲正袤, 甲上廣, 甲深, 南頭上廣, 南頭深, 乙積)
丙正袤, 丙斜袤, 丙上廣, 丙深 = calculate_river_params(袤 - 甲正袤 -乙正袤,乙深#----- content ends here -----


"""

"""


"""
Code error: '(' was never closed (<string>, line 64)"""
