"""
假令太史造仰觀臺，上廣袤少，下廣袤多。上下廣差二丈，上下袤差四丈，上廣袤差三丈，高多上廣一十一丈，甲縣差一千四百一十八人，乙縣差三千二百二十二人，夏程人功常積七十五尺，限五日役臺畢。羨道從臺南面起，上廣多下廣一丈二尺，少袤一百四尺，高多袤四丈。甲縣一十三鄉，乙縣四十三鄉，每鄉別均賦常積六千三百尺，限一日役羨道畢。二縣差到人共造仰觀臺，二縣鄉人共造羨道，皆從先給甲縣，以次與乙縣。臺自下基給高，道自初登給袤。問：臺道廣、高、袤及縣別給高、廣、袤各幾何？
術曰：以程功尺數乘二縣人，又以限日乘之，為臺積。又以上下袤差乘上下廣差，三而一，為隅陽冪。以乘截高，為隅陽截積。又半上下廣差，乘斬上袤，為隅頭冪。以乘截高，為隅頭截積。並二積，以減臺積，余為實。以上下廣差並上下袤差，半之，為正數，加截上袤，以乘截高，所得增隅陽冪加隅頭冪，為方法。又並截高及截上袤與正數，為廉法，從。開立方除之，即得上廣。各加差，得臺下廣及上下袤、高。求均給積尺受廣袤，術曰：以程功尺數乘乙縣人，又以限日乘之，為乙積。三因之，又以高冪乘之，以上下廣差乘袤差而一，為實。又以臺高乘上廣，廣差而一，為上廣之高。又以臺高乘上袤，袤差而一，為上袤之高。又以上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即乙高。以減本高，余即甲高。此是從下給臺甲高。又以廣差乘乙高，以本高而一，所得加上廣，即甲上廣。又以袤差乘乙高，如本高而一，所得加上袤，即甲上袤。其上廣、袤即乙下廣、袤，臺上廣、袤即乙上廣、袤。其後求廣、袤，有增損者，皆放此。求羨道廣、袤、高，術曰：以均賦常積乘二縣五十六鄉，又六因，為積。又以道上廣多下廣數加上廣少袤，為下廣少袤。又以高多袤加下廣少袤，為下廣少高。以乘下廣少袤，為隅陽冪。又以下廣少上廣乘之，為鱉隅積。以減積，余三而一，為實。並下廣少袤與下廣少高，以下廣少上廣乘之，鱉從橫廉冪。三而一，加隅冪，為方法。又以三除上廣多下廣，以下廣少袤、下廣少高加之，為廉法，從。開立方除之，即下廣。加廣差，即上廣。加袤多上廣於上廣，即袤。加高多袤，即道高。求羨道均給積尺甲縣受廣、袤，術曰：以均賦常積乘甲縣上十三鄉，又六因，為積。以袤再乘之，以道上下廣差乘臺高為法而一，為實。又三因下廣，以袤乘之，如上下廣差而一，為都廉，從。開立方除之，即甲袤。以廣差乘甲袤，本袤而一，以下廣加之，即甲上廣。又以臺高乘甲袤，本袤除之，即甲高。
答曰：臺高 a丈 上廣 b丈 ，下廣 c丈 ，上袤 d丈 ，下袤 e丈 ；甲縣給高 f丈 ，上廣 g丈 ，下廣 h丈 ，上袤 i丈 ，下袤 j丈 ；乙縣給高 k丈 ，上廣 l丈 ，下廣 m丈 ，上袤 n丈 ，下袤 o丈 ；羨道高 p丈 ，上廣 q丈 ，下廣 r丈 ，袤 s丈 ；甲縣鄉人給高 t丈 ，上廣 u丈 ，下廣 v丈 ，袤 w丈 ；乙縣鄉人給高 x丈 ，上廣 y丈 ，下廣 z丈 ，袤 a丈 。
"""

"""
Here is the Python code that translates the ancient Chinese math problem into computations for the unknowns. The solutions are stored in variables named as specified in the answer.


"""


from fractions import Fraction

# Constants and given values
程功常積 = Fraction(75)  # 每人每日功積，單位：尺
臺限日 = 5  # 臺限日，單位：日
羨道限日 = 1  # 羨道限日，單位：日
甲縣差 = 1418  # 甲縣差人數
乙縣差 = 3222  # 乙縣差人數
甲縣鄉數 = 13  # 甲縣鄉數
乙縣鄉數 = 43  # 乙縣鄉數
均賦常積 = Fraction(6300)  # 每鄉每日均賦常積，單位：尺

# 臺的上下廣差、上下袤差、上廣袤差、高多上廣
上下廣差 = Fraction(2)  # 單位：丈
上下袤差 = Fraction(4)  # 單位：丈
上廣袤差 = Fraction(3)  # 單位：丈
高多上廣 = Fraction(11)  # 單位：丈

# 羨道的上廣多下廣、少袤、高多袤
羨道上廣多下廣 = Fraction(1, 5)  # 單位：丈
羨道少袤 = Fraction(104)  # 單位：尺
羨道高多袤 = Fraction(4)  # 單位：丈

