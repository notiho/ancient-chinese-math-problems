"""
假令太史造仰觀臺，上廣袤少，下廣袤多。上下廣差二丈，上下袤差四丈，上廣袤差三丈，高多上廣一十一丈，甲縣差一千四百一十八人，乙縣差三千二百二十二人，夏程人功常積七十五尺，限五日役臺畢。羨道從臺南面起，上廣多下廣一丈二尺，少袤一百四尺，高多袤四丈。甲縣一十三鄉，乙縣四十三鄉，每鄉別均賦常積六千三百尺，限一日役羨道畢。二縣差到人共造仰觀臺，二縣鄉人共造羨道，皆從先給甲縣，以次與乙縣。臺自下基給高，道自初登給袤。問：臺道廣、高、袤及縣別給高、廣、袤各幾何？
術曰：以程功尺數乘二縣人，又以限日乘之，為臺積。又以上下袤差乘上下廣差，三而一，為隅陽冪。以乘截高，為隅陽截積。又半上下廣差，乘斬上袤，為隅頭冪。以乘截高，為隅頭截積。並二積，以減臺積，余為實。以上下廣差並上下袤差，半之，為正數，加截上袤，以乘截高，所得增隅陽冪加隅頭冪，為方法。又並截高及截上袤與正數，為廉法，從。開立方除之，即得上廣。各加差，得臺下廣及上下袤、高。求均給積尺受廣袤，術曰：以程功尺數乘乙縣人，又以限日乘之，為乙積。三因之，又以高冪乘之，以上下廣差乘袤差而一，為實。又以臺高乘上廣，廣差而一，為上廣之高。又以臺高乘上袤，袤差而一，為上袤之高。又以上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即乙高。以減本高，余即甲高。此是從下給臺甲高。又以廣差乘乙高，以本高而一，所得加上廣，即甲上廣。又以袤差乘乙高，如本高而一，所得加上袤，即甲上袤。其上廣、袤即乙下廣、袤，臺上廣、袤即乙上廣、袤。其後求廣、袤，有增損者，皆放此。求羨道廣、袤、高，術曰：以均賦常積乘二縣五十六鄉，又六因，為積。又以道上廣多下廣數加上廣少袤，為下廣少袤。又以高多袤加下廣少袤，為下廣少高。以乘下廣少袤，為隅陽冪。又以下廣少上廣乘之，為鱉隅積。以減積，余三而一，為實。並下廣少袤與下廣少高，以下廣少上廣乘之，鱉從橫廉冪。三而一，加隅冪，為方法。又以三除上廣多下廣，以下廣少袤、下廣少高加之，為廉法，從。開立方除之，即下廣。加廣差，即上廣。加袤多上廣於上廣，即袤。加高多袤，即道高。求羨道均給積尺甲縣受廣、袤，術曰：以均賦常積乘甲縣上十三鄉，又六因，為積。以袤再乘之，以道上下廣差乘臺高為法而一，為實。又三因下廣，以袤乘之，如上下廣差而一，為都廉，從。開立方除之，即甲袤。以廣差乘甲袤，本袤而一，以下廣加之，即甲上廣。又以臺高乘甲袤，本袤除之，即甲高。
答曰：臺高 a丈 上廣 b丈 ，下廣 c丈 ，上袤 d丈 ，下袤 e丈 ；甲縣給高 f丈 ，上廣 g丈 ，下廣 h丈 ，上袤 i丈 ，下袤 j丈 ；乙縣給高 k丈 ，上廣 l丈 ，下廣 m丈 ，上袤 n丈 ，下袤 o丈 ；羨道高 p丈 ，上廣 q丈 ，下廣 r丈 ，袤 s丈 ；甲縣鄉人給高 t丈 ，上廣 u丈 ，下廣 v丈 ，袤 w丈 ；乙縣鄉人給高 x丈 ，上廣 y丈 ，下廣 z丈 ，袤 a丈 。
"""

"""
This problem is highly complex and involves a significant amount of calculations, including geometric relationships, proportional distributions, and iterative steps. Translating this entire procedure into Python code requires breaking it into smaller, manageable parts. Below is the Python implementation of the problem, step by step, following the structure of the procedure ("術") provided.

---

### Step 1: Define constants and initial values


---

### Step 2: Calculate the total volume of the 台 (臺積)


---

### Step 3: Calculate 隅陽冪 and 隅頭冪


---

### Step 4: Calculate the remaining volume (實) and 正數


---

### Step 5: Solve for 上廣, 下廣, 上下袤, and 高


---

### Step 6: Calculate 羨道 dimensions


---

### Step 7: Calculate contributions from 甲縣 and 乙縣


---

### Final Answer

"""

#----- content starts here -----

from fractions import Fraction

# Constants
上下廣差 = Fraction(2)  # 二丈
上下袤差 = Fraction(4)  # 四丈
上廣袤差 = Fraction(3)  # 三丈
高多上廣 = Fraction(11)  # 十一丈
甲縣差 = 1418
乙縣差 = 3222
夏程人功常積 = 75  # 七十五尺
限日臺 = 5  # 五日
羨道上廣多下廣 = Fraction(1, 5)  # 一丈二尺
羨道少袤 = 104  # 一百四尺
羨道高多袤 = 4  # 四丈
甲縣鄉數 = 13  # 一十三鄉
乙縣鄉數 = 43  # 四十三鄉
均賦常積 = 6300  # 六千三百尺
限日羨道 = 1  # 一日

# Calculate 台積
臺積 = 夏程人功常積 * (甲縣差 + 乙縣差) * 限日臺

