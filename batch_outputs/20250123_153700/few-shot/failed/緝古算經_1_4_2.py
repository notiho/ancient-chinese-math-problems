"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is extremely complex and involves multiple calculations for various geometric and labor-related aspects of the task. It requires breaking down the procedure into smaller steps and encoding each part systematically. Below is the Python code that follows the procedure ("術") described in the problem.


"""


from fractions import Fraction
import math

# Helper function to calculate square root for斜袤
def 開平方(value):
    return Fraction(math.sqrt(value))

# Constants and inputs
袤 = Fraction(1, 2) * 276  # 袤一里二百七十六步
北頭深 = Fraction(1, 10) * (1 * 10 + 8 * 10 + 6)  # 北頭深一丈八尺六寸
南頭深 = Fraction(1, 10) * (241 * 10 + 8)  # 南頭深二百四十一尺八寸
北頭上廣 = Fraction(1, 10) * (12 * 10 + 2 * 10 + 4)  # 北頭上廣十二步二尺四寸
南頭上廣 = Fraction(1, 10) * (86 * 10 + 4 * 10 + 8)  # 南頭上廣八十六步四尺八寸
下廣 = Fraction(1, 10) * (6 * 10 + 1 * 10 + 2)  # 下廣六步一尺二寸
程功 = Fraction(1, 10) * (3 * 10 + 7 * 10 + 2)  # 程功常積三尺七寸二分
限日 = 96  # 限九十六日役
甲郡人 = 22320  # 甲郡人數
乙郡人 = 68076  # 乙郡人數
丙郡人 = 59985  # 丙郡人數
丁郡人 = 37944  # 丁郡人數
漘北頭高 = Fraction(1, 10) * (223 * 10 + 2)  # 北頭高二百二十三尺二寸
漘南頭高 = 0  # 南頭無高
漘下廣 = Fraction(1, 10) * (406 * 10 + 7 * 10 + 5)  # 下廣四百六尺七寸五厘

# Step 1: Calculate total work for each郡
def 計算積(人數, 程功, 限日):
    return Fraction(人數 * 程功 * 限日, 4 * 3)

甲積 = 計算積(甲郡人, 程功, 限日)
乙積 = 計算積(乙郡人, 程功, 限日)
丙積 = 計算積(丙郡人, 程功, 限日)
丁積 = 計算積(丁郡人, 程功, 限日)

# Step 2: Calculate正袤,斜袤,上廣, and深 for each郡
def 計算正袤(積, 袤, 上廣差, 深差):
    法 = 上廣差 * 深差
    return Fraction(積 * 6 * 袤, 法)

def 計算上廣(小頭上廣, 兩頭上廣差, 正袤, 本袤):
    return 小頭上廣 + Fraction(兩頭上廣差 * 正袤, 本袤)

def 計算深(小頭深, 南頭深, 正袤, 本袤):
    return 小頭深 + Fraction((南頭深 - 小頭深) * 正袤, 本袤)

def 計算斜袤(正袤, 深差):
    return 開平方(正袤**2 + 深差**2)

# 甲郡計算
甲正袤 = 計算正袤(甲積, 袤, 北頭上廣 - 下廣, 北頭深 - 南頭深)
甲上廣 = 計算上廣(下廣, 北頭上廣 - 下廣, 甲正袤, 袤)
甲深 = 計算深(北頭深, 南頭深, 甲正袤, 袤)
甲斜袤 = 計算斜袤(甲正袤, 北頭深 - 南頭深)

# 乙郡計算
乙正袤 = 計算正袤(乙積, 袤, 北頭上廣 - 下廣, 北頭深 - 南頭深)
乙上廣 = 計算上廣(下廣, 北頭上廣 - 下廣, 乙正袤, 袤)
乙深 = 計算深(北頭深, 南頭深, 乙正袤, 袤)
乙斜袤 = 計算斜袤(乙正袤, 北頭深 - 南頭深)

# 丙郡計算
丙正袤 = 計算正袤(丙積, 袤, 北頭上廣 - 下廣, 北頭深 - 南頭深)
丙上廣 = 計算上廣(下廣, 北頭上廣 - 下廣, 丙正袤, 袤)
丙深 = 計算深(北頭深, 南頭深, 丙正袤, 袤)
丙斜袤 = 計算斜袤(丙正袤, 北頭深 - 南頭深)

# 丁郡計算
丁正袤 = 計算正袤(丁積, 袤, 北頭上廣 - 下廣, 北頭深 - 南頭深)
丁上廣 = 計算上廣(下廣, 北頭上廣 - 下廣, 丁正袤, 袤)
丁深 = 計算深(北頭深, 南頭深, 丁正袤, 袤)
丁斜袤 = 計算斜袤(丁正袤, 北頭深 - 南頭深)

# Step 3: Calculate漘上廣
def 計算漘上廣(總人, 程功, 限日, 正袤, 高, 下廣):
    總積 = 總人 * 程功 * 限日
    實 = 總積 * 6
    return Fraction(實, 正袤 * 高) - Fraction(下廣, 2)

漘上廣 = 計算漘上廣(甲郡人 + 乙郡人 + 丙郡人 + 丁郡人, 程功, 限日, 袤, 漘北頭高, 漘下廣)

# Final answers
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


This code follows the procedure step by step, calculating the required values for each郡 (region) and the漘 (embankment). The results are printed at the end. Note that all calculations use `Fraction` to ensure precision, and the square root is calculated using a helper function.
"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: 3285779/92
Variable 'b' has wrong value. Expected: 144, Actual: -38787200/43
Variable 'c' has wrong value. Expected: 1443/10, Actual: 242136280556613/268435456
Variable 'd' has wrong value. Expected: 651/25, Actual: -10116852/215
Variable 'e' has wrong value. Expected: 279/25, Actual: -7588752/5
Variable 'f' has wrong value. Expected: 576/5, Actual: -118300960/43
Variable 'g' has wrong value. Expected: 2886/25, Actual: 5908125070873127/2147483648
Variable 'h' has wrong value. Expected: 1023/25, Actual: -30859572/215
Variable 'i' has wrong value. Expected: 93/5, Actual: -23145792/5
Variable 'j' has wrong value. Expected: 288/5, Actual: -2424200
Variable 'k' has wrong value. Expected: 1443/25, Actual: 162685308855087/67108864
Variable 'l' has wrong value. Expected: 1209/25, Actual: -632364/5
Variable 'm' has wrong value. Expected: 558/25, Actual: -20394852/5
Variable 'n' has wrong value. Expected: 144/5, Actual: -65938240/43
Variable 'o' has wrong value. Expected: 1443/50, Actual: 6586106688432243/4294967296
Variable 'p' has wrong value. Expected: 1302/25, Actual: -17199732/215
Variable 'q' has wrong value. Expected: 1209/50, Actual: -12900912/5"""
