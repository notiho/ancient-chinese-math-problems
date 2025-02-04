"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is highly complex and involves multiple steps of calculation for determining the dimensions of the river excavation and embankment construction, as well as distributing the workload among the four counties. Below is the Python code that follows the procedure ("術") step by step to compute the required values.


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants and given values
袤 = 1 * 300 + 276  # 袤 (length of the river) in steps
北頭深 = 1 * 10 + 8 + Fraction(6, 10)  # 北頭深 (depth at the north end) in chi
南頭深 = 241 + Fraction(8, 10)  # 南頭深 (depth at the south end) in chi
北頭上廣 = 12 * 10 + 2 + Fraction(4, 10)  # 北頭上廣 (upper width at the north end) in chi
南頭上廣 = 86 * 10 + 4 + Fraction(8, 10)  # 南頭上廣 (upper width at the south end) in chi
北頭下廣 = 6 * 10 + 1 + Fraction(2, 10)  # 北頭下廣 (lower width at the north end) in chi
南頭下廣 = 8 * 10 + 6 + Fraction(4, 10)  # 南頭下廣 (lower width at the south end) in chi
漘下廣 = 406 * 10 + 7 + Fraction(5, 10)  # 漘下廣 (lower width of the embankment) in chi
北頭高 = 223 + Fraction(2, 10)  # 北頭高 (height at the north end) in chi
南頭高 = 0  # 南頭高 (height at the south end) in chi
甲郡人 = 22320  # People in 甲郡
乙郡人 = 68076  # People in 乙郡
丙郡人 = 59985  # People in 丙郡
丁郡人 = 37944  # People in 丁郡
程功 = 3 + Fraction(7, 10) + Fraction(2, 100)  # Work per person per day in cubic chi
限日 = 96  # Number of days

# Helper function to calculate 正袤, 斜袤, 上廣, and 深 for each county
def calculate_dimensions(小頭深, 小頭上廣, 小頭下廣, 大頭深, 大頭上廣, 大頭下廣, 人數, 本袤):
    # Calculate the total volume of work for the county
    積 = Fraction(程功 * 人數 * 限日, 4 * 3)

    # Calculate the 法 (divisor)
    廣差 = 大頭上廣 - 小頭上廣
    深差 = 大頭深 - 小頭深
    法 = 廣差 * 深差

    # Calculate 正袤
    正袤 = Fraction(積, 法)

    # Calculate 上廣
    上廣 = Fraction(廣差 * 正袤, 本袤) + 小頭上廣

    # Calculate 深
    深 = Fraction(深差 * 正袤, 本袤) + 小頭深

    # Calculate 斜袤
    斜袤 = sqrt(正袤**2 + 深差**2)

    return 正袤, 斜袤, 上廣, 深

# Calculate dimensions for 甲郡
甲正袤, 甲斜袤, 甲上廣, 甲深 = calculate_dimensions(
    北頭深, 北頭上廣, 北頭下廣, 南頭深, 南頭上廣, 南頭下廣, 甲郡人, 袤
)

# Calculate dimensions for 乙郡
乙正袤, 乙斜袤, 乙上廣, 乙深 = calculate_dimensions(
    甲深, 甲上廣, 北頭下廣, 南頭深, 南頭上廣, 南頭下廣, 乙郡人, 袤
)

# Calculate dimensions for 丙郡
丙正袤, 丙斜袤, 丙上廣, 丙深 = calculate_dimensions(
    乙深, 乙上廣, 北頭下廣, 南頭深, 南頭上廣, 南頭下廣, 丙郡人, 袤
)

# Calculate dimensions for 丁郡
丁正袤, 丁斜袤, 丁上廣, 丁深 = calculate_dimensions(
    丙深, 丙上廣, 北頭下廣, 南頭深, 南頭上廣, 南頭下廣, 丁郡人, 袤
)

# Calculate 漘上廣
總人 = 甲郡人 + 乙郡人 + 丙郡人 + 丁郡人
漘積 = 程功 * 總人 * 限日
漘實 = 漘積 * 6
漘上廣 = Fraction(漘實, 袤 * 北頭高) - 漘下廣
漘上廣 = Fraction(漘上廣, 2)

# Final results
a = 漘上廣
b, c, d, e = 甲正袤, 甲斜袤, 甲上廣, 甲深
f, g, h, i = 乙正袤, 乙斜袤, 乙上廣, 乙深
j, k, l, m = 丙正袤, 丙斜袤, 丙上廣, 丙深
n, o, p, q = 丁正袤, 丁斜袤, 丁上廣, 丁深

# Output results
print(f"漘上廣: {a}丈")
print(f"甲郡正袤: {b}丈, 斜袤: {c}丈, 上廣: {d}丈, 深: {e}丈")
print(f"乙郡正袤: {f}丈, 斜袤: {g}丈, 上廣: {h}丈, 深: {i}丈")
print(f"丙郡正袤: {j}丈, 斜袤: {k}丈, 上廣: {l}丈, 深: {m}丈")
print(f"丁郡正袤: {n}丈, 斜袤: {o}丈, 上廣: {p}丈, 深: {q}丈")
#----- content ends here -----


"""


This code follows the procedure described in the problem, calculating the required dimensions for each county and the embankment width. Note that all calculations are performed using fractions to maintain precision.
"""


"""
Variable 'a' has wrong value. Expected: 5821/1000, Actual: -3715/8
Variable 'b' has wrong value. Expected: 144, Actual: 465/116
Variable 'c' has wrong value. Expected: 1443/10, Actual: 223.23599405076578
Variable 'd' has wrong value. Expected: 651/25, Actual: 3827/30
Variable 'e' has wrong value. Expected: 279/25, Actual: 187023/9280
Variable 'f' has wrong value. Expected: 576/5, Actual: 6064754688/489161689
Variable 'g' has wrong value. Expected: 2886/25, Actual: 221.99314979474775
Variable 'h' has wrong value. Expected: 1023/25, Actual: 95170847/663510
Variable 'i' has wrong value. Expected: 93/5, Actual: 1023118575/41049152
Variable 'j' has wrong value. Expected: 288/5, Actual: 2614052516429675520/229089166740025201
Variable 'k' has wrong value. Expected: 1443/25, Actual: 217.17573860321332
Variable 'l' has wrong value. Expected: 1209/25, Actual: 50090155657784567/317577517089510
Variable 'm' has wrong value. Expected: 558/25, Actual: 574110017193371847/19647462390604352
Variable 'n' has wrong value. Expected: 144/5, Actual: 378808145773402300434914483121758208/50423098212317929747921102835189761
Variable 'o' has wrong value. Expected: 1443/50, Actual: 212.71213835700595
Variable 'p' has wrong value. Expected: 1302/25, Actual: 2381088323862274658957197232207947/14262462257347988396548161737262
Variable 'q' has wrong value. Expected: 1209/50, Actual: 705746282976126539029059056396244579/22059274958031555386661156820298560"""
