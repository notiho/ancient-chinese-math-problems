"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The problem involves calculating various dimensions and values for the construction of a riverbank and dividing the work among four counties. We'll use the `Fraction` class to handle non-integer values and ensure precision.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
袤 = Fraction(1, 1) + Fraction(276, 1000)  # 袤 = 1里276步
下廣 = Fraction(6, 1) + Fraction(1, 10) + Fraction(2, 100)  # 下廣 = 6步1尺2寸
北頭深 = Fraction(1, 1) + Fraction(8, 10) + Fraction(6, 100)  # 北頭深 = 1丈8尺6寸
上廣北 = Fraction(12, 1) + Fraction(2, 10) + Fraction(4, 100)  # 北頭上廣 = 12步2尺4寸
南頭深 = Fraction(241, 1) + Fraction(8, 10)  # 南頭深 = 241尺8寸
上廣南 = Fraction(86, 1) + Fraction(4, 10) + Fraction(8, 100)  # 南頭上廣 = 86步4尺8寸
北頭高 = Fraction(223, 1) + Fraction(2, 10)  # 北頭高 = 223尺2寸
下廣漘 = Fraction(406, 1) + Fraction(7, 10) + Fraction(5, 1000)  # 下廣漘 = 406尺7寸5厘
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944
程功 = Fraction(3, 1) + Fraction(7, 10) + Fraction(2, 100)  # 程功 = 3尺7寸2分
限日 = 96

# Calculate 漘上廣 (a)
總人 = 甲郡人 + 乙郡人 + 丙郡人 + 丁郡人
積 = 程功 * 總人 * 限日
實 = 積 * 6
正袤 = 袤
a = (實 / (正袤 * 北頭高) - 下廣漘) / 2

# Function to calculate dimensions for each county
def calculate_dimensions(人數, 上廣小, 深小, 上廣大, 深大, 正袤前):
    積 = 程功 * 人數 * 限日 / 4
    法 = 上廣小 * 深小 - 上廣大 * 深大
    小頭冪 = (上廣小 + 下廣) * 深小 / 3
    垣方 = 積 / 法
    都廉 = (3 * 上廣小 * 正袤前) / (上廣小 - 上廣大)
    正袤 = (垣方 / 小頭冪) ** Fraction(1, 3)
    深差 = 深大 - 深小
    廣差 = 上廣大 - 上廣小
    上廣 = (廣差 * 正袤 / 袤) + 上廣小
    深 = (深差 * 正袤 / 袤) + 深小
    斜袤 = (正袤 ** 2 + 深差 ** 2) ** Fraction(1, 2)
    return 正袤, 斜袤, 上廣, 深

# Calculate for 甲郡
b, c, d, e = calculate_dimensions(甲郡人, 上廣北, 北頭深, 上廣南, 南頭深, 袤)

# Calculate for 乙郡
f, g, h, i = calculate_dimensions(乙郡人, d, e, 上廣南, 南頭深, b)

# Calculate for 丙郡
j, k, l, m = calculate_dimensions(丙郡人, h, i, 上廣南, 南頭深, f)

# Calculate for 丁郡
n, o, p, q = calculate_dimensions(丁郡人, l, m, 上廣南, 南頭深, j)

# Output results
a = a / 10  # Convert to 丈
b = b / 10
c = c / 10
d = d / 10
e = e / 10
f = f / 10
g = g / 10
h = h / 10
i = i / 10
j = j / 10
k = k / 10
l = l / 10
m = m / 10
n = n / 10
o = o / 10
p = p / 10
q = q / 10

# Results
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q
#----- content ends here -----


"""


This code calculates the required dimensions and values for each county and the riverbank width (`漘上廣`). Each variable corresponds to the unknowns in the problem. The results are stored in variables `a`, `b`, `c`, ..., `q` as specified in the problem.
"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: 90370052221/1276000
Variable 'b' has wrong value. Expected: 144, Actual: (0.10156210887286321+0.1759107326916409j)
Variable 'c' has wrong value. Expected: 1443/10, Actual: (23.99357011431453+0.0007446105310886944j)
Variable 'd' has wrong value. Expected: 651/25, Actual: (7.13306815260295+10.23480626569547j)
Variable 'e' has wrong value. Expected: 279/25, Actual: (19.283815362817244+33.0783865219689j)
Variable 'f' has wrong value. Expected: 576/5, Actual: (0.014495446377925153+0.011316058339600435j)
Variable 'g' has wrong value. Expected: 2886/25, Actual: (4.896179964304511-33.0783845898414j)
Variable 'h' has wrong value. Expected: 1023/25, Actual: (8.212827385810417+9.20647532331947j)
Variable 'i' has wrong value. Expected: 93/5, Actual: (22.773543681995584+29.754871889510696j)
Variable 'j' has wrong value. Expected: 288/5, Actual: (0.012754972321567883+0.013225756330410395j)
Variable 'k' has wrong value. Expected: 1443/25, Actual: (1.406450651486337-29.754871827200287j)
Variable 'l' has wrong value. Expected: 1209/25, Actual: (9.21057984613371+8.331296240473089j)
Variable 'm' has wrong value. Expected: 558/25, Actual: (25.998230176203162+26.926336475472965j)
Variable 'n' has wrong value. Expected: 144/5, Actual: (0.009547226647934315+0.012985899174447587j)
Variable 'o' has wrong value. Expected: 1443/50, Actual: (1.8182346629754533+26.926338217262593j)
Variable 'p' has wrong value. Expected: 1302/25, Actual: (10.016365862376965+7.650681987821455j)
Variable 'q' has wrong value. Expected: 1209/50, Actual: (28.602490638722106+24.726624948247313j)"""
