"""
假令穿河袤一裏二百七十六步下廣六步一尺二寸北頭深一丈八尺六寸上廣十二步二尺四寸南頭深二百四十一尺八寸上廣八十六步四尺八寸運土於河西岸造漘北頭高二百二十三尺二寸南頭無高下廣四百六尺七寸五厘袤與河同甲郡二萬二千三百二十人乙郡六萬八千七十六人丙郡五萬九千九百八十五人丁郡三萬七千九百四十四人自穿負築各人程功常積三尺七寸二分限九十六日役河漘俱了四郡分共造漘其河自北頭先給甲郡以次與乙合均賦積尺問逐郡各給斜正袤上廣及深並漘上廣各多少
術曰如築堤術入之以程功乘甲郡人又以限日乘之四之三而一為積又六因以乘袤冪以上廣差乘深差為法除之為實又並小頭上下廣以乘小頭深三之為垣頭冪又乘袤冪以法除之為垣方三因小頭上廣以乘正袤以廣差除之為都廉從開立方除之即得小頭袤為甲袤求深廣以本袤及深廣差求之以兩頭上廣差乘甲袤以本袤除之所得加小頭上廣即甲上廣以小頭深減南頭深余以乘甲袤以本袤除之所得加小頭深即甲深又正袤自乘深差自乘並而開方除之即斜袤若求乙丙丁每以前大深廣為後小深廣準甲求之即得求漘上廣術曰以程功乘總人又以限日乘之為積六因之為實以正袤除之又以高除之所得以下廣減之余又半之即漘上廣
答曰漘上廣 a丈 甲郡正袤 b丈 斜袤 c丈 上廣 d丈 深 e丈 乙郡正袤 f丈 斜袤 g丈 上廣 h丈 深 i丈 丙郡正袤 j丈 斜袤 k丈 上廣 l丈 深 m丈 丁郡正袤 n丈 斜袤 o丈 上廣 p丈 深 q丈 
"""

