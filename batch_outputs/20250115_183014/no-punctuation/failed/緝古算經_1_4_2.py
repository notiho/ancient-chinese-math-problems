"""
假令穿河袤一裏二百七十六步下廣六步一尺二寸北頭深一丈八尺六寸上廣十二步二尺四寸南頭深二百四十一尺八寸上廣八十六步四尺八寸運土於河西岸造漘北頭高二百二十三尺二寸南頭無高下廣四百六尺七寸五厘袤與河同甲郡二萬二千三百二十人乙郡六萬八千七十六人丙郡五萬九千九百八十五人丁郡三萬七千九百四十四人自穿負築各人程功常積三尺七寸二分限九十六日役河漘俱了四郡分共造漘其河自北頭先給甲郡以次與乙合均賦積尺問逐郡各給斜正袤上廣及深並漘上廣各多少
術曰如築堤術入之以程功乘甲郡人又以限日乘之四之三而一為積又六因以乘袤冪以上廣差乘深差為法除之為實又並小頭上下廣以乘小頭深三之為垣頭冪又乘袤冪以法除之為垣方三因小頭上廣以乘正袤以廣差除之為都廉從開立方除之即得小頭袤為甲袤求深廣以本袤及深廣差求之以兩頭上廣差乘甲袤以本袤除之所得加小頭上廣即甲上廣以小頭深減南頭深余以乘甲袤以本袤除之所得加小頭深即甲深又正袤自乘深差自乘並而開方除之即斜袤若求乙丙丁每以前大深廣為後小深廣準甲求之即得求漘上廣術曰以程功乘總人又以限日乘之為積六因之為實以正袤除之又以高除之所得以下廣減之余又半之即漘上廣
答曰漘上廣 a丈 甲郡正袤 b丈 斜袤 c丈 上廣 d丈 深 e丈 乙郡正袤 f丈 斜袤 g丈 上廣 h丈 深 i丈 丙郡正袤 j丈 斜袤 k丈 上廣 l丈 深 m丈 丁郡正袤 n丈 斜袤 o丈 上廣 p丈 深 q丈 
"""

"""
This problem is extremely complex and involves multiple steps for calculating the dimensions of the river and embankment construction, as well as distributing the workload among four regions. To solve this, we need to carefully follow the procedure ("術") provided. Below is the Python code that implements the solution step by step.


"""


from fractions import Fraction
import math

# Constants and initial values
程功 = Fraction(3, 7)  # Each person's work volume (常積)
限日 = 96  # Time limit in days
總人 = 22320 + 68076 + 59985 + 37944  # Total people from all regions

# 河 dimensions
河袤 = 1 * 300 + 276  # Total length in steps (1 里 = 300 步)
北頭深 = 1 * 10 + 8 + Fraction(6, 10)  # Depth at the north head in 丈
南頭深 = 241 + Fraction(8, 10)  # Depth at the south head in 尺
北頭上廣 = 12 * 10 + 2 + Fraction(4, 10)  # Upper width at the north head in 步
南頭上廣 = 86 * 10 + 4 + Fraction(8, 10)  # Upper width at the south head in 步
下廣 = 6 * 10 + 1 + Fraction(2, 10)  # Lower width in 步

# 漘 dimensions
漘下廣 = 406 * 10 + 7 + Fraction(5, 10)  # Lower width of the embankment in 步
北頭高 = 223 + Fraction(2, 10)  # Height at the north head in 尺
南頭高 = 0  # Height at the south head in 尺

# Helper functions
def 開平方(value):
    """Calculate the square root of a value."""
    return Fraction(math.sqrt(float(value)))

# Step 1: Calculate the total work volume for the embankment (漘)
漘積 = 程功 * 總人 * 限日 * Fraction(4, 3) * 6

# Step 2: Calculate the 正袤 and 斜袤 for each region
def 計算郡正斜袤(郡人數, 前深, 前廣, 後深, 後廣, 本袤):
    """Calculate 正袤, 斜袤, 上廣, and 深 for a region."""
    積 = 程功 * 郡人數 * 限日 * Fraction(4, 3)
    法 = 本袤 * (後廣 - 前廣) * (後深 - 前深)
    正袤 = 積 / 法

    # Calculate 上廣 and 深
    上廣 = 前廣 + (後廣 - 前廣) * 正袤 / 本袤
    深 = 前深 + (後深 - 前深) * 正袤 / 本袤

    # Calculate 斜袤
    斜袤 = 開平方(正袤**2 + (後廣 - 前廣)**2 + (後深 - 前深)**2)

    return 正袤, 斜袤, 上廣, 深

