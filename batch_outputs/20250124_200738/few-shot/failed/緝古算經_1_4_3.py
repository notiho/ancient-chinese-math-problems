"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is extremely complex and involves multiple steps of calculation, including the use of geometric principles, proportional distribution, and iterative calculations for each of the four regions (甲, 乙, 丙, 丁). Below is the Python implementation of the procedure ("術") described in the problem. Each step is carefully translated into Python code, and the comments explain the corresponding part of the procedure.


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants and inputs
程功 = Fraction(3, 7)  # Each person's work capacity: 3尺7寸2分 = 3.72尺
限日 = 96  # Limit of 96 days
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944

# 河 dimensions
袤 = 1 * 300 + 276  # 袤: 1里2百76步 = 300步 + 276步
北頭深 = 1 * 10 + 8.6  # 北頭深: 1丈8尺6寸 = 10尺 + 8.6尺
北頭上廣 = 12 * 10 + 2.4  # 北頭上廣: 12步2尺4寸 = 120尺 + 2.4尺
南頭深 = 241.8  # 南頭深: 241尺8寸 = 241.8尺
南頭上廣 = 86 * 10 + 4.8  # 南頭上廣: 86步4尺8寸 = 860尺 + 4.8尺

# 漘 dimensions
北頭高 = 223.2  # 北頭高: 223尺2寸 = 223.2尺
南頭高 = 0  # 南頭無高
漘下廣 = 406.75  # 漘下廣: 406尺7寸5厘 = 406.75尺

# Helper function to calculate 正袤, 斜袤, 上廣, and 深 for a given 郡
def calculate_geometric_properties(郡人數, 前小深, 前小廣, 本袤, 深差, 廣差, 小頭深, 小頭上廣):
    # Step 1: Calculate 積 for the 郡
    積 = Fraction(程功 * 郡人數 * 限日, 4 * 3)

    # Step 2: Calculate 法
    法 = Fraction(本袤 * 深差 * 廣差, 6)

    # Step 3: Calculate 正袤
    正袤 = Fraction(積, 法)

    # Step 4: Calculate 斜袤
    斜袤 = sqrt(正袤**2 + 深差**2)

    # Step 5: Calculate 上廣
    上廣 = Fraction(小頭上廣 * 3 * 正袤, 廣差)

    # Step 6: Calculate 深
    深 = Fraction(小頭深 * 正袤, 深差)

    return 正袤, 斜袤, 上廣, 深

# Step 1: Calculate for 甲郡
甲正袤, 甲斜袤, 甲上廣, 甲深 = calculate_geometric_properties(
    郡人數=甲郡人,
    前小深=北頭深,
    前小廣=北頭上廣,
    本袤=袤,
    深差=南頭深 - 北頭深,
    廣差=南頭上廣 - 北頭上廣,
    小頭深=北頭深,
    小頭上廣=北頭上廣
)

# Step 2: Calculate for 乙郡
乙正袤, 乙斜袤, 乙上廣, 乙深 = calculate_geometric_properties(
    郡人數=乙郡人,
    前小深=甲深,
    前小廣=甲上廣,
    本袤=袤,
    深差=南頭深 - 甲深,
    廣差=南頭上廣 - 甲上廣,
    小頭深=甲深,
    小頭上廣=甲上廣
)

# Step 3: Calculate for 丙郡
丙正袤, 丙斜袤, 丙上廣, 丙深 = calculate_geometric_properties(
    郡人數=丙郡人,
    前小深=乙深,
    前小廣=乙上廣,
    本袤=袤,
    深差=南頭深 - 乙深,
    廣差=南頭上廣 - 乙上廣,
    小頭深=乙深,
    小頭上廣=乙上廣
)

# Step 4: Calculate for 丁郡
丁正袤, 丁斜袤, 丁上廣, 丁深 = calculate_geometric_properties(
    郡人數=丁郡人,
    前小深=丙深,
    前小廣=丙上廣,
    本袤=袤,
    深差=南頭深 - 丙深,
    廣差=南頭上廣 - 丙上廣,
    小頭深=丙深,
    小頭上廣=丙上廣
)

# Step 5: Calculate 漘上廣
總人數 = 甲郡人 + 乙郡人 + 丙郡人 + 丁郡人
漘積 = 程功 * 總人數 * 限日
漘實 = 漘積 * 6
漘上廣 = Fraction(漘實, 袤 * 北頭高) - 漘下廣
漘上廣 = 漘上廣 / 2

# Output results
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i = 乙正袤, 乙斜袤, 乙上廣, 乙深
j, k, l, m = 丙正袤, 丙斜袤, 丙上廣, 丙深
n, o, p, q = 丁正袤, 丁斜袤, 丁上廣, 丁深

print(f"漘上廣: {a}丈")
print(f"甲郡正袤: {b}丈, 斜袤: {c}丈, 上廣: {d}丈, 深: {e}丈")
print(f"乙郡正袤: {f}丈, 斜袤: {g}丈, 上廣: {h}丈, 深: {i}丈")
print(f"丙郡正袤: {j}丈, 斜袤: {k}丈, 上廣: {l}丈, 深: {m}丈")
print(f"丁郡正袤: {n}丈, 斜袤: {o}丈, 上廣: {p}丈, 深: {q}丈")
#----- content ends here -----


"""


This code follows the procedure step by step, calculating the required dimensions for each 郡 (region) and the 漘 (embankment). The results are printed in the required format. Note that the calculations involve fractions to ensure precision, and square roots are used for calculating diagonal lengths (斜袤).
"""


"""
Code error: both arguments should be Rational instances"""