# 隅陽冪
隅陽冪 = (上下廣差 * 上下袤差) / 3

# 隅陽截積
隅陽截積 = 隅陽冪 * 高多上廣

# 隅頭冪
隅頭冪 = (上下廣差 / 2) * 上廣袤差

# 隅頭截積
隅頭截積 = 隅頭冪 * 高多上廣

# Combine 隅陽截積 and 隅頭截積
隅積 = 隅陽截積 + 隅頭截積

# Remaining volume (實)
實 = 臺積 - 隅積

# 正數
正數 = ((上下廣差 + 上下袤差) / 2) + 上廣袤差

# 方法
方法 = 隅陽冪 + 隅頭冪 + 正數 * 高多上廣

# 廉法
廉法 = 正數 + 高多上廣 + 上廣袤差

# Solve for 上廣
上廣 = (實 / 方法) ** Fraction(1, 3)

# Calculate 下廣, 上下袤, and 高
下廣 = 上廣 + 上下廣差
上下袤 = 上廣 + 上下袤差
高 = 上廣 + 高多上廣

# 羨道積
羨道積 = 均賦常積 * (甲縣鄉數 + 乙縣鄉數) * 6

# 下廣少袤
下廣少袤 = 羨道上廣多下廣 + 羨道少袤

# 下廣少高
下廣少高 = 羨道高多袤 + 下廣少袤

# 隅陽冪 for 羨道
羨道隅陽冪 = 下廣少袤 * 下廣少高

# 鱉隅積
鱉隅積 = 羨道上廣多下廣 * 下廣少袤

# Remaining volume for 羨道
羨道實 = (羨道積 - 鱉隅積) / 3

# Solve for 下廣
下廣 = (羨道實 / 羨道隅陽冪) ** Fraction(1, 3)

# Calculate 上廣, 袤, and 高 for 羨道
上廣 = 下廣 + 羨道上廣多下廣
袤 = 上廣 + 羨道少袤
高 = 袤 + 羨道高多袤

# 甲縣 contribution
甲積 = 均賦常積 * 甲縣鄉數 * 6

# Solve for 甲袤
甲袤 = (甲積 / (上下廣差 * 高)) ** Fraction(1, 3)

# Calculate 甲上廣 and 甲高
甲上廣 = (上下廣差 * 甲袤) / 高 + 上廣
甲高 = (高 * 甲袤) / 上廣

# 乙縣 contribution
乙積 = 均賦常積 * 乙縣鄉數 * 6

# Solve for 乙袤
乙袤 = (乙積 / (上下廣差 * 高)) ** Fraction(1, 3)

# Calculate 乙上廣 and 乙高
乙上廣 = (上下廣差 * 乙袤) / 高 + 上廣
乙高 = (高 * 乙袤) / 上廣

# Output results
a = 高
b = 上廣
c = 下廣
d = 上下袤
e = 上下袤 + 上下袤差
f = 甲高
g = 甲上廣
h = 下廣
i = 甲袤
j = 上下袤
k = 乙高
l = 乙上廣
m = 下廣
n = 乙袤
o = 上下袤
p = 高
q = 上廣
r = 下廣
s = 袤
t = 甲高
u = 甲上廣
v = 下廣
w = 甲袤
x = 乙高
y = 乙上廣
z = 下廣
#----- content ends here -----


"""


This solution provides the values for all the required dimensions and contributions.
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 112.17026753242399
Variable 'b' has wrong value. Expected: 7, Actual: 4.170267532423994
Variable 'c' has wrong value. Expected: 9, Actual: 3.9702675324239936
Variable 'd' has wrong value. Expected: 10, Actual: 32.95601735470656
Variable 'e' has wrong value. Expected: 14, Actual: 36.95601735470656
Variable 'f' has wrong value. Expected: 9/2, Actual: 349.3196146627005
Variable 'g' has wrong value. Expected: 17/2, Actual: 4.401826376837292
Variable 'h' has wrong value. Expected: 9, Actual: 3.9702675324239936
Variable 'i' has wrong value. Expected: 13, Actual: 12.987008763669298
Variable 'j' has wrong value. Expected: 14, Actual: 32.95601735470656
Variable 'k' has wrong value. Expected: 27/2, Actual: 520.4727624932996
Variable 'l' has wrong value. Expected: 7, Actual: 4.515281285940007
Variable 'm' has wrong value. Expected: 17/2, Actual: 3.9702675324239936
Variable 'n' has wrong value. Expected: 10, Actual: 19.350142517128464
Variable 'o' has wrong value. Expected: 13, Actual: 32.95601735470656
Variable 'p' has wrong value. Expected: 18, Actual: 112.17026753242399
Variable 'q' has wrong value. Expected: 18/5, Actual: 4.170267532423994
Variable 'r' has wrong value. Expected: 12/5, Actual: 3.9702675324239936
Variable 's' has wrong value. Expected: 14, Actual: 108.17026753242399
Variable 't' has wrong value. Expected: 9, Actual: 349.3196146627005
Variable 'u' has wrong value. Expected: 3, Actual: 4.401826376837292
Variable 'v' has wrong value. Expected: 12/5, Actual: 3.9702675324239936
Variable 'w' has wrong value. Expected: 7, Actual: 12.987008763669298
Variable 'x' has wrong value. Expected: 9, Actual: 520.4727624932996
Variable 'y' has wrong value. Expected: 18/5, Actual: 4.515281285940007
Variable 'z' has wrong value. Expected: 3, Actual: 3.9702675324239936
Missing variable in output: '{'"""
