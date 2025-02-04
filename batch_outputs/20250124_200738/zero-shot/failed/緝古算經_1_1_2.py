"""
假令太史造仰觀臺，上廣袤少，下廣袤多。上下廣差二丈，上下袤差四丈，上廣袤差三丈，高多上廣一十一丈，甲縣差一千四百一十八人，乙縣差三千二百二十二人，夏程人功常積七十五尺，限五日役臺畢。羨道從臺南面起，上廣多下廣一丈二尺，少袤一百四尺，高多袤四丈。甲縣一十三鄉，乙縣四十三鄉，每鄉別均賦常積六千三百尺，限一日役羨道畢。二縣差到人共造仰觀臺，二縣鄉人共造羨道，皆從先給甲縣，以次與乙縣。臺自下基給高，道自初登給袤。問：臺道廣、高、袤及縣別給高、廣、袤各幾何？
術曰：以程功尺數乘二縣人，又以限日乘之，為臺積。又以上下袤差乘上下廣差，三而一，為隅陽冪。以乘截高，為隅陽截積。又半上下廣差，乘斬上袤，為隅頭冪。以乘截高，為隅頭截積。並二積，以減臺積，余為實。以上下廣差並上下袤差，半之，為正數，加截上袤，以乘截高，所得增隅陽冪加隅頭冪，為方法。又並截高及截上袤與正數，為廉法，從。開立方除之，即得上廣。各加差，得臺下廣及上下袤、高。求均給積尺受廣袤，術曰：以程功尺數乘乙縣人，又以限日乘之，為乙積。三因之，又以高冪乘之，以上下廣差乘袤差而一，為實。又以臺高乘上廣，廣差而一，為上廣之高。又以臺高乘上袤，袤差而一，為上袤之高。又以上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即乙高。以減本高，余即甲高。此是從下給臺甲高。又以廣差乘乙高，以本高而一，所得加上廣，即甲上廣。又以袤差乘乙高，如本高而一，所得加上袤，即甲上袤。其上廣、袤即乙下廣、袤，臺上廣、袤即乙上廣、袤。其後求廣、袤，有增損者，皆放此。求羨道廣、袤、高，術曰：以均賦常積乘二縣五十六鄉，又六因，為積。又以道上廣多下廣數加上廣少袤，為下廣少袤。又以高多袤加下廣少袤，為下廣少高。以乘下廣少袤，為隅陽冪。又以下廣少上廣乘之，為鱉隅積。以減積，余三而一，為實。並下廣少袤與下廣少高，以下廣少上廣乘之，鱉從橫廉冪。三而一，加隅冪，為方法。又以三除上廣多下廣，以下廣少袤、下廣少高加之，為廉法，從。開立方除之，即下廣。加廣差，即上廣。加袤多上廣於上廣，即袤。加高多袤，即道高。求羨道均給積尺甲縣受廣、袤，術曰：以均賦常積乘甲縣上十三鄉，又六因，為積。以袤再乘之，以道上下廣差乘臺高為法而一，為實。又三因下廣，以袤乘之，如上下廣差而一，為都廉，從。開立方除之，即甲袤。以廣差乘甲袤，本袤而一，以下廣加之，即甲上廣。又以臺高乘甲袤，本袤除之，即甲高。
答曰：臺高 a丈 上廣 b丈 ，下廣 c丈 ，上袤 d丈 ，下袤 e丈 ；甲縣給高 f丈 ，上廣 g丈 ，下廣 h丈 ，上袤 i丈 ，下袤 j丈 ；乙縣給高 k丈 ，上廣 l丈 ，下廣 m丈 ，上袤 n丈 ，下袤 o丈 ；羨道高 p丈 ，上廣 q丈 ，下廣 r丈 ，袤 s丈 ；甲縣鄉人給高 t丈 ，上廣 u丈 ，下廣 v丈 ，袤 w丈 ；乙縣鄉人給高 x丈 ，上廣 y丈 ，下廣 z丈 ，袤 a丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical problem into Python code. The solution will involve using the `Fraction` class from the `fractions` module to handle fractional values. Let's compute the values of the unknowns step by step.


"""

