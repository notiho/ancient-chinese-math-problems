"""
假令太史造仰觀臺，上廣袤少，下廣袤多。上下廣差二丈，上下袤差四丈，上廣袤差三丈，高多上廣一十一丈，甲縣差一千四百一十八人，乙縣差三千二百二十二人，夏程人功常積七十五尺，限五日役臺畢。羨道從臺南面起，上廣多下廣一丈二尺，少袤一百四尺，高多袤四丈。甲縣一十三鄉，乙縣四十三鄉，每鄉別均賦常積六千三百尺，限一日役羨道畢。二縣差到人共造仰觀臺，二縣鄉人共造羨道，皆從先給甲縣，以次與乙縣。臺自下基給高，道自初登給袤。問：臺道廣、高、袤及縣別給高、廣、袤各幾何？
術曰：以程功尺數乘二縣人，又以限日乘之，為臺積。又以上下袤差乘上下廣差，三而一，為隅陽冪。以乘截高，為隅陽截積。又半上下廣差，乘斬上袤，為隅頭冪。以乘截高，為隅頭截積。並二積，以減臺積，余為實。以上下廣差並上下袤差，半之，為正數，加截上袤，以乘截高，所得增隅陽冪加隅頭冪，為方法。又並截高及截上袤與正數，為廉法，從。開立方除之，即得上廣。各加差，得臺下廣及上下袤、高。求均給積尺受廣袤，術曰：以程功尺數乘乙縣人，又以限日乘之，為乙積。三因之，又以高冪乘之，以上下廣差乘袤差而一，為實。又以臺高乘上廣，廣差而一，為上廣之高。又以臺高乘上袤，袤差而一，為上袤之高。又以上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即乙高。以減本高，余即甲高。此是從下給臺甲高。又以廣差乘乙高，以本高而一，所得加上廣，即甲上廣。又以袤差乘乙高，如本高而一，所得加上袤，即甲上袤。其上廣、袤即乙下廣、袤，臺上廣、袤即乙上廣、袤。其後求廣、袤，有增損者，皆放此。求羨道廣、袤、高，術曰：以均賦常積乘二縣五十六鄉，又六因，為積。又以道上廣多下廣數加上廣少袤，為下廣少袤。又以高多袤加下廣少袤，為下廣少高。以乘下廣少袤，為隅陽冪。又以下廣少上廣乘之，為鱉隅積。以減積，余三而一，為實。並下廣少袤與下廣少高，以下廣少上廣乘之，鱉從橫廉冪。三而一，加隅冪，為方法。又以三除上廣多下廣，以下廣少袤、下廣少高加之，為廉法，從。開立方除之，即下廣。加廣差，即上廣。加袤多上廣於上廣，即袤。加高多袤，即道高。求羨道均給積尺甲縣受廣、袤，術曰：以均賦常積乘甲縣上十三鄉，又六因，為積。以袤再乘之，以道上下廣差乘臺高為法而一，為實。又三因下廣，以袤乘之，如上下廣差而一，為都廉，從。開立方除之，即甲袤。以廣差乘甲袤，本袤而一，以下廣加之，即甲上廣。又以臺高乘甲袤，本袤除之，即甲高。
答曰：臺高 a丈 上廣 b丈 ，下廣 c丈 ，上袤 d丈 ，下袤 e丈 ；甲縣給高 f丈 ，上廣 g丈 ，下廣 h丈 ，上袤 i丈 ，下袤 j丈 ；乙縣給高 k丈 ，上廣 l丈 ，下廣 m丈 ，上袤 n丈 ，下袤 o丈 ；羨道高 p丈 ，上廣 q丈 ，下廣 r丈 ，袤 s丈 ；甲縣鄉人給高 t丈 ，上廣 u丈 ，下廣 v丈 ，袤 w丈 ；乙縣鄉人給高 x丈 ，上廣 y丈 ，下廣 z丈 ，袤 a丈 。
"""

"""
This problem is extremely complex and involves a multi-step calculation process with numerous variables. It describes the construction of a platform and a path, with detailed instructions for calculating dimensions and allocations of work between two counties. Due to the length and complexity of the problem, I will break it into smaller sections and translate the procedure into Python code step by step.

Let's start with the first part: calculating the dimensions of the platform (臺). This involves determining the height, top width, bottom width, top length, and bottom length of the platform.

---

### Part 1: Calculating the dimensions of the platform (臺)



---

### Part 2: Allocating work for the platform (臺) between the two counties



---

### Part 3: Calculating the dimensions of the path (羨道)



---

### Part 4: Allocating work for the path (羨道) between the two counties



---

### Final Output


"""