"""
This problem is highly complex and involves multiple steps of calculation, including geometric relationships, proportional distribution, and iterative calculations for each of the four regions (甲, 乙, 丙, 丁). Translating this into Python code requires breaking down the procedure into manageable steps and encoding each part of the procedure as described in the problem.

Below is the Python implementation of this problem, following the structure of the procedure ("術") provided:


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants and initial values
程功 = Fraction(3, 7)  # 常積三尺七寸二分
限日 = 96  # 限九十六日
總人 = 22320 + 68076 + 59985 + 37944  # 四郡總人數
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944

# 河的初始數據
河袤 = 1 * 300 + 276  # 一里二百七十六步
小頭廣 = 6 + Fraction(1, 10) * (1 * 10 + 2)  # 下廣六步一尺二寸
小頭深 = 1 * 10 + 8 + Fraction(1, 10) * 6  # 北頭深一丈八尺六寸
南頭深 = 241 + Fraction(1, 10) * 8  # 南頭深二百四十一尺八寸
南頭廣 = 86 + Fraction(1, 10) * (4 * 10 + 8)  # 上廣八十六步四尺八寸

# 漘的初始數據
漘北頭高 = 223 + Fraction(1, 10) * 2  # 北頭高二百二十三尺二寸
漘南頭高 = 0  # 南頭無高
漘下廣 = 406 + Fraction(1, 10) * (7 * 10 + 5)  # 下廣四百六尺七寸五厘
漘袤 = 河袤  # 漘袤與河同

# Helper function to calculate geometric relationships
def calculate_郡(郡人, 本袤, 小頭廣, 小頭深, 南頭廣, 南頭深, 程功, 限日):
    # Step 1: Calculate the total accumulated volume for the 郡
    積 = 程功 * 郡人 * 限日 * Fraction(4, 3)

    # Step 2: Calculate the divisor (法)
    法 = 6 * 本袤 * (南頭廣 - 小頭廣) * (南頭深 - 小頭深)

    # Step 3: Calculate 正袤
    正袤 = 積 / 法

    # Step 4: Calculate 上廣 and 深
    上廣 = 小頭廣 + (南頭廣 - 小頭廣) * 正袤 / 本袤
    深 = 小頭深 + (南頭深 - 小頭深) * 正袤 / 本袤

    # Step 5: Calculate 斜袤
    斜袤 = sqrt(正袤**2 + (深 - 小頭深)**2)

    return 正袤, 斜袤, 上廣, 深

# Step 1: Calculate for 甲郡
甲正袤, 甲斜袤, 甲上廣, 甲深 = calculate_郡(甲郡人, 河袤, 小頭廣, 小頭深, 南頭廣, 南頭深, 程功, 限日)

# Step 2: Calculate for 乙郡
乙正袤, 乙斜袤, 乙上廣, 乙深 = calculate_郡(乙郡人, 河袤, 小頭廣, 小頭深, 南頭廣, 南頭深, 程功, 限日)

# Step 3: Calculate for 丙郡
丙正袤, 丙斜袤, 丙上廣, 丙深 = calculate_郡(丙郡人, 河袤, 小頭廣, 小頭深, 南頭廣, 南頭深, 程功, 限日)

# Step 4: Calculate for 丁郡
丁正袤, 丁斜袤, 丁上廣, 丁深 = calculate_郡(丁郡人, 河袤, 小頭廣, 小頭深, 南頭廣, 南頭深, 程功, 限日)

# 漘上廣 calculation
漘積 = 程功 * 總人 * 限日
漘實 = 漘積 * 6
漘上廣 = (漘實 / (漘袤 * 漘北頭高)) - 漘下廣
漘上廣 = 漘上廣 / 2

# Final answers
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i = 乙正袤, 乙斜袤, 乙上廣, 乙深
j, k, l, m = 丙正袤, 丙斜袤, 丙上廣, 丙深
n, o, p, q = 丁正袤, 丁斜袤, 丁上廣, 丁深

# Output results
print(f"漘上廣: {a} 丈")
print(f"甲郡正袤: {b} 丈, 斜袤: {c} 丈, 上廣: {d} 丈, 深: {e} 丈")
print(f"乙郡正袤: {f} 丈, 斜袤: {g} 丈, 上廣: {h} 丈, 深: {i} 丈")
print(f"丙郡正袤: {j} 丈, 斜袤: {k} 丈, 上廣: {l} 丈, 深: {m} 丈")
print(f"丁郡正袤: {n} 丈, 斜袤: {o} 丈, 上廣: {p} 丈, 深: {q} 丈")
#----- content ends here -----


"""


This code follows the procedure step by step, calculating the required values for each 郡 (region) and the 漘 (embankment). Each calculation is based on the relationships and formulas provided in the problem description.
"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: -1453/56
Variable 'b' has wrong value. Expected: 144, Actual: 250/13167
Variable 'c' has wrong value. Expected: 1443/10, Actual: 0.020362523333714636
Variable 'd' has wrong value. Expected: 651/25, Actual: 326717/45360
Variable 'e' has wrong value. Expected: 279/25, Actual: 9800123/526680
Variable 'f' has wrong value. Expected: 576/5, Actual: 1525/26334
Variable 'g' has wrong value. Expected: 2886/25, Actual: 0.062105696167829634
Variable 'h' has wrong value. Expected: 1023/25, Actual: 1307893/181440
Variable 'i' has wrong value. Expected: 93/5, Actual: 39232267/2106720
Variable 'j' has wrong value. Expected: 288/5, Actual: 5375/105336
Variable 'k' has wrong value. Expected: 1443/25, Actual: 0.054724281459358086
Variable 'l' has wrong value. Expected: 1209/25, Actual: 5230847/725760
Variable 'm' has wrong value. Expected: 558/25, Actual: 156906593/8426880
Variable 'n' has wrong value. Expected: 144/5, Actual: 425/13167
Variable 'o' has wrong value. Expected: 1443/50, Actual: 0.03461628966731488
Variable 'p' has wrong value. Expected: 1302/25, Actual: 653609/90720
Variable 'q' has wrong value. Expected: 1209/50, Actual: 19605671/1053360"""
