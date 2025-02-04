"""
假令太史造仰觀臺，上廣袤少，下廣袤多。上下廣差二丈，上下袤差四丈，上廣袤差三丈，高多上廣一十一丈，甲縣差一千四百一十八人，乙縣差三千二百二十二人，夏程人功常積七十五尺，限五日役臺畢。羨道從臺南面起，上廣多下廣一丈二尺，少袤一百四尺，高多袤四丈。甲縣一十三鄉，乙縣四十三鄉，每鄉別均賦常積六千三百尺，限一日役羨道畢。二縣差到人共造仰觀臺，二縣鄉人共造羨道，皆從先給甲縣，以次與乙縣。臺自下基給高，道自初登給袤。問：臺道廣、高、袤及縣別給高、廣、袤各幾何？
術曰：以程功尺數乘二縣人，又以限日乘之，為臺積。又以上下袤差乘上下廣差，三而一，為隅陽冪。以乘截高，為隅陽截積。又半上下廣差，乘斬上袤，為隅頭冪。以乘截高，為隅頭截積。並二積，以減臺積，余為實。以上下廣差並上下袤差，半之，為正數，加截上袤，以乘截高，所得增隅陽冪加隅頭冪，為方法。又並截高及截上袤與正數，為廉法，從。開立方除之，即得上廣。各加差，得臺下廣及上下袤、高。求均給積尺受廣袤，術曰：以程功尺數乘乙縣人，又以限日乘之，為乙積。三因之，又以高冪乘之，以上下廣差乘袤差而一，為實。又以臺高乘上廣，廣差而一，為上廣之高。又以臺高乘上袤，袤差而一，為上袤之高。又以上廣之高乘上袤之高，三之，為方法。又並兩高，三之，二而一，為廉法，從。開立方除之，即乙高。以減本高，余即甲高。此是從下給臺甲高。又以廣差乘乙高，以本高而一，所得加上廣，即甲上廣。又以袤差乘乙高，如本高而一，所得加上袤，即甲上袤。其上廣、袤即乙下廣、袤，臺上廣、袤即乙上廣、袤。其後求廣、袤，有增損者，皆放此。求羨道廣、袤、高，術曰：以均賦常積乘二縣五十六鄉，又六因，為積。又以道上廣多下廣數加上廣少袤，為下廣少袤。又以高多袤加下廣少袤，為下廣少高。以乘下廣少袤，為隅陽冪。又以下廣少上廣乘之，為鱉隅積。以減積，余三而一，為實。並下廣少袤與下廣少高，以下廣少上廣乘之，鱉從橫廉冪。三而一，加隅冪，為方法。又以三除上廣多下廣，以下廣少袤、下廣少高加之，為廉法，從。開立方除之，即下廣。加廣差，即上廣。加袤多上廣於上廣，即袤。加高多袤，即道高。求羨道均給積尺甲縣受廣、袤，術曰：以均賦常積乘甲縣上十三鄉，又六因，為積。以袤再乘之，以道上下廣差乘臺高為法而一，為實。又三因下廣，以袤乘之，如上下廣差而一，為都廉，從。開立方除之，即甲袤。以廣差乘甲袤，本袤而一，以下廣加之，即甲上廣。又以臺高乘甲袤，本袤除之，即甲高。
答曰：臺高 a(=18)丈 上廣 b(=7)丈 ，下廣 c(=9)丈 ，上袤 d(=10)丈 ，下袤 e(=14)丈 ；甲縣給高 f(=9/2)丈 ，上廣 g(=17/2)丈 ，下廣 h(=9)丈 ，上袤 i(=13)丈 ，下袤 j(=14)丈 ；乙縣給高 k(=27/2)丈 ，上廣 l(=7)丈 ，下廣 m(=17/2)丈 ，上袤 n(=10)丈 ，下袤 o(=13)丈 ；羨道高 p(=18)丈 ，上廣 q(=18/5)丈 ，下廣 r(=12/5)丈 ，袤 s(=14)丈 ；甲縣鄉人給高 t(=9)丈 ，上廣 u(=3)丈 ，下廣 v(=12/5)丈 ，袤 w(=7)丈 ；乙縣鄉人給高 x(=9)丈 ，上廣 y(=18/5)丈 ，下廣 z(=3)丈 ，袤 a(=7)丈 。
"""

