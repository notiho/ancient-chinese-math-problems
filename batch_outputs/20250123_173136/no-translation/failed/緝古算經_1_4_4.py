"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is highly complex and involves multiple steps of ancient Chinese mathematical procedures. It requires breaking down the problem into smaller parts and systematically solving each step. Below is the Python code representation of the procedure described in the problem. I will follow the structure of the procedure ("術") and use the `Fraction` class to ensure accuracy.


"""


from fractions import Fraction
from math import sqrt

# Constants
程功 = Fraction(3, 7)  # 每人程功常積三尺七寸二分
限日 = 96  # 限九十六日役

# 人數
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944

# 河的數據
袤 = 276  # 一里二百七十六步
北頭深 = Fraction(18, 1) + Fraction(6, 10)  # 一丈八尺六寸
南頭深 = Fraction(241, 1) + Fraction(8, 10)  # 二百四十一尺八寸
北頭上廣 = Fraction(12, 1) + Fraction(24, 10)  # 十二步二尺四寸
南頭上廣 = Fraction(86, 1) + Fraction(48, 10)  # 八十六步四尺八寸
下廣 = Fraction(6, 1) + Fraction(12, 10)  # 六步一尺二寸

# 漘的數據
北頭高 = Fraction(223, 1) + Fraction(2, 10)  # 二百二十三尺二寸
南頭高 = 0  # 南頭無高
漘下廣 = Fraction(406, 1) + Fraction(75, 100)  # 四百六尺七寸五厘

# Step 1: 計算甲郡的積
甲積 = (程功 * 甲郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)

# Step 2: 計算甲郡的正袤
甲法 = (北頭上廣 - 下廣) * (北頭深 - 南頭深)
甲正袤 = sqrt(float(甲積 / 甲法))

# Step 3: 計算甲郡的上廣
甲上廣 = ((北頭上廣 - 南頭上廣) * 甲正袤 / 袤) + 北頭上廣

# Step 4: 計算甲郡的深
甲深 = ((北頭深 - 南頭深) * 甲正袤 / 袤) + 北頭深

# Step 5: 計算甲郡的斜袤
甲斜袤 = sqrt(float(甲正袤**2 + (北頭深 - 南頭深)**2))

# Step 6: 計算乙郡的數據
乙積 = (程功 * 乙郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)
乙正袤 = sqrt(float(乙積 / 甲法))
乙上廣 = ((北頭上廣 - 南頭上廣) * 乙正袤 / 袤) + 北頭上廣
乙深 = ((北頭深 - 南頭深) * 乙正袤 / 袤) + 北頭深
乙斜袤 = sqrt(float(乙正袤**2 + (北頭深 - 南頭深)**2))

# Step 7: 計算丙郡的數據
丙積 = (程功 * 丙郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)
丙正袤 = sqrt(float(丙積 / 甲法))
丙上廣 = ((北頭上廣 - 南頭上廣) * 丙正袤 / 袤) + 北頭上廣
丙深 = ((北頭深 - 南頭深) * 丙正袤 / 袤) + 北頭深
丙斜袤 = sqrt(float(丙正袤**2 + (北頭深 - 南頭深)**2))

# Step 8: 計算丁郡的數據
丁積 = (程功 * 丁郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)
丁正袤 = sqrt(float(丁積 / 甲法))
丁上廣 = ((北頭上廣 - 南頭上廣) * 丁正袤 / 袤) + 北頭上廣
丁深 = ((北頭深 - 南頭深) * 丁正袤 / 袤) + 北頭深
丁斜袤 = sqrt(float(丁正袤**2 + (北頭深 - 南頭深)**2))

# Step 9: 計算漘上廣
總人 = 甲郡人 + 乙郡人 + 丙郡人 + 丁郡人
漘積 = (程功 * 總人 * 限日) * Fraction(6, 1)
漘上廣 = ((漘積 / (袤 * 北頭高)) - 漘下廣) / 2

# Results
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i = 乙正袤, 乙斜袤, 乙上廣, 乙深
j, k, l, m = 丙正袤, 丙斜袤, 丙上廣, 丙深
n, o, p, q = 丁正袤, 丁斜袤, 丁上廣, 丁深

# Output
print(f"漘上廣: {a}丈")
print(f"甲郡正袤: {b}丈, 斜袤: {c}丈, 上廣: {d}丈, 深: {e}丈")
print(f"乙郡正袤: {f}丈, 斜袤: {g}丈, 上廣: {h}丈, 深: {i}丈")
print(f"丙郡正袤: {j}丈, 斜袤: {k}丈, 上廣: {l}丈, 深: {m}丈")
print(f"丁郡正袤: {n}丈, 斜袤: {o}丈, 上廣: {p}丈, 深: {q}丈")


"""


This code follows the procedure step by step, using the given data to calculate the required values for each郡 (region) and the漘 (embankment). Note that the calculations involve fractions and square roots, and the results are expressed in丈 (Chinese unit of length).
"""


"""
Code error: math domain error"""