# Calculate for 甲郡
甲正袤, 甲斜袤, 甲上廣, 甲深 = 計算郡正斜袤(22320, 北頭深, 北頭上廣, 南頭深, 南頭上廣, 河袤)

# Calculate for 乙郡
乙正袤, 乙斜袤, 乙上廣, 乙深 = 計算郡正斜袤(68076, 甲深, 甲上廣, 南頭深, 南頭上廣, 河袤)

# Calculate for 丙郡
丙正袤, 丙斜袤, 丙上廣, 丙深 = 計算郡正斜袤(59985, 乙深, 乙上廣, 南頭深, 南頭上廣, 河袤)

# Calculate for 丁郡
丁正袤, 丁斜袤, 丁上廣, 丁深 = 計算郡正斜袤(37944, 丙深, 丙上廣, 南頭深, 南頭上廣, 河袤)

# Step 3: Calculate 漘上廣
漘實 = 漘積 / 河袤 / 北頭高
漘上廣 = (漘實 - 漘下廣) / 2

# Final answers
a = 漘上廣
b = 甲正袤
c = 甲斜袤
d = 甲上廣
e = 甲深
f = 乙正袤
g = 乙斜袤
h = 乙上廣
i = 乙深
j = 丙正袤
k = 丙斜袤
l = 丙上廣
m = 丙深
n = 丁正袤
o = 丁斜袤
p = 丁上廣
q = 丁深

# Print the results
print(f"漘上廣: {a} 丈")
print(f"甲郡正袤: {b} 丈, 斜袤: {c} 丈, 上廣: {d} 丈, 深: {e} 丈")
print(f"乙郡正袤: {f} 丈, 斜袤: {g} 丈, 上廣: {h} 丈, 深: {i} 丈")
print(f"丙郡正袤: {j} 丈, 斜袤: {k} 丈, 上廣: {l} 丈, 深: {m} 丈")
print(f"丁郡正袤: {n} 丈, 斜袤: {o} 丈, 上廣: {p} 丈, 深: {q} 丈")


"""


This code follows the procedure step by step, calculating the dimensions for each region and the embankment. Note that the calculations involve fractions to maintain precision, and the square root is computed using a helper function.
"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: -50195/28
Variable 'b' has wrong value. Expected: 144, Actual: 125/9744
Variable 'c' has wrong value. Expected: 1443/10, Actual: 6818963691671265/8796093022208
Variable 'd' has wrong value. Expected: 651/25, Actual: 925469/7560
Variable 'e' has wrong value. Expected: 279/25, Actual: 14502947/779520
Variable 'f' has wrong value. Expected: 576/5, Actual: 1232514662400/31499247031561
Variable 'g' has wrong value. Expected: 2886/25, Actual: 6818811830598943/8796093022208
Variable 'h' has wrong value. Expected: 1023/25, Actual: 5196259581911/42429887640
Variable 'i' has wrong value. Expected: 93/5, Actual: 81462948553193/4374992858880
Variable 'j' has wrong value. Expected: 288/5, Actual: 34209041071746314479104000/992067765065150416535203921
Variable 'k' has wrong value. Expected: 1443/25, Actual: 6818348618427201/8796093022208
Variable 'l' has wrong value. Expected: 1209/25, Actual: 163726536042236380294830671/1336418721566930714270040
Variable 'm' has wrong value. Expected: 558/25, Actual: 2567688338998263406121545073/137799619290456855871399680
Variable 'n' has wrong value. Expected: 144/5, Actual: 21467560098908955168938502911777303012995425757593600/984080614817919131546460245645086066238997187867806241
Variable 'o' has wrong value. Expected: 1443/50, Actual: 6817940430095721/8796093022208
Variable 'p' has wrong value. Expected: 1302/25, Actual: 162455364929917231855064858337516587720644480792550591/1325738563457701436194522981772976072216722808666840
Variable 'q' has wrong value. Expected: 1209/50, Actual: 2548323707213608852440115082399965520622891330012120833/136698376320971881420946369676146866113013196271425280"""