#----- content starts here -----

from fractions import Fraction

# Given constants
上下廣差 = Fraction(2)  # 2丈
上下袤差 = Fraction(4)  # 4丈
上廣袤差 = Fraction(3)  # 3丈
高多上廣 = Fraction(11)  # 11丈
甲縣差 = Fraction(1418)  # 1418人
乙縣差 = Fraction(3222)  # 3222人
夏程人功常積 = Fraction(75)  # 75尺
限日臺 = Fraction(5)  # 5日
羨道上廣多下廣 = Fraction(1, 5)  # 1丈2尺 = 1.2丈
羨道少袤 = Fraction(104)  # 104尺
羨道高多袤 = Fraction(4)  # 4丈
甲縣鄉數 = Fraction(13)  # 13鄉
乙縣鄉數 = Fraction(43)  # 43鄉
均賦常積 = Fraction(6300)  # 6300尺
限日羨道 = Fraction(1)  # 1日

# Step 1: Compute the total volume of the 仰觀臺
臺積 = 夏程人功常積 * (甲縣差 + 乙縣差) * 限日臺

# Step 2: Compute 隅陽冪 and 隅陽截積
隅陽冪 = (上下袤差 * 上下廣差) / 3
隅陽截積 = 隅陽冪 * 高多上廣

# Step 3: Compute 隅頭冪 and 隅頭截積
隅頭冪 = (上下廣差 / 2) * (上廣袤差)
隅頭截積 = 隅頭冪 * 高多上廣

# Step 4: Compute the actual volume
實 = 臺積 - (隅陽截積 + 隅頭截積)

# Step 5: Compute 正數 and 方法
正數 = ((上下廣差 + 上下袤差) / 2) + 上廣袤差
方法 = (正數 * 高多上廣) + 隅陽冪 + 隅頭冪

# Step 6: Compute 廉法
廉法 = 正數 + 高多上廣 + 上廣袤差

# Step 7: Solve for 上廣 (b)
b = (實 / 方法) ** Fraction(1, 3)

# Step 8: Compute other dimensions of the 仰觀臺
c = b + 上下廣差  # 下廣
d = b + 上廣袤差  # 上袤
e = d + 上下袤差  # 下袤
a = b + 高多上廣  # 高

# Step 9: Compute the contributions of 甲縣 and 乙縣 to the 仰觀臺
乙積 = 夏程人功常積 * 乙縣差 * 限日臺
乙高 = (乙積 / (上下廣差 * 上下袤差)) ** Fraction(1, 3)
f = a - 乙高  # 甲縣給高
g = b + (上下廣差 * 乙高 / a)  # 甲縣上廣
h = g + 上下廣差  # 甲縣下廣
i = d + (上下袤差 * 乙高 / a)  # 甲縣上袤
j = i + 上下袤差  # 甲縣下袤
k = 乙高  # 乙縣給高
l = g  # 乙縣上廣
m = h  # 乙縣下廣
n = i  # 乙縣上袤
o = j  # 乙縣下袤

# Step 10: Compute the dimensions of the 羨道
羨道積 = 均賦常積 * (甲縣鄉數 + 乙縣鄉數) * 6
下廣少袤 = 羨道上廣多下廣 + 羨道少袤
下廣少高 = 羨道高多袤 + 下廣少袤
隅陽冪_羨道 = 下廣少袤 * 下廣少高
鱉隅積 = (羨道上廣多下廣 * 下廣少袤)
實_羨道 = (羨道積 - 隅陽冪_羨道 - 鱉隅積) / 3
方法_羨道 = 隅陽冪_羨道 + 鱉隅積
廉法_羨道 = 羨道上廣多下廣 + 下廣少袤 + 下廣少高
r = (實_羨道 / 方法_羨道) ** Fraction(1, 3)  # 下廣
q = r + 羨道上廣多下廣  # 上廣
s = q + 羨道少袤  # 袤
p = s + 羨道高多袤  # 高