from fractions import Fraction

# Given data
上下廣差 = 2  # Difference between top and bottom widths (in zhang)
上下袤差 = 4  # Difference between top and bottom lengths (in zhang)
高多上廣 = 11  # Height exceeds the top width by 11 zhang
程功常積 = 75  # Standard work volume per person (in chi^3)
甲縣差 = 1418  # Number of people from County A
乙縣差 = 3222  # Number of people from County B
限日 = 5  # Days allocated for constructing the platform

# Step 1: Calculate the total volume of the platform
臺積 = 程功常積 * (甲縣差 + 乙縣差) * 限日

# Step 2: Calculate the corner slant volumes (隅陽冪 and 隅頭冪)
隅陽冪 = Fraction(上下袤差 * 上下廣差, 3)  # Corner slant volume for the sides
隅陽截積 = 隅陽冪 * 高多上廣  # Corner slant volume multiplied by height

隅頭冪 = Fraction(上下廣差, 2) * 上下袤差  # Corner slant volume for the top
隅頭截積 = 隅頭冪 * 高多上廣  # Corner slant volume multiplied by height

# Step 3: Subtract corner slant volumes from total volume to get the main volume
實 = 臺積 - (隅陽截積 + 隅頭截積)

# Step 4: Calculate the divisor (方法) for determining the top width
正數 = Fraction(上下廣差 + 上下袤差, 2) + 上下袤差  # Corrected divisor
方法 = 正數 * 高多上廣 + 隅陽冪 + 隅頭冪

# Step 5: Calculate the top width (上廣)
廉法 = 高多上廣 + 上下袤差 + 正數  # Divisor for the cubic root
上廣 = (實 / 方法) ** Fraction(1, 3)  # Top width (cubic root of the ratio)

# Step 6: Calculate the bottom width, top length, bottom length, and height
下廣 = 上廣 + 上下廣差
上袤 = 上廣 + 上下袤差
下袤 = 上袤 + 上下袤差
臺高 = 上廣 + 高多上廣

# Output results for the platform
a = 臺高
b = 上廣
c = 下廣
d = 上袤
e = 下袤

# Step 1: Calculate the volume allocated to County B (乙縣)
乙積 = 程功常積 * 乙縣差 * 限日

# Step 2: Calculate the height for County B (乙高)
實 = 乙積 * 3 * 臺高 / (上下廣差 * 上下袤差)
乙高 = (實 / 方法) ** Fraction(1, 3)

# Step 3: Calculate the height for County A (甲高)
甲高 = 臺高 - 乙高

# Step 4: Calculate the top and bottom widths and lengths for County A
甲上廣 = 上廣 + (上下廣差 * 乙高 / 臺高)
甲下廣 = 甲上廣 + 上下廣差
甲上袤 = 上袤 + (上下袤差 * 乙高 / 臺高)
甲下袤 = 甲上袤 + 上下袤差

# Step 5: Assign County B's dimensions
乙上廣 = 上廣
乙下廣 = 下廣
乙上袤 = 上袤
乙下袤 = 下袤

# Output results for the counties
f = 甲高
g = 甲上廣
h = 甲下廣
i = 甲上袤
j = 甲下袤
k = 乙高
l = 乙上廣
m = 乙下廣
n = 乙上袤
o = 乙下袤

# Given data for the path
道上廣多下廣 = Fraction(12, 10)  # Top width exceeds bottom width by 1.2 zhang
少袤 = 104  # Shorter length (in chi)
高多袤 = 40  # Height exceeds length by 4 zhang
均賦常積 = 6300  # Standard work volume per village (in chi^3)
甲縣鄉數 = 13  # Number of villages in County A
乙縣鄉數 = 43  # Number of villages in County B

# Step 1: Calculate the total volume of the path
羨道積 = 均賦常積 * (甲縣鄉數 + 乙縣鄉數) * 6

# Step 2: Calculate the bottom width, top width, length, and height
下廣 = (羨道積 / (道上廣多下廣 + 少袤 + 高多袤)) ** Fraction(1, 3)
上廣 = 下廣 + 道上廣多下廣
袤 = 上廣 + 少袤
道高 = 袤 + 高多袤

