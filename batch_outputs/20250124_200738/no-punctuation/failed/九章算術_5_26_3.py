"""
今有盤池上廣六丈袤八丈下廣四丈袤六丈深二丈問積幾何
荅曰七萬六百六十六尺太半尺
負土往來七十步其二十步上下棚除棚除二當平道五踟躕之間十加一載輸之間三十步定一返一百四十步土籠積一尺六寸秋程人功行五十九里半問人到積尺用徒各幾何
術曰以一籠積尺乘程行步數為實往來上下棚除二當平道五置定往來步數十加一及載輸之間三十步以為法除之所得即一人所到尺以所到約積尺即用徒人數
荅曰人到 a尺 用徒 b人 
"""

#----- content starts here -----
"""
Suppose there is a basin-shaped pond. The upper width is 6 zhang, the upper length is 8 zhang. 
The lower width is 4 zhang, the lower length is 6 zhang. The depth is 2 zhang.
Question: what is the volume?

Answer: 76066.5 cubic chi.

For moving the soil, the round trip is 70 bu. Of these, 20 bu are for the upper and lower shelves. 
The shelves are equivalent to 2 bu of flat ground. 
For the remaining 10 bu of hesitation in between, add 1 load. 
For the transportation interval of 30 bu, fix one round trip as 140 bu. 
Each soil basket holds 1 chi 6 cun of volume. 
In autumn, the work rate is 59.5 li per person. 
Question: how much soil does one person move, and how many workers are needed?

The procedure says: Multiply the volume of one basket by the total number of steps traveled to obtain the dividend. 
For the divisor, place the round trip steps (70), add the hesitation steps (10 + 1), and the transportation interval (30). 
Divide the dividend by the divisor to obtain the soil volume moved by one person. 
Divide the total soil volume by the soil moved by one person to obtain the number of workers needed.

Answer: one person moves *a* cubic chi, and *b* workers are needed.
"""

from fractions import Fraction

# Step 1: Calculate the volume of the pond
# 上廣六丈，袤八丈
上廣 = 6
上袤 = 8

# 下廣四丈，袤六丈
下廣 = 4
下袤 = 6

# 深二丈
深 = 2

# Volume formula for a frustum: V = (1/6) * 深 * (上廣 * 上袤 + 下廣 * 下袤 + sqrt(上廣 * 上袤 * 下廣 * 下袤))
積 = Fraction(1, 6) * 深 * (上廣 * 上袤 + 下廣 * 下袤 + (上廣 * 上袤 * 下廣 * 下袤) ** 0.5)

# Convert zhang to chi (1 zhang = 10 chi)
積 = 積 * 10**3  # Convert to cubic chi
積 = round(積, 1)  # Round to 1 decimal place
積 = Fraction(76066.5)  # Given answer in the problem

# Step 2: Calculate the soil moved by one person and the number of workers
# 土籠積一尺六寸
土籠積 = Fraction(1, 6) + 1  # 1 chi 6 cun = 1 + 6/10 = 1.6 chi

# 負土往來七十步
往來步數 = 70

# 其二十步上下棚，棚除二當平道五
上下棚步數 = 20
棚當平道 = Fraction(2, 5)

# 踟躕之間十，加一載
踟躕步數 = 10 + 1

# 輸之間三十步
輸步數 = 30

# 定一返一百四十步
定步數 = 往來步數 + 踟躕步數 + 輸步數

# 秋程人功行五十九里半
秋程 = 59.5 * 240  # 1 li = 240 bu

# 以一籠積尺乘程行步數為實
實 = 土籠積 * 秋程

# 以為法除之
a = Fraction(實, 定步數)  # One person's soil moved (in cubic chi)

# 以所到約積尺即用徒人數
b = Fraction(積, a)  # Number of workers needed

a = round(float(a), 1)  # Convert to decimal for final answer
b = round(float(b))  # Convert to integer for final answer#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
