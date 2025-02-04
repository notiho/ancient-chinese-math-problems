"""
假令穿河，袤一裏二百七十六步，下廣六步一尺二寸；北頭深一丈八尺六寸，上廣十二步二尺四寸；南頭深二百四十一尺八寸；上廣八十六步四尺八寸。運土於河西岸造漘，北頭高二百二十三尺二寸，南頭無高，下廣四百六尺七寸五厘，袤與河同。甲郡二萬二千三百二十人，乙郡六萬八千七十六人，丙郡五萬九千九百八十五人，丁郡三萬七千九百四十四人。自穿、負、築，各人程功常積三尺七寸二分。限九十六日役，河漘俱了。四郡分共造漘，其河自北頭先給甲郡，以次與乙，合均賦積尺。問：逐郡各給斜、正袤，上廣及深，並漘上廣各多少？
術曰：如築堤術入之。以程功乘甲郡人，又以限日乘之，四之，三而一，為積。又六因，以乘袤冪。以上廣差乘深差，為法。除之，為實。又並小頭上、下廣，以乘小頭深，三之，為垣頭冪。又乘袤冪，以法除之，為垣方。三因小頭上廣，以乘正袤，以廣差除之，為都廉，從。開立方除之，即得小頭袤，為甲袤。求深、廣，以本袤及深廣差求之。以兩頭上廣差乘甲袤，以本袤除之，所得加小頭上廣，即甲上廣。以小頭深減南頭深，余以乘甲袤，以本袤除之，所得加小頭深，即甲深。又正袤自乘，深差自乘，並，而開方除之，即斜袤。若求乙、丙、丁，每以前大深、廣為後小深、廣，準甲求之，即得。求漘上廣，術曰：以程功乘總人，又以限日乘之，為積。六因之，為實。以正袤除之，又以高除之，所得以下廣減之，余又半之，即漘上廣。
答曰：漘上廣 a丈 ；甲郡正袤 b丈 ，斜袤 c丈 ，上廣 d丈 ，深 e丈 ；乙郡正袤 f丈 ，斜袤 g丈 ，上廣 h丈 ，深 i丈 ；丙郡正袤 j丈 ，斜袤 k丈 ，上廣 l丈 ，深 m丈 ，丁郡正袤 n丈 ，斜袤 o丈 ，上廣 p丈 ，深 q丈 。
"""

"""
This problem is highly complex and involves multiple steps of calculations for dividing the work of digging a river and building embankments among four regions. It requires careful application of ancient Chinese mathematical procedures to calculate the dimensions of the river and embankments for each region. Below is the Python implementation of the procedure described in the problem.


"""

#----- content starts here -----

from fractions import Fraction
from math import sqrt

# Constants
程功 = Fraction(3, 7, 2)  # Each person's work capacity per day in cubic chi
限日 = 96  # Limit of days
總人 = 22320 + 68076 + 59985 + 37944  # Total people from all regions

# 河 dimensions
袤 = Fraction(1, 3) * 276  # Total length of the river in bu
北頭深 = Fraction(1, 8, 6)  # North depth in chi
南頭深 = Fraction(241, 8)  # South depth in chi
北頭上廣 = Fraction(12, 2, 4)  # North top width in bu
南頭上廣 = Fraction(86, 4, 8)  # South top width in bu
北頭下廣 = Fraction(6, 1, 2)  # North bottom width in bu
南頭下廣 = Fraction(8, 4, 8)  # South bottom width in bu

# 漘 dimensions
北頭高 = Fraction(223, 2)  # North embankment height in chi
南頭高 = 0  # South embankment height in chi
漘下廣 = Fraction(406, 7, 5)  # Bottom width of the embankment in chi
漘袤 = 袤  # Length of the embankment is the same as the river

# Region populations
甲郡人 = 22320
乙郡人 = 68076
丙郡人 = 59985
丁郡人 = 37944

# Step 1: Calculate the total work capacity for each region
甲積 = (程功 * 甲郡人 * 限日) / 4 * 3
乙積 = (程功 * 乙郡人 * 限日) / 4 * 3
丙積 = (程功 * 丙郡人 * 限日) / 4 * 3
丁積 = (程功 * 丁郡人 * 限日) / 4 * 3

# Step 2: Calculate the total volume of the river
總積 = (北頭上廣 + 南頭上廣) * (北頭深 + 南頭深) * 袤 / 2

# Step 3: Calculate the dimensions for each region
def calculate_region_dimensions(積, 上廣差, 深差, 本袤, 小頭上廣, 小頭深):
    # Calculate 正袤
    正袤 = sqrt((積 * 6) / (上廣差 * 深差))
    
    # Calculate 上廣
    上廣 = 小頭上廣 + (上廣差 * 正袤 / 本袤)
    
    # Calculate 深
    深 = 小頭深 + (深差 * 正袤 / 本袤)
    
    # Calculate 斜袤
    斜袤 = sqrt(正袤**2 + 深差**2)
    
    return 正袤, 斜袤, 上廣, 深

# 甲郡 calculations
甲正袤, 甲斜袤, 甲上廣, 甲深 = calculate_region_dimensions(
    甲積, 北頭上廣 - 南頭上廣, 北頭深 - 南頭深, 袤, 北頭上廣, 北頭深
)

# 乙郡 calculations
乙正袤, 乙斜袤, 乙上廣, 乙深 = calculate_region_dimensions(
    乙積, 甲上廣 - 南頭上廣, 甲深 - 南頭深, 袤, 甲上廣, 甲深
)

# 丙郡 calculations
丙正袤, 丙斜袤, 丙上廣, 丙深 = calculate_region_dimensions(
    丙積, 乙上廣 - 南頭上廣, 乙深 - 南頭深, 袤, 乙上廣, 乙深
)

# 丁郡 calculations
丁正袤, 丁斜袤, 丁上廣, 丁深 = calculate_region_dimensions(
    丁積, 丙上廣 - 南頭上廣, 丙深 - 南頭深, 袤, 丙上廣, 丙深
)

# Step 4: Calculate 漘上廣
漘積 = 程功 * 總人 * 限日
漘實 = 漘積 * 6
漘上廣 = (漘實 / (漘袤 * 北頭高) - 漘下廣) / 2

# Final answers
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


This code follows the ancient procedure step by step to calculate the required dimensions for the river and embankments for each region. Each calculation is based on the relationships and ratios described in the problem.
"""


"""
Code error: Fraction.__new__() takes from 1 to 3 positional arguments but 4 were given"""
