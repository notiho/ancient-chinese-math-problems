"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
荅曰七萬六百六十六尺太半尺
負土往來七十步其二十步上下棚除棚除二當平道五踟躕之間十加一載輸之間三十步定一返一百四十步土籠積一尺六寸秋程人功行五十九里半問人到積尺用徒各幾何
術曰以一籠積尺乘程行步數為實往來上下棚除二當平道五置定往來步數十加一及載輸之間三十步以為法除之所得即一人所到尺以所到約積尺即用徒人數
荅曰人到 a尺 用徒 b人 
"""

#----- content starts here -----
"""
Suppose there is a basin-shaped pond. 
The upper width is 6 zhang, the upper length is 8 zhang. 
The lower width is 4 zhang, the lower length is 6 zhang. 
The depth is 2 zhang. 
Question: what is the volume?

Answer: 76066.5 chi³.

For moving the soil, the round trip is 70 bu. 
Of these, 20 bu are for the ascent and descent, where the shelves are removed. 
The shelves removed are equivalent to 2 bu, which are treated as flat ground. 
The hesitation in between is 10 bu, with an additional 1 bu for loading. 
The transportation distance is 30 bu. 
One round trip is fixed at 140 bu. 
The soil basket holds 1 chi 6 cun of soil. 
In autumn, the work rate is 59.5 li per person. 
Question: how much soil does one person transport, and how many workers are needed?

The procedure says: Multiply the volume of one basket of soil by the total number of steps in the journey to get the dividend. 
For the divisor, place the round trip steps (70 bu), the ascent and descent (20 bu), the shelves removed (2 bu treated as flat ground), the hesitation (10 bu), the additional loading (1 bu), and the transportation distance (30 bu). 
Divide the dividend by the divisor to get the amount of soil one person can transport. 
Divide the total soil volume by the amount transported by one person to get the number of workers needed.

Answer: one person transports *a* chi³, and *b* workers are needed.
"""

from fractions import Fraction

# 上廣六丈，袤八丈
上廣 = 6 * 10  # Convert zhang to chi
上袤 = 8 * 10  # Convert zhang to chi

# 下廣四丈，袤六丈
下廣 = 4 * 10  # Convert zhang to chi
下袤 = 6 * 10  # Convert zhang to chi

# 深二丈
深 = 2 * 10  # Convert zhang to chi

# 計算池的體積
# 積 = 深 × ((上廣 × 上袤 + 下廣 × 下袤) / 2)
積 = 深 * ((上廣 * 上袤 + 下廣 * 下袤) / 2)

# 積為 76066.5 尺³
池積 = Fraction(760665, 10)  # Representing 76066.5 as a fraction

# 土籠積一尺六寸
土籠積 = 1 + Fraction(6, 10)  # 1 chi 6 cun = 1.6 chi³

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚
上下棚步數 = 20

# 棚除二當平道五
棚除步數 = 2
棚當平道步數 = 5

# 踟躕之間十，加一載
踟躕步數 = 10
載步數 = 1

# 輸之間三十步
輸步數 = 30

# 一返一百四十步
一返步數 = 140

# 秋程人功行五十九里半
秋程人功 = 59 + Fraction(1, 2)  # 59.5 li

# 計算一人所到尺
# 實 = 土籠積 × 秋程人功 × 一返步數
實 = 土籠積 * 秋程人功 * 一返步數

# 法 = 往來步數 + 上下棚步數 + 棚當平道步數 + 踟躕步數 + 載步數 + 輸步數
法 = 往來步數 + 上下棚步數 + 棚當平道步數 + 踟躕步數 + 載步數 + 輸步數

# 一人所到尺 = 實 / 法
一人所到尺 = Fraction(實, 法)

# 計算用徒人數
# 用徒人數 = 池積 / 一人所到尺
用徒人數 = Fraction(池積, 一人所到尺)

# 答案
a = 一人所到尺
b = 用徒人數

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 204, Actual: 98
Variable 'b' has wrong value. Expected: 53000/153, Actual: 152133/196"""