"""
This problem is extremely complex and involves multiple steps of calculations for determining the dimensions of the Tai (platform) and the Xian Dao (path), as well as the distribution of labor and resources between two counties (甲縣 and 乙縣). The solution requires careful application of ancient Chinese mathematical procedures, including volume calculations, proportional distributions, and iterative adjustments.

Below is the Python implementation of the solution, following the structure of the ancient procedure ("術"). Each section of the code is preceded by comments explaining the corresponding part of the procedure.


"""

#----- content starts here -----

from fractions import Fraction

# Constants and given values
穿地積 = 10000  # Dug-out earth volume in chi
甲縣差 = 1418  # People from 甲縣
乙縣差 = 3222  # People from 乙縣
夏程人功常積 = 75  # Standard work per person in chi^3
限日 = 5  # Days to complete the Tai
羨道鄉數 = 56  # Total number of villages for the path
甲縣鄉數 = 13  # Villages in 甲縣
乙縣鄉數 = 43  # Villages in 乙縣
均賦常積 = 6300  # Standard work per village in chi^3

# Tai dimensions and differences
上下廣差 = 2  # Difference between upper and lower widths in zhang
上下袤差 = 4  # Difference between upper and lower lengths in zhang
上廣袤差 = 3  # Difference between upper width and upper length in zhang
高多上廣 = 11  # Height exceeds upper width by 11 zhang

# Path dimensions and differences
上廣多下廣 = Fraction(12, 10)  # Upper width exceeds lower width by 1.2 zhang
少袤 = 104  # Shorter length in chi
高多袤 = 40  # Height exceeds length by 4 zhang

# Step 1: Calculate Tai dimensions
# Calculate the total volume of the Tai
臺積 = 夏程人功常積 * (甲縣差 + 乙縣差) * 限日

# Calculate 隅陽冪 (corner slant volume)
隅陽冪 = Fraction(上下袤差 * 上下廣差, 3)

# Calculate 隅陽截積 (corner slant cross-section volume)
隅陽截積 = 隅陽冪 * 高多上廣

# Calculate 隅頭冪 (corner top volume)
隅頭冪 = Fraction(上下廣差, 2) * 上廣袤差

# Calculate 隅頭截積 (corner top cross-section volume)
隅頭截積 = 隅頭冪 * 高多上廣

# Combine the two volumes and subtract from total volume
實 = 臺積 - (隅陽截積 + 隅頭截積)

# Calculate 正數 (base divisor)
正數 = Fraction(上下廣差 + 上下袤差, 2) + 上廣袤差

# Calculate 方法 (method divisor)
方法 = 正數 * 高多上廣 + 隅陽冪 + 隅頭冪

# Calculate 廉法 (edge divisor)
廉法 = 高多上廣 + 上廣袤差 + 正數

# Solve for 上廣 (upper width)
上廣 = Fraction(實, 方法)

# Calculate other dimensions
下廣 = 上廣 + 上下廣差
上袤 = 上廣 + 上廣袤差
下袤 = 上袤 + 上下袤差
臺高 = 上廣 + 高多上廣

# Step 2: Calculate labor distribution for Tai
# Calculate 乙縣積 (乙縣's total work volume)
乙積 = 夏程人功常積 * 乙縣差 * 限日

# Calculate 乙高 (乙縣's height contribution)
乙高 = Fraction(乙積, 方法)

# Calculate 甲高 (甲縣's height contribution)
甲高 = 臺高 - 乙高

# Calculate 甲上廣 (甲縣's upper width contribution)
甲上廣 = 上廣 + Fraction(上下廣差 * 乙高, 臺高)

