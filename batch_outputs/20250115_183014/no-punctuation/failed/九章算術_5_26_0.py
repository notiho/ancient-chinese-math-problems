"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
荅曰七萬六百六十六尺太半尺
負土往來七十步其二十步上下棚除棚除二當平道五踟躕之間十加一載輸之間三十步定一返一百四十步土籠積一尺六寸秋程人功行五十九里半問人到積尺用徒各幾何
術曰以一籠積尺乘程行步數為實往來上下棚除二當平道五置定往來步數十加一及載輸之間三十步以為法除之所得即一人所到尺以所到約積尺即用徒人數
荅曰人到 a尺 用徒 b人 
"""

"""
Suppose there is a basin-shaped pond. The top width is 6 zhang, the top length is 8 zhang. 
The bottom width is 4 zhang, the bottom length is 6 zhang. The depth is 2 zhang.
Question: what is the volume?

Answer: 76066.5 chi³.

For moving the soil, the round trip is 70 bu. Of these, 20 bu are for the upper and lower shelves, 
and the shelves are equivalent to 2 bu of flat ground. For the flat ground, 5 bu are for hesitation, 
10 bu are for adding one load, and 30 bu are for the loading and unloading interval. 
One round trip is 140 bu. The soil basket holds 1 chi 6 cun of volume. 
In autumn, the work rate is 59.5 li per person per day. 
Question: how much soil does one person move, and how many workers are needed?

The procedure says: Multiply the volume of one basket by the total number of steps in the round trip, obtaining the dividend.
For the divisor, place the round trip steps (70), add the hesitation steps (10), and the loading/unloading interval (30).
Divide the dividend by the divisor to obtain the volume moved by one person.
Divide the total volume by the volume moved by one person to find the number of workers needed.

Answer: one person moves *a* chi³, and *b* workers are needed.
"""

from fractions import Fraction

# Dimensions of the pond
上廣 = 6  # Top width in zhang
上袤 = 8  # Top length in zhang
下廣 = 4  # Bottom width in zhang
下袤 = 6  # Bottom length in zhang
深 = 2    # Depth in zhang

# Convert all dimensions to chi (1 zhang = 10 chi)
上廣 *= 10
上袤 *= 10
下廣 *= 10
下袤 *= 10
深 *= 10

# Volume of the pond
# Volume formula for a frustum: V = (1/6) * 深 * (上廣 * 上袤 + 下廣 * 下袤 + sqrt(上廣 * 上袤 * 下廣 * 下袤))
積 = Fraction(1, 6) * 深 * (上廣 * 上袤 + 下廣 * 下袤 + (上廣 * 上袤 * 下廣 * 下袤) ** 0.5)

# Soil movement parameters
往來步數 = 70  # Round trip steps
上下棚步數 = 20  # Steps for shelves
棚當平道 = 2  # Shelves equivalent to flat ground
平道踟躕步數 = 5  # Hesitation steps
加載步數 = 10  # Steps to add one load
載輸步數 = 30  # Loading/unloading interval steps
一籠積 = Fraction(1, 6)  # Volume of one basket (1 chi 6 cun = 1.5 chi)

# Adjusted round trip steps
棚當平道步數 = Fraction(上下棚步數, 棚當平道)
總步數 = 往來步數 + 平道踟躕步數 + 加載步數 + 載輸步數 + 棚當平道步數

# Volume moved by one person in one round trip
一人所到積 = Fraction(一籠積 * 總步數, 總步數)

# Total workers needed
用徒 = Fraction(積, 一人所到積)

# Results
a = 一人所到積
b = 用徒


"""
Code error: both arguments should be Rational instances"""