# Output results for the path
p = 道高
q = 上廣
r = 下廣
s = 袤

# Step 1: Calculate the volume allocated to County A (甲縣)
甲積 = 均賦常積 * 甲縣鄉數 * 6

# Step 2: Calculate the length for County A (甲袤)
實 = 甲積 * 2 * 下廣 / (上下廣差 * 道高)
甲袤 = (實 / 方法) ** Fraction(1, 3)

# Step 3: Calculate the top and bottom widths and height for County A
甲上廣 = 下廣 + (上下廣差 * 甲袤 / 道高)
甲下廣 = 甲上廣 + 上下廣差
甲高 = 道高 * 甲袤 / 袤

# Step 4: Assign County B's dimensions
乙上廣 = 上廣
乙下廣 = 下廣
乙袤 = 袤
乙高 = 道高 - 甲高

# Output results for the counties
t = 甲高
u = 甲上廣
v = 甲下廣
w = 甲袤
x = 乙高
y = 乙上廣
z = 乙下廣
a = 乙袤

print(f"臺高 {a}丈 上廣 {b}丈 ，下廣 {c}丈 ，上袤 {d}丈 ，下袤 {e}丈")
print(f"甲縣給高 {f}丈 ，上廣 {g}丈 ，下廣 {h}丈 ，上袤 {i}丈 ，下袤 {j}丈")
print(f"乙縣給高 {k}丈 ，上廣 {l}丈 ，下廣 {m}丈 ，上袤 {n}丈 ，下袤 {o}丈")
print(f"羨道高 {p}丈 ，上廣 {q}丈 ，下廣 {r}丈 ，袤 {s}丈")
print(f"甲縣鄉人給高 {t}丈 ，上廣 {u}丈 ，下廣 {v}丈 ，袤 {w}丈")
print(f"乙縣鄉人給高 {x}丈 ，上廣 {y}丈 ，下廣 {z}丈 ，袤 {a}丈")


"""


This code follows the procedure described in the problem and calculates all the required dimensions and allocations. Note that the calculations involve fractions to ensure accuracy, as the original problem uses precise ratios.
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 129.62892766170813
Variable 'b' has wrong value. Expected: 7, Actual: 27.499586221864515
Variable 'c' has wrong value. Expected: 9, Actual: 29.499586221864515
Variable 'd' has wrong value. Expected: 10, Actual: 31.499586221864515
Variable 'e' has wrong value. Expected: 14, Actual: 35.49958622186452
Variable 'f' has wrong value. Expected: 9/2, Actual: -20.797118014720887
Variable 'g' has wrong value. Expected: 17/2, Actual: 30.579967600244622
Variable 'h' has wrong value. Expected: 9, Actual: 32.57996760024462
Variable 'i' has wrong value. Expected: 13, Actual: 37.66034897862473
Variable 'j' has wrong value. Expected: 14, Actual: 41.66034897862473
Variable 'k' has wrong value. Expected: 27/2, Actual: 59.296704236585406
Variable 'l' has wrong value. Expected: 7, Actual: 27.499586221864515
Variable 'm' has wrong value. Expected: 17/2, Actual: 29.499586221864515
Variable 'n' has wrong value. Expected: 10, Actual: 31.499586221864515
Variable 'o' has wrong value. Expected: 13, Actual: 35.49958622186452
Variable 'p' has wrong value. Expected: 18, Actual: 169.62892766170813
Variable 'q' has wrong value. Expected: 18/5, Actual: 25.628927661708136
Variable 'r' has wrong value. Expected: 12/5, Actual: 24.428927661708137
Variable 's' has wrong value. Expected: 14, Actual: 129.62892766170813
Variable 't' has wrong value. Expected: 9, Actual: 12.375432307988643
Variable 'u' has wrong value. Expected: 3, Actual: 24.540432181009542
Variable 'v' has wrong value. Expected: 12/5, Actual: 26.540432181009542
Variable 'w' has wrong value. Expected: 7, Actual: 9.457196019265758
Variable 'x' has wrong value. Expected: 9, Actual: 157.2534953537195
Variable 'y' has wrong value. Expected: 18/5, Actual: 25.628927661708136
Variable 'z' has wrong value. Expected: 3, Actual: 24.428927661708137
Missing variable in output: '{'"""
