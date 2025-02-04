"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
To solve this ancient Chinese math problem, we will translate the described algorithm into Python code. We'll use the `Fraction` class from the `fractions` module to handle fractional calculations. Here's the Python code:


"""


from fractions import Fraction

# Given data
袤 = Fraction(1, 1) + Fraction(276, 1000)  # 1里276步
下廣 = Fraction(6, 1) + Fraction(1, 10) + Fraction(2, 100)  # 6步1尺2寸
北頭深 = Fraction(1, 1) + Fraction(8, 10) + Fraction(6, 100)  # 1丈8尺6寸
上廣北 = Fraction(12, 1) + Fraction(2, 10) + Fraction(4, 100)  # 12步2尺4寸
南頭深 = Fraction(241, 1) + Fraction(8, 10)  # 241尺8寸
上廣南 = Fraction(86, 1) + Fraction(4, 10) + Fraction(8, 100)  # 86步4尺8寸
北頭高 = Fraction(223, 1) + Fraction(2, 10)  # 223尺2寸
南頭高 = Fraction(0, 1)  # 無高
下廣漘 = Fraction(406, 1) + Fraction(7, 10) + Fraction(5, 1000)  # 406步7寸5厘
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944
程功 = Fraction(3, 1) + Fraction(7, 10) + Fraction(2, 100)  # 3尺7寸2分
限日 = 96

# Calculate 漘上廣 (a)
總人 = 甲郡人 + 乙郡人 + 丙郡人 + 丁郡人
積 = 程功 * 總人 * 限日
實 = 積 * 6
正袤 = 袤
a = (實 / (正袤 * 北頭高)) - 下廣漘
a /= 2

# Helper function to calculate for each 郡
def calculate_郡(人數, 前小深, 前小廣):
    積 = 程功 * 人數 * 限日 / 4 / 3
    法 = 積 * 6 * 袤**2 / ((上廣北 - 下廣) * (北頭深 - 南頭深))
    垣頭冪 = (前小廣 + 下廣) * 前小深 / 3
    垣方 = 垣頭冪 * 袤**2 / 法
    小頭袤 = 垣方**(1/3)
    正袤 = 小頭袤
    深差 = 北頭深 - 南頭深
    廣差 = 上廣北 - 下廣
    上廣 = (廣差 * 小頭袤 / 袤) + 下廣
    深 = (深差 * 小頭袤 / 袤) + 南頭深
    斜袤 = (正袤**2 + 深差**2)**(1/2)
    return 正袤, 斜袤, 上廣, 深

# Calculate for 甲郡
b, c, d, e = calculate_郡(甲郡人, 北頭深, 上廣北)

# Calculate for 乙郡
f, g, h, i = calculate_郡(乙郡人, e, d)

# Calculate for 丙郡
j, k, l, m = calculate_郡(丙郡人, i, h)

# Calculate for 丁郡
n, o, p, q = calculate_郡(丁郡人, m, l)

# Results
a = float(a)
b = float(b)
c = float(c)
d = float(d)
e = float(e)
f = float(f)
g = float(g)
h = float(h)
i = float(i)
j = float(j)
k = float(k)
l = float(l)
m = float(m)
n = float(n)
o = float(o)
p = float(p)
q = float(q)

# Output variables
print(f"漘上廣 a = {a}丈")
print(f"甲郡正袤 b = {b}丈, 斜袤 c = {c}丈, 上廣 d = {d}丈, 深 e = {e}丈")
print(f"乙郡正袤 f = {f}丈, 斜袤 g = {g}丈, 上廣 h = {h}丈, 深 i = {i}丈")
print(f"丙郡正袤 j = {j}丈, 斜袤 k = {k}丈, 上廣 l = {l}丈, 深 m = {m}丈")
print(f"丁郡正袤 n = {n}丈, 斜袤 o = {o}丈, 上廣 p = {p}丈, 深 q = {q}丈")


"""


This code calculates the required values for each 郡 and the 漘上廣 using the described algorithm. The results are stored in variables `a`, `b`, `c`, ..., `q` as specified in the problem.
"""


"""
Code error: float() argument must be a string or a real number, not 'complex'"""