# Calculate 甲上袤 (甲縣's upper length contribution)
甲上袤 = 上袤 + Fraction(上下袤差 * 乙高, 臺高)

# Step 3: Calculate Path dimensions
# Calculate total path volume
羨道積 = 均賦常積 * 羨道鄉數 * 6

# Calculate 下廣少袤 (lower width and shorter length)
下廣少袤 = 上廣多下廣 + 少袤

# Calculate 下廣少高 (lower width and shorter height)
下廣少高 = 高多袤 + 下廣少袤

# Calculate 隅陽冪 for path
隅陽冪_道 = 下廣少袤 * 下廣少高

# Calculate 鱉隅積 (turtle corner volume)
鱉隅積 = 下廣少袤 * 上廣多下廣

# Calculate path dimensions
實_道 = Fraction(羨道積 - 鱉隅積, 3)
方法_道 = 隅陽冪_道 + 鱉隅積
廉法_道 = 上廣多下廣 + 下廣少袤 + 下廣少高

下廣_道 = Fraction(實_道, 方法_道)
上廣_道 = 下廣_道 + 上廣多下廣
袤_道 = 上廣_道 + 少袤
道高 = 袤_道 + 高多袤

# Step 4: Labor distribution for Path
# Calculate 甲縣's contribution to path
甲積_道 = 均賦常積 * 甲縣鄉數 * 6
甲袤_道 = Fraction(甲積_道, 方法_道)
甲上廣_道 = 下廣_道 + Fraction(上下廣差 * 甲袤_道, 袤_道)
甲高_道 = Fraction(臺高 * 甲袤_道, 袤_道)

# Calculate 乙縣's contribution to path
乙積_道 = 羨道積 - 甲積_道
乙袤_道 = 袤_道 - 甲袤_道
乙上廣_道 = 上廣_道 - 甲上廣_道
乙高_道 = 道高 - 甲高_道

# Final results
print(f"臺高: {臺高}丈, 上廣: {上廣}丈, 下廣: {下廣}丈, 上袤: {上袤}丈, 下袤: {下袤}丈")
print(f"甲縣給高: {甲高}丈, 上廣: {甲上廣}丈, 下廣: {下廣}丈, 上袤: {甲上袤}丈, 下袤: {下袤}丈")
print(f"乙縣給高: {乙高}丈, 上廣: {上廣}丈, 下廣: {下廣}丈, 上袤: {上袤}丈, 下袤: {下袤}丈")
print(f"羨道高: {道高}丈, 上廣: {上廣_道}丈, 下廣: {下廣_道}丈, 袤: {袤_道}丈")
print(f"甲縣鄉人給高: {甲高_道}丈, 上廣: {甲上廣_道}丈, 下廣: {下廣_道}丈, 袤: {甲袤_道}丈")
print(f"乙縣鄉人給高: {乙高_道}丈, 上廣: {乙上廣_道}丈, 下廣: {下廣_道}丈, 袤: {乙袤_道}丈")
#----- content ends here -----


"""


This code follows the ancient procedure step by step, using Python's `Fraction` class to handle fractional arithmetic precisely. Each variable corresponds to a specific part of the problem, and the calculations are performed in the order described in the procedure.
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'
Missing variable in output: 'c'
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'
Missing variable in output: 'g'
Missing variable in output: 'h'
Missing variable in output: 'i'
Missing variable in output: 'j'
Missing variable in output: 'k'
Missing variable in output: 'l'
Missing variable in output: 'm'
Missing variable in output: 'n'
Missing variable in output: 'o'
Missing variable in output: 'p'
Missing variable in output: 'q'
Missing variable in output: 'r'
Missing variable in output: 's'
Missing variable in output: 't'
Missing variable in output: 'u'
Missing variable in output: 'v'
Missing variable in output: 'w'
Missing variable in output: 'x'
Missing variable in output: 'y'
Missing variable in output: 'z'
Missing variable in output: '{'"""