# Step 11: Compute the contributions of 甲縣 and 乙縣 to the 羨道
甲積_羨道 = 均賦常積 * 甲縣鄉數 * 6
w = (甲積_羨道 / (上下廣差 * a)) ** Fraction(1, 3)  # 甲縣袤
u = r + (上下廣差 * w / s)  # 甲縣上廣
v = u + 上下廣差  # 甲縣下廣
t = p - (a * w / s)  # 甲縣高
x = p - t  # 乙縣高
y = q - u  # 乙縣上廣
z = r - v  # 乙縣下廣
a = s - w  # 乙縣袤

# Final results
print(f"臺高 a={a}丈 上廣 b={b}丈 下廣 c={c}丈 上袤 d={d}丈 下袤 e={e}丈")
print(f"甲縣給高 f={f}丈 上廣 g={g}丈 下廣 h={h}丈 上袤 i={i}丈 下袤 j={j}丈")
print(f"乙縣給高 k={k}丈 上廣 l={l}丈 下廣 m={m}丈 上袤 n={n}丈 下袤 o={o}丈")
print(f"羨道高 p={p}丈 上廣 q={q}丈 下廣 r={r}丈 袤 s={s}丈")
print(f"甲縣鄉人給高 t={t}丈 上廣 u={u}丈 下廣 v={v}丈 袤 w={w}丈")
print(f"乙縣鄉人給高 x={x}丈 上廣 y={y}丈 下廣 z={z}丈 袤 a={a}丈")
#----- content ends here -----


"""


This Python code follows the ancient Chinese mathematical procedure to compute the unknowns step by step. Each variable corresponds to the unknowns in the problem, and the results are printed at the end.
"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 89.84011260656544
Variable 'b' has wrong value. Expected: 7, Actual: 28.956017354706564
Variable 'c' has wrong value. Expected: 9, Actual: 30.956017354706564
Variable 'd' has wrong value. Expected: 10, Actual: 31.956017354706564
Variable 'e' has wrong value. Expected: 14, Actual: 35.95601735470656
Variable 'f' has wrong value. Expected: 9/2, Actual: -13.298396086274991
Variable 'g' has wrong value. Expected: 17/2, Actual: 31.62166908712121
Variable 'h' has wrong value. Expected: 9, Actual: 33.621669087121205
Variable 'i' has wrong value. Expected: 13, Actual: 37.28732081953585
Variable 'j' has wrong value. Expected: 14, Actual: 41.28732081953585
Variable 'k' has wrong value. Expected: 27/2, Actual: 53.25441344098155
Variable 'l' has wrong value. Expected: 7, Actual: 31.62166908712121
Variable 'm' has wrong value. Expected: 17/2, Actual: 33.621669087121205
Variable 'n' has wrong value. Expected: 10, Actual: 37.28732081953585
Variable 'o' has wrong value. Expected: 13, Actual: 41.28732081953585
Variable 'p' has wrong value. Expected: 18, Actual: 112.16076723922492
Variable 'q' has wrong value. Expected: 18/5, Actual: 4.16076723922492
Variable 'r' has wrong value. Expected: 12/5, Actual: 3.96076723922492
Variable 's' has wrong value. Expected: 14, Actual: 108.16076723922492
Variable 't' has wrong value. Expected: 9, Actual: 105.39287521019484
Variable 'u' has wrong value. Expected: 3, Actual: 4.299534337504442
Variable 'v' has wrong value. Expected: 12/5, Actual: 6.299534337504442
Variable 'w' has wrong value. Expected: 7, Actual: 18.32065463265949
Variable 'x' has wrong value. Expected: 9, Actual: 6.7678920290300795
Variable 'y' has wrong value. Expected: 18/5, Actual: -0.13876709827952194
Variable 'z' has wrong value. Expected: 3, Actual: -2.3387670982795217
Missing variable in output: '{'"""
