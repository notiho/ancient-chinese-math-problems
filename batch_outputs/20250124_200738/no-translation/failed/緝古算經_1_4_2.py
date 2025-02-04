"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is extremely complex and involves multiple steps of calculations, including volumetric calculations, proportional distribution, and iterative computations for each of the four regions. Translating this into Python code while adhering strictly to the ancient Chinese mathematical procedure is a significant task. Below is the Python implementation of the procedure described in the problem:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants and inputs
袤 = Fraction(1, 2) * 276  # 袤一里二百七十六步
小頭下廣 = Fraction(6, 1) + Fraction(1, 10) * 2  # 下廣六步一尺二寸
北頭深 = Fraction(10, 1) + Fraction(1, 10) * 8 + Fraction(1, 100) * 6  # 北頭深一丈八尺六寸
北頭上廣 = Fraction(12, 1) + Fraction(1, 10) * 2 + Fraction(1, 100) * 4  # 上廣十二步二尺四寸
南頭深 = Fraction(241, 1) + Fraction(1, 10) * 8  # 南頭深二百四十一尺八寸
南頭上廣 = Fraction(86, 1) + Fraction(1, 10) * 4 + Fraction(1, 100) * 8  # 上廣八十六步四尺八寸
漘下廣 = Fraction(406, 1) + Fraction(1, 10) * 7 + Fraction(1, 1000) * 5  # 下廣四百六尺七寸五厘
北頭高 = Fraction(223, 1) + Fraction(1, 10) * 2  # 北頭高二百二十三尺二寸
總人 = Fraction(22320 + 68076 + 59985 + 37944, 1)  # 四郡總人數
程功 = Fraction(3, 1) + Fraction(1, 10) * 7 + Fraction(1, 100) * 2  # 程功常積三尺七寸二分
限日 = 96  # 限九十六日役

# Step 1: Calculate total volume (積)
積 = (程功 * 總人 * 限日) / 4 * 3

# Step 2: Calculate 漘上廣
漘實 = 積 * 6
漘正袤 = 袤
漘上廣 = ((漘實 / 漘正袤) / 北頭高 - 漘下廣) / 2

# Step 3: Calculate for 甲郡
甲人 = 22320
甲積 = (程功 * 甲人 * 限日) / 4 * 3
甲袤冪 = 袤 ** 2
甲法 = (北頭上廣 - 小頭下廣) * (北頭深 - 南頭深)
甲實 = 甲積 * 6 * 袤冪 / 甲法
甲垣頭冪 = ((北頭上廣 + 小頭下廣) * 北頭深) / 3
甲垣方 = (甲垣頭冪 * 袤冪) / 甲法
甲都廉 = (3 * 北頭上廣 * 袤) / (北頭上廣 - 小頭下廣)
甲正袤 = sqrt(甲都廉)
甲深 = (北頭深 - 南頭深) * (甲正袤 / 袤) + 北頭深
甲上廣 = (北頭上廣 - 小頭下廣) * (甲正袤 / 袤) + 小頭下廣
甲斜袤 = sqrt(甲正袤 ** 2 + (北頭深 - 南頭深) ** 2)

# Step 4: Calculate for 乙郡, 丙郡, 丁郡
乙人 = 68076
丙人 = 59985
丁人 = 37944

乙正袤 = (乙人 / 總人) * 袤
丙正袤 = (丙人 / 總人) * 袤
丁正袤 = (丁人 / 總人) * 袤

乙深 = (北頭深 - 南頭深) * (乙正袤 / 袤) + 北頭深
丙深 = (北頭深 - 南頭深) * (丙正袤 / 袤) + 北頭深
丁深 = (北頭深 - 南頭深) * (丁正袤 / 袤) + 北頭深

乙上廣 = (北頭上廣 - 小頭下廣) * (乙正袤 / 袤) + 小頭下廣
丙上廣 = (北頭上廣 - 小頭下廣) * (丙正袤 / 袤) + 小頭下廣
丁上廣 = (北頭上廣 - 小頭下廣) * (丁正袤 / 袤) + 小頭下廣

乙斜袤 = sqrt(乙正袤 ** 2 + (北頭深 - 南頭深) ** 2)
丙斜袤 = sqrt(丙正袤 ** 2 + (北頭深 - 南頭深) ** 2)
丁斜袤 = sqrt(丁正袤 ** 2 + (北頭深 - 南頭深) ** 2)

# Outputs
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i = 乙正袤,乙斜袤,乙#----- content ends here -----


"""

"""


"""
Code error: name '袤冪' is not defined"""
