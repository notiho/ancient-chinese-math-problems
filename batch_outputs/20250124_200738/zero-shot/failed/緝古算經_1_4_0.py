"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
To solve this ancient Chinese math problem, we will translate the described algorithm into Python code. The solution involves calculating various dimensions and values for the four counties (甲, 乙, 丙, 丁) based on the given parameters. Here's the Python implementation:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
袤 = Fraction(1, 1) + Fraction(276, 300)  # 袤 = 1里276步
下廣 = Fraction(6, 1) + Fraction(1, 10) + Fraction(2, 100)  # 下廣 = 6步1尺2寸
北頭深 = Fraction(1, 1) + Fraction(8, 10) + Fraction(6, 100)  # 北頭深 = 1丈8尺6寸
上廣北 = Fraction(12, 1) + Fraction(2, 10) + Fraction(4, 100)  # 北頭上廣 = 12步2尺4寸
南頭深 = Fraction(241, 1) + Fraction(8, 10)  # 南頭深 = 241尺8寸
上廣南 = Fraction(86, 1) + Fraction(4, 10) + Fraction(8, 100)  # 南頭上廣 = 86步4尺8寸
漘高北 = Fraction(223, 1) + Fraction(2, 10)  # 北頭漘高 = 223尺2寸
漘高南 = Fraction(0, 1)  # 南頭漘高 = 0
漘下廣 = Fraction(406, 1) + Fraction(7, 10) + Fraction(5, 1000)  # 漘下廣 = 406尺7寸5厘
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
漘上廣 = (實 / (正袤 * 漘高北)) - 漘下廣
漘上廣 /= 2
a = 漘上廣

# Helper function to calculate for each 郡
def calculate_郡(人數, 上廣小, 深小, 上廣大, 深大, 正袤前):
    積 = 程功 * 人數 * 限日 / 4
    法 = (上廣大 - 上廣小) * (深大 - 深小)
    實 = 積 * 6 * 袤**2 / 法
    垣頭冪 = (上廣小 + 下廣) * 深小 / 3
    垣方 = 垣頭冪 * 袤**2 / 法
    都廉 = 3 * 上廣小 * 正袤前 / (上廣大 - 上廣小)
    正袤 = 都廉**(1/3)
    深 = 深小 + (深大 - 深小) * 正袤 / 袤
    上廣 = 上廣小 + (上廣大 - 上廣小) * 正袤 / 袤
    斜袤 = (正袤**2 + (深大 - 深小)**2)**(1/2)
    return 正袤, 斜袤, 上廣, 深

# Calculate for 甲郡
b, c, d, e = calculate_郡(甲郡人, 上廣北, 北頭深, 上廣南, 南頭深, 袤)

# Calculate for 乙郡
f, g, h, i = calculate_郡(乙郡人, d, e, 上廣南, 南頭深, b)

# Calculate for 丙郡
j, k, l, m = calculate_郡(丙郡人, h, i, 上廣南, 南頭深, f)

# Calculate for 丁郡
n, o, p, q = calculate_郡(丁郡人, l, m, 上廣南, 南頭深, j)

# Results
a = 漘上廣
b, c, d, e = b, c, d, e
f, g, h, i = f, g, h, i
j, k, l, m = j, k, l, m
n, o, p, q = n, o, p, q
#----- content ends here -----


"""


This Python code calculates the required values for each 郡 (county) and assigns them to the variables `a`, `b`, `c`, ..., `q` as specified in the problem. The calculations follow the ancient algorithm described in the problem statement.
"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: 188243659/400
Variable 'b' has wrong value. Expected: 144, Actual: 0.9829286170726224
Variable 'c' has wrong value. Expected: 1443/10, Actual: 239.94201330460294
Variable 'd' has wrong value. Expected: 651/25, Actual: 50.24657319347473
Variable 'e' has wrong value. Expected: 279/25, Actual: 124.69536061479428
Variable 'f' has wrong value. Expected: 576/5, Actual: 1.5991164500633217
Variable 'g' has wrong value. Expected: 2886/25, Actual: 117.11555720296062
Variable 'h' has wrong value. Expected: 1023/25, Actual: 80.424421552058
Variable 'i' has wrong value. Expected: 93/5, Actual: 222.22867062501075
Variable 'j' has wrong value. Expected: 288/5, Actual: 3.9940290467145734
Variable 'k' has wrong value. Expected: 1443/25, Actual: 19.974714053781028
Variable 'l' has wrong value. Expected: 1209/25, Actual: 93.02137791442212
Variable 'm' has wrong value. Expected: 558/25, Actual: 262.941409170076
Variable 'n' has wrong value. Expected: 144/5, Actual: (2.771949655198315+4.801157638826512j)
Variable 'o' has wrong value. Expected: 1443/50, Actual: (20.784652162660024+0.6403074324913153j)
Variable 'p' has wrong value. Expected: 1302/25, Actual: (83.57743507358657-16.357388824103527j)
Variable 'q' has wrong value. Expected: 1209/50, Actual: (232.41905403497256-52.86626986065996j)"""