# 臺的計算
臺積 = 程功常積 * (甲縣差 + 乙縣差) * 臺限日  # 臺積，單位：尺³
隅陽冪 = (上下袤差 * 上下廣差) / 3  # 隅陽冪，單位：丈²
隅陽截積 = 隅陽冪 * 高多上廣  # 隅陽截積，單位：丈³
隅頭冪 = (上下廣差 / 2) * (上廣袤差)  # 隅頭冪，單位：丈²
隅頭截積 = 隅頭冪 * 高多上廣  # 隅頭截積，單位：丈³
實 = 臺積 - (隅陽截積 + 隅頭截積)  # 實，單位：丈³
正數 = ((上下廣差 + 上下袤差) / 2) + 上廣袤差  # 正數，單位：丈
方法 = 隅陽冪 + 隅頭冪 + 正數 * 高多上廣  # 方法，單位：丈³
廉法 = 高多上廣 + 上廣袤差 + 正數  # 廉法，單位：丈
b = (實 / 方法) ** Fraction(1, 3)  # 上廣 b，單位：丈
c = b + 上下廣差  # 下廣 c，單位：丈
d = b + 上廣袤差  # 上袤 d，單位：丈
e = d + 上下袤差  # 下袤 e，單位：丈
a = b + 高多上廣  # 臺高 a，單位：丈

# 甲縣和乙縣給臺的計算
乙積 = 程功常積 * 乙縣差 * 臺限日  # 乙積，單位：尺³
乙高 = (乙積 / (隅陽冪 + 隅頭冪)) ** Fraction(1, 3)  # 乙高 k，單位：丈
f = a - 乙高  # 甲高 f，單位：丈
g = b + (上下廣差 * f / a)  # 甲上廣 g，單位：丈
h = g + 上下廣差  # 甲下廣 h，單位：丈
i = d + (上下袤差 * f / a)  # 甲上袤 i，單位：丈
j = i + 上下袤差  # 甲下袤 j，單位：丈
k = 乙高  # 乙高 k，單位：丈
l = g  # 乙上廣 l，單位：丈
m = h  # 乙下廣 m，單位：丈
n = i  # 乙上袤 n，單位：丈
o = j  # 乙下袤 o，單位：丈

# 羨道的計算
羨道積 = 均賦常積 * (甲縣鄉數 + 乙縣鄉數) * 羨道限日  # 羨道積，單位：尺³
下廣少袤 = 羨道上廣多下廣 + 羨道少袤  # 下廣少袤，單位：丈
下廣少高 = 羨道高多袤 + 下廣少袤  # 下廣少高，單位：丈
隅陽冪 = 下廣少袤 * 下廣少高  # 隅陽冪，單位：丈²
鱉隅積 = (羨道上廣多下廣 * 下廣少袤) / 3  # 鱉隅積，單位：丈³
實 = (羨道積 - 鱉隅積) / 3  # 實，單位：丈³
方法 = 隅陽冪 + 鱉隅積  # 方法，單位：丈³
廉法 = 羨道上廣多下廣 + 下廣少袤 + 下廣少高  # 廉法，單位：丈
r = (實 / 方法) ** Fraction(1, 3)  # 下廣 r，單位：丈
q = r + 羨道上廣多下廣  # 上廣 q，單位：丈
s = q + 羨道少袤  # 袤 s，單位：丈
p = s + 羨道高多袤  # 羨道高 p，單位：丈

# 甲縣和乙縣給羨道的計算
甲積 = 均賦常積 * 甲縣鄉數 * 羨道限日  # 甲積，單位：尺³
w = (甲積 / (羨道上廣多下廣 * p)) ** Fraction(1, 3)  # 甲袤 w，單位：丈
u = r + (羨道上廣多下廣 * w / s)  # 甲上廣 u，單位：丈
v = u + 羨道上廣多下廣  # 甲下廣 v，單位：丈
t = p - (羨道高多袤 * w / s)  # 甲高 t，單位：丈
x = p - t  # 乙高 x，單位：丈
y = q - u  # 乙上廣 y，單位：丈
z = r - v  # 乙下廣 z，單位：丈
a = s - w  # 乙袤 a，單位：丈


"""

"""


"""
Variable 'a' has wrong value. Expected: 18, Actual: 90.90407373918055
Variable 'b' has wrong value. Expected: 7, Actual: 28.956017354706564
Variable 'c' has wrong value. Expected: 9, Actual: 30.956017354706564
Variable 'd' has wrong value. Expected: 10, Actual: 31.956017354706564
Variable 'e' has wrong value. Expected: 14, Actual: 35.95601735470656
Variable 'f' has wrong value. Expected: 9/2, Actual: -19.785517902477558
Variable 'g' has wrong value. Expected: 17/2, Actual: 27.965652487916508
Variable 'h' has wrong value. Expected: 9, Actual: 29.965652487916508
Variable 'i' has wrong value. Expected: 13, Actual: 29.97528762112645
Variable 'j' has wrong value. Expected: 14, Actual: 33.975287621126455
Variable 'k' has wrong value. Expected: 27/2, Actual: 59.74153525718412
Variable 'l' has wrong value. Expected: 7, Actual: 27.965652487916508
Variable 'm' has wrong value. Expected: 17/2, Actual: 29.965652487916508
Variable 'n' has wrong value. Expected: 10, Actual: 29.97528762112645
Variable 'o' has wrong value. Expected: 13, Actual: 33.975287621126455
Variable 'p' has wrong value. Expected: 18, Actual: 110.38446669899878
Variable 'q' has wrong value. Expected: 18/5, Actual: 2.384466698998783
Variable 'r' has wrong value. Expected: 12/5, Actual: 2.184466698998783
Variable 's' has wrong value. Expected: 14, Actual: 106.38446669899878
Variable 't' has wrong value. Expected: 9, Actual: 109.80241206489066
Variable 'u' has wrong value. Expected: 3, Actual: 2.213569430704189
Variable 'v' has wrong value. Expected: 12/5, Actual: 2.413569430704189
Variable 'w' has wrong value. Expected: 7, Actual: 15.480392959818227
Variable 'x' has wrong value. Expected: 9, Actual: 0.5820546341081183
Variable 'y' has wrong value. Expected: 18/5, Actual: 0.17089726829459417
Variable 'z' has wrong value. Expected: 3, Actual: -0.22910273170540618
Missing variable in output: '{'"""
