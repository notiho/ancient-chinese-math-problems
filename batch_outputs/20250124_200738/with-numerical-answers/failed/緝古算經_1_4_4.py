"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a(=5821/1000)丈 ；甲郡正袤 b(=144)丈 ，斜袤 c(=1443/10)丈 ，上廣 d(=651/25)丈 ，深 e(=279/25)丈 ；乙郡正袤 f(=576/5)丈 ，斜袤 g(=2886/25)丈 ，上廣 h(=1023/25)丈 ，深 i(=93/5)丈 ；丙郡正袤 j(=288/5)丈 ，斜袤 k(=1443/25)丈 ，上廣 l(=1209/25)丈 ，深 m(=558/25)丈 ，丁郡正袤 n(=144/5)丈 ，斜袤 o(=1443/50)丈 ，上廣 p(=1302/25)丈 ，深 q(=1209/50)丈 。
"""

"""
This problem is extremely complex and involves multiple steps of calculation for each of the four regions (甲郡, 乙郡, 丙郡, 丁郡) and their contributions to the excavation and embankment construction. Below is the Python implementation of the procedure described in the problem, step by step, following the ancient Chinese mathematical method.


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants and initial values
程功 = Fraction(372, 100)  # Each person's work capacity (3尺7寸2分 = 372/100尺)
限日 = 96  # Limit of 96 days
總人 = 22320 + 68076 + 59985 + 37944  # Total people from all regions
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944

# 河 dimensions
袤 = Fraction(276, 1) + 1 * 300  # Total length (1里 = 300步, plus 276步)
北頭深 = Fraction(186, 10)  # 北頭深 = 1丈8尺6寸 = 186/10丈
南頭深 = Fraction(2418, 10)  # 南頭深 = 241尺8寸 = 2418/10丈
北頭上廣 = Fraction(1224, 10)  # 北頭上廣 = 12步2尺4寸 = 1224/10丈
南頭上廣 = Fraction(8648, 10)  # 南頭上廣 = 86步4尺8寸 = 8648/10丈
北頭下廣 = Fraction(612, 10)  # 北頭下廣 = 6步1尺2寸 = 612/10丈
南頭下廣 = Fraction(8648, 10)  # 南頭下廣 = 86步4尺8寸 = 8648/10丈

# 漘 dimensions
漘北頭高 = Fraction(2232, 10)  # 漘北頭高 = 223尺2寸 = 2232/10丈
漘南頭高 = 0  # 漘南頭無高
漘下廣 = Fraction(40675, 100)  # 漘下廣 = 406尺7寸5厘 = 40675/100丈

# Step 1: Calculate the total volume of work for each region
甲積 = (程功 * 甲郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)
乙積 = (程功 * 乙郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)
丙積 = (程功 * 丙郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)
丁積 = (程功 * 丁郡人 * 限日) / Fraction(4, 1) * Fraction(3, 1)

# Step 2: Calculate the embankment dimensions
漘積 = (程功 * 總人 * 限日) * Fraction(6, 1)
漘實 = 漘積 / 袤
漘上廣 = (漘實 / 漘北頭高 - 漘下廣) / 2

# Step 3: Calculate 正袤, 斜袤, 上廣, and 深 for each region
def calculate_region(積, 小頭深, 小頭上廣, 大頭深, 大頭上廣, 本袤):
    # Calculate 正袤
    正袤 = 積 / ((大頭上廣 - 小頭上廣) * (大頭深 - 小頭深))
    
    # Calculate 上廣
    上廣 = ((大頭上廣 - 小頭上廣) * 正袤 / 本袤) + 小頭上廣
    
    # Calculate 深
    深 = ((大頭深 - 小頭深) * 正袤 / 本袤) + 小頭深
    
    # Calculate 斜袤
    斜袤 = sqrt(正袤**2 + (大頭深 - 小頭深)**2)
    
    return 正袤, 斜袤, 上廣, 深

# 甲郡 calculations
甲正袤, 甲斜袤, 甲上廣, 甲深 = calculate_region(甲積, 北頭深, 北頭上廣, 南頭深, 南頭上廣, 袤)

# 乙郡 calculations
乙正袤, 乙斜袤, 乙上廣, 乙深 = calculate_region(乙積, 甲深, 甲上廣, 南頭深, 南頭上廣, 袤)

# 丙郡 calculations
丙正袤, 丙斜袤, 丙上廣, 丙深 = calculate_region(丙積, 乙深, 乙上廣, 南頭深, 南頭上廣, 袤)

# 丁郡 calculations
丁正袤, 丁斜袤, 丁上廣, 丁深 = calculate_region(丁積, 丙深, 丙上廣, 南頭深, 南頭上廣, 袤)

# Final results
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i = 乙正袤, 乙斜袤, 乙上廣, 乙深
j, k, l, m = 丙正袤, 丙斜袤, 丙上廣, 丙深
n, o, p, q = 丁正袤, 丁斜袤, 丁上廣, 丁深

# Output results
print(f"漘上廣 a={a}丈")
print(f"甲郡正袤 b={b}丈，斜袤 c={c}丈，上廣 d={d}丈，深 e={e}丈")
print(f"乙郡正袤 f={f}丈，斜袤 g={g}丈，上廣 h={h}丈，深 i={i}丈")
print(f"丙郡正袤 j={j}丈，斜袤 k={k}丈，上廣 l={l}丈，深 m={m}丈")
print(f"丁郡正袤 n={n}丈，斜袤 o={o}丈，上廣 p={p}丈，深 q={q}丈")
#----- content ends here -----


"""


This code follows the ancient Chinese procedure step by step, using fractions to maintain precision and calculating the required dimensions for each region.
"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: 1366
Variable 'b' has wrong value. Expected: 144, Actual: 4185/116
Variable 'c' has wrong value. Expected: 1443/10, Actual: 226.09695315619814
Variable 'd' has wrong value. Expected: 651/25, Actual: 1689/10
Variable 'e' has wrong value. Expected: 279/25, Actual: 302343/9280
Variable 'f' has wrong value. Expected: 576/5, Actual: 6064754688/48427681
Variable 'g' has wrong value. Expected: 2886/25, Actual: 243.83671191604597
Variable 'h' has wrong value. Expected: 1023/25, Actual: 22282839/69590
Variable 'i' has wrong value. Expected: 93/5, Actual: 5041620489/64579520
Variable 'j' has wrong value. Expected: 288/5, Actual: 258794799817006080/1436303351379649
Variable 'k' has wrong value. Expected: 1443/25, Actual: 243.46104969634428
Variable 'l' has wrong value. Expected: 1209/25, Actual: 1293784773605607/2637363086870
Variable 'm' has wrong value. Expected: 558/25, Actual: 316424054134434297/2447472944615360
Variable 'n' has wrong value. Expected: 144/5, Actual: 235126818643551646868863648800768/974182470463795084284181145761
Variable 'o' has wrong value. Expected: 1443/50, Actual: 266.2951760377745
Variable 'p' has wrong value. Expected: 1302/25, Actual: 1685180682599245955239183702551/2603095363894269050439959030
Variable 'q' has wrong value. Expected: 1209/50, Actual: 85240450692690418074532374589173/483134499538776335761656395968"""
