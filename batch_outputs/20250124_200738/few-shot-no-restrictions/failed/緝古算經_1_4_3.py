"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is extremely complex and involves a detailed calculation of the dimensions and contributions of four counties (甲, 乙, 丙, 丁) in constructing a riverbank and digging a river. It requires calculating the dimensions of the river (正袤, 斜袤, 上廣, 深) and the riverbank (漘上廣) for each county based on their labor contributions and the geometric properties of the river and riverbank.

Below is the Python implementation of this problem, broken into steps for clarity. We'll use the `Fraction` class to handle precise calculations and ensure accuracy.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants and inputs
# 河 dimensions
袤 = Fraction(1, 2) * (300 + 276)  # 袤 = 1里2百76步 = 300步 + 276步
北頭深 = Fraction(1, 2) * (10 + 8) + Fraction(6, 10)  # 北頭深 = 1丈8尺6寸
南頭深 = Fraction(241, 10) + Fraction(8, 10)  # 南頭深 = 241尺8寸
北頭上廣 = Fraction(12, 2) + Fraction(4, 10)  # 北頭上廣 = 12步2尺4寸
南頭上廣 = Fraction(86, 2) + Fraction(4, 10)  # 南頭上廣 = 86步4尺8寸
北頭下廣 = Fraction(6, 2) + Fraction(2, 10)  # 北頭下廣 = 6步1尺2寸
南頭下廣 = Fraction(8, 2) + Fraction(4, 10)  # 南頭下廣 = 8步4尺8寸

# 漘 dimensions
北頭高 = Fraction(223, 10) + Fraction(2, 10)  # 北頭高 = 223尺2寸
南頭高 = 0  # 南頭無高
漘下廣 = Fraction(406, 10) + Fraction(7, 10) + Fraction(5, 100)  # 漘下廣 = 406尺7寸5厘

# Labor inputs
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944
總人 = 甲郡人 + 乙郡人 + 丙郡人 + 丁郡人

# 工程 inputs
程功 = Fraction(3, 2) + Fraction(7, 10) + Fraction(2, 100)  # 每人程功 = 3尺7寸2分
限日 = 96  # 限日 = 96日

# Helper functions
def calculate_正袤_斜袤_上廣_深(小頭深, 小頭上廣, 小頭下廣, 大頭深, 大頭上廣, 大頭下廣, 人數, 總人數, 本袤, 深差, 廣差):
    """
    Calculate 正袤, 斜袤, 上廣, and 深 for a given county.
    """
    # Calculate 正袤
    積 = 程功 * 人數 * 限日
    積 = 積 * 6  # 六因之
    正袤 = 積 / (本袤 * 深差 * 廣差)

    # Calculate 上廣
    上廣 = 小頭上廣 + (廣差 * 正袤 / 本袤)

    # Calculate 深
    深 = 小頭深 + (深差 * 正袤 / 本袤)

    # Calculate 斜袤
    斜袤 = sqrt(正袤**2 + 深差**2)

    return 正袤, 斜袤, 上廣, 深

# Step 1: Calculate 差 values
深差 = 北頭深 - 南頭深
廣差 = 北頭上廣 - 南頭上廣

# Step 2: Calculate 正袤, 斜袤, 上廣, and 深 for 甲郡
甲正袤, 甲斜袤, 甲上廣, 甲深 = calculate_正袤_斜袤_上廣_深(
    小頭深=北頭深,
    小頭上廣=北頭上廣,
    小頭下廣=北頭下廣,
    大頭深=南頭深,
    大頭上廣=南頭上廣,
    大頭下廣=南頭下廣,
    人數=甲郡人,
    總人數=總人,
    本袤=袤,
    深差=深差,
    廣差=廣差
)

# Step 3: Calculate 正袤, 斜袤, 上廣, and 深 for 乙郡
乙正袤, 乙斜袤, 乙上廣, 乙深 = calculate_正袤_斜袤_上廣_深(
    小頭深=甲深,
    小頭上廣=甲上廣,
    小頭下廣=北頭下廣,
    大頭深=南頭深,
    大頭上廣=南頭上廣,
    大頭下廣=南頭下廣,
    人數=乙郡人,
    總人數=總人,
    本袤=袤,
    深差=深差,
    廣差=廣差
)

# Step 4: Calculate 漘上廣
漘積 = 程功 * 總人 * 限日
漘積 = 漘積 * 6  # 六因之
漘實 = 漘積 / 袤
漘上廣 = (漘實 / 北頭高 - 漘下廣) / 2

# Output results
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i =乙#----- content ends here -----


"""

"""


"""
Code error: name '乙' is not defined"""
